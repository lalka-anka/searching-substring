#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, содержащий алгоритмы поиска"""


class Algorithms:
    def __init__(self, name, st, sub):
        self.name = name
        self.string = st
        self.substring = sub


class BruteForce(Algorithms):
    """
    Поиск через алгоритм грубой силы

    Алгоритм, основанный на методе грубой силы, для решения общей задачи поиска называется последовательным поиском.
    Этот алгоритм просто по очереди сравнивает элементы заданного списка с ключом поиска до тех пор,
    пока не будет найден элемент с указанным значением ключа.
    """
    def search(self, st, sub):
        index = -1
        str_len = len(st)
        sub_len = len(sub)
        for i in range(str_len - sub_len + 1):
            success = True
            for j in range(sub_len):
                if sub[j] is not st[i + j]:
                    success = False
                    break
            if success:
                index = i
                break
        return index


class BoyerMoore(Algorithms):
    """
    Ппоиск через алгоритм Бойера-Мура

    Совмещается начало текста (строки) и шаблона, проверка начинается с последнего символа шаблона.
    Если символы совпадают, производится сравнение предпоследнего символа шаблона и т. д.
    Если все символы шаблона совпали с наложенными символами строки, значит, подстрока найдена,
    и выполняется поиск следующего вхождения подстроки.
    """
    def search(self, txt, pat):
        sub_len = len(pat)
        st_len = len(txt)
        bad_char = [-1] * 256
        for i in range(sub_len):
            bad_char[ord(pat[i])] = i
        index = 0
        s = 0
        while s <= st_len - sub_len:
            j = sub_len - 1
            while j >= 0 and pat[j] == txt[s + j]:
                j -= 1

            if j < 0:
                index = s
                s += (sub_len - bad_char[ord(txt[s + sub_len])] if s + sub_len < st_len else 1)
            else:
                s += max(1, j - bad_char[ord(txt[s + j])])
        if index == 0:
            index = -1
        return index


class RabinKarp(Algorithms):
    """
    Поиск через алгоритм Рабина-Карпа

    Алгоритм поиска строки, который ищет шаблон в тексте, используя хеширование.
    """
    def search_mod_hash(self, st, sub):
        """Хеширование по модулю"""
        basis = 256
        prime = 101
        str_len = len(st)
        sub_len = len(sub)
        hash_ = pow(basis, sub_len - 1) % prime
        sub_mod = 0
        str_mod = 0
        result = []
        for i in range(sub_len):
            sub_mod = (basis * sub_mod + ord(sub[i])) % prime
            str_mod = (basis * str_mod + ord(st[i])) % prime
        for s in range(str_len - sub_len + 1):
            if sub_mod == str_mod:
                match = True
                for i in range(sub_len):
                    if sub[i] != st[s + i]:
                        match = False
                        break
                if match:
                    result = result + [s]
            if s < str_len - sub_len:
                str_mod = (str_mod - hash_ * ord(st[s])) % prime
                str_mod = (str_mod * basis + ord(st[s + sub_len])) % prime
                str_mod = (str_mod + prime) % prime
        if not result:
            index = -1
        else:
            index = result[0]
        return index

    def search_mult_hash(self, st, sub):
        """Хеширование через умножение на константу и взятие модуля"""
        index = -1
        prime = 88730
        str_len = len(st)
        sub_len = len(sub)
        sub_hash = 0
        str_hash = 0
        shift = 1
        error = True
        variable = sub_len - 1
        while variable >= 0:
            sub_hash += ord(sub[variable]) * shift % prime
            str_hash += ord(st[variable]) * shift % prime
            variable -= 1
        for i in range(str_len - sub_len + 1):
            if sub_hash == str_hash:
                for j in range(sub_len):
                    error = False
                    if sub[j] != st[i + j]:
                        error = True
                        break
                if not error:
                    index = i
                    return index
                else:
                    return index
            if i != str_len - sub_len:
                str_hash = (str_hash - ord(st[i]) * shift + ord(st[i + sub_len])) % prime
            else:
                index = -1
                return index

    def search_brute_hash(self, st, sub):
        """Прямое хеширование"""
        str_len = len(st)
        sub_len = len(sub)
        error = True
        sub_hash = 0
        str_hash = 0
        index = -1
        for i in range(sub_len):
            sub_hash += ord(sub[i])
            str_hash += ord(st[i])
        for i in range(str_len - sub_len + 1):
            if str_hash == sub_hash:
                for j in range(sub_len):
                    error = False
                    if sub[j] != st[i + j]:
                        error = True
                        break
                if not error:
                    index = i
                    return index
                else:
                    return index
            if i != str_len - sub_len:
                str_hash = str_hash - ord(st[i]) + ord(st[i + sub_len])
            else:
                index = -1
                return index


class KnuthMorrisPratt(Algorithms):
    """
    Поиск через алгоритм Кнута-Морриса-Пратта

    Осуществляется сдвиг по строке и символы последовательно сравниваются с образцом. Не совпало - начало
    сравнения перемещается на один шаг и снова сравнивается. И так до тех пор, пока образец не будет найден.
    """
    def search(self, st, sub):
        d = {0: 0}
        str_len = len(st)
        sub_len = len(sub)
        for i in range(1, sub_len):
            j = d[i - 1]
            while j > 0 and sub[j] is not sub[i]:
                j = d[j - 1]
            if sub[j] == sub[i]:
                j += 1
            d[i] = j
        i = j = 0
        while i < str_len and j < sub_len:
            if sub[j] == st[i]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = d[j - 1]
        else:
            if j == sub_len:
                index = i - j
                return index
        return -1
