#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий запуск программы"""
import os
from program import BruteForce
from program import BoyerMoore
from program import RabinKarp
from program import KnuthMorrisPratt
from program import Algorithms
import argparse
from create_csv import return_table
from create_2d_graphs import return_2d_graphs
from create_3d_graphs import return_3d_graphs


def get_result(alg, st, sub):
    """Метод, возвращающий результат поиска указанного алгоритма"""
    algo = Algorithms
    bf = BruteForce('bf', st, sub)
    bm = BoyerMoore('bm', st, sub)
    rk1 = RabinKarp('rk1', st, sub)
    rk2 = RabinKarp('rk2', st, sub)
    rk3 = RabinKarp('rk3', st, sub)
    kmp = KnuthMorrisPratt('kmp', st, sub)

    for i in algo.__subclasses__():
        if alg == i.__name__[0]:
            return bf.search(st, sub)
        elif alg == i.__name__[1]:
            return bm.search(st, sub)
        elif alg == i.__name__[2]:
            return rk1.search_mod_hash(st, sub)
        elif alg == i.__name__[3]:
            return rk2.search_brute_hash(st, sub)
        elif alg == i.__name__[4]:
            return rk3.search_mult_hash(st, sub)
        else:
            return kmp.search(st, sub)


def get_contains(algorithm, filename):
    """Метод, осуществляющий работу с файлом, из которого производится чтение"""
    st = ''
    with open(filename) as t:
        for i in t:
            st += i + ' '
    s = st.split(' ')
    text = s[0]
    pattern = s[1]
    result = get_result(algorithm, text, pattern)
    return result


def parsing():
    """Метод, осуществляющий парсинг и возвращающий результат поиска статистику"""
    parser = argparse.ArgumentParser(description='Search for a substring in a string and finding statistics')
    parser.add_argument('-alg', '--algorithm', type=str, metavar='',
                        help='Algorithms for a search:\nBruteForce, BoyerMoore, '
                             'RabinKarp1_mod_hash, RabinKarp2_mult_hash, RabinKarp3_brute_hash, KnuthMorrisPratt')
    parser.add_argument('-st', '--string', type=str, metavar='', help='String for a search')
    parser.add_argument('-sub', '--substring', type=str, metavar='', help='Substring for a search')
    parser.add_argument('-doc', '--document', type=str, metavar='', help='Searching data')
    parser.add_argument('-file', '--file', type=str, metavar='', help='The path of the file in which to save statistics')
    args = parser.parse_args()
    algorithm = args.algorithm
    string = args.string
    substring = args.substring
    doc = args.document
    file = args.file

    if algorithm is None and substring is None and string is None and doc is None:
        alg = input('Введите алгоритм поиска: ')
        st = input('Введите строку для поиска: ')
        sub = input('Введите подстроку для поиска: ')
        result = get_result(alg, st, sub)
        print(result)
    elif doc is not None and string is None and substring is None:
        result = get_contains(algorithm, doc)
        print(result)
    else:
        result = get_result(algorithm, string, substring)
        print(result)

    if file is None:
        file = 'file.csv'
        path = os.path.abspath(file)
        return_table(file)
        return_3d_graphs(path), return_2d_graphs(path)
        os.remove(path)
    else:
        return_table(file)


if __name__ == '__main__':
    parsing()
