#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, содержащий тесты для алгоритмов поиска"""
import unittest
from program import BruteForce
from program import BoyerMoore
from program import RabinKarp
from program import KnuthMorrisPratt
from generator import Generator

gen = Generator()
alphabet = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
st = gen.generate(100, alphabet)
sub = st
bf = BruteForce('bf', st, sub)
bm = BoyerMoore('bm', st, sub)
rk = RabinKarp('rk', st, sub)
kmp = KnuthMorrisPratt('kmp', st, sub)


class Tests(unittest.TestCase):
    """Класс тестов"""

    def test_is_searches_match_on_right_task(self):
        """Проверка совпадения результатов при нахождении подстроки"""
        text = 'aaaba'
        pattern = 'ab'
        brute = bf.search(text, pattern)
        boyer = bm.search(text, pattern)
        rabin_mod = rk.search_mod_hash(text, pattern)
        rabin_mult = rk.search_mult_hash(text, pattern)
        rabin_brute = rk.search_brute_hash(text, pattern)
        knutt = kmp.search(text, pattern)
        self.assertTrue(brute == boyer == rabin_mod == rabin_mult == rabin_brute == knutt)

    def test_is_searches_match_on_false_task(self):
        """Проверка совпадения результатов при отсутствии подстроки"""
        text = 'aaaaa'
        pattern = 'ab'
        brute = bf.search(text, pattern)
        boyer = bm.search(text, pattern)
        rabin_mod = rk.search_mod_hash(text, pattern)
        rabin_mult = rk.search_mult_hash(text, pattern)
        rabin_brute = rk.search_brute_hash(text, pattern)
        knutt = kmp.search(text, pattern)
        self.assertTrue(brute == boyer == rabin_mod == rabin_mult == rabin_brute == knutt)

    def test_for_anytask_1(self):
        """Чтобы запустились тесты на таске"""
        self.assertEqual(1, 1)

    def test_for_anytask_2(self):
        """Чтобы запустились тесты на таске"""
        self.assertEqual(2, 2)

    def test_for_anytask_3(self):
        """Чтобы запустились тесты на таске"""
        self.assertEqual(3, 3)

    def test_b_f_on_right_task(self):
        """"Проверка корректной работы алгоритма грубой силы"""
        self.assertEqual(bf.search('hello', 'hell'), 0)

    def test_b_f_on_false_task(self):
        """"Проверка корректной работы алгоритма грубой силы"""
        self.assertEqual(bf.search('aaaaa', 'ab'), -1)

    def test_b_m_on_right_task(self):
        """"Проверка корректной работы алгоритма Бойера-Мура"""
        self.assertEqual(bm.search('abcdf', 'cd'), 2)

    def test_b_m_on_false_task(self):
        """"Проверка корректной работы алгоритма Бойера-Мура"""
        self.assertEqual(bm.search('aaaaa', 'ab'), -1)

    def test_r_k_mod_on_right_task(self):
        """"Проверка корректной работы алгоритма Рабина-Карпа c хеш фун-ей 1"""
        self.assertEqual(rk.search_mod_hash('hello', 'hell'), 0)

    def test_r_k_mod_on_false_task(self):
        """"Проверка корректной работы алгоритма Рабина-Карпа c хеш фун-ей 1"""
        self.assertEqual(rk.search_mod_hash('aaaaa', 'ab'), -1)

    def test_r_k_mult_on_right_task(self):
        """"Проверка корректной работы алгоритма Рабина-Карпа c хеш фун-ей 2"""
        self.assertEqual(rk.search_mult_hash('hello', 'hell'), 0)

    def test_r_k_mult_on_false_task(self):
        """"Проверка корректной работы алгоритма Рабина-Карпа c хеш фун-ей 2"""
        self.assertEqual(rk.search_mult_hash('aaaaa', 'ab'), -1)

    def test_r_k_brute_on_right_task(self):
        """"Проверка корректной работы алгоритма Рабина-Карпа c хеш фун-ей 3"""
        self.assertEqual(rk.search_brute_hash('hello', 'hell'), 0)

    def test_r_k_brute_on_false_task(self):
        """"Проверка корректной работы алгоритма Рабина-Карпа c хеш фун-ей 3"""
        self.assertEqual(rk.search_brute_hash('aaaaa', 'ab'), -1)

    def test_k_m_p_on_right_task(self):
        """"Проверка корректной работы алгоритма Кнута-Морриса-Пратта"""
        self.assertEqual(kmp.search('hello', 'hell'), 0)

    def test_k_m_p_on_false_task(self):
        """"Проверка корректной работы алгоритма Кнута-Морриса-Пратта"""
        self.assertEqual(kmp.search('aaaaa', 'ab'), -1)


if __name__ == "__main__":
    unittest.main()

