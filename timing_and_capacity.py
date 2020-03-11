#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, фиксирующий время и объем затрачиваемой памяти при работе алгоритмов"""
import timeit
from program import BruteForce
from program import BoyerMoore
from program import RabinKarp
from program import KnuthMorrisPratt
from generator import Generator
from functools import partial
from memory_profiler import memory_usage


gen = Generator()
alphabet = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
st = gen.generate(100, alphabet)
sub = st
bf = BruteForce('bf', st, sub)
bm = BoyerMoore('bm', st, sub)
rk = RabinKarp('rk', st, sub)
kmp = KnuthMorrisPratt('kmp', st, sub)


def b_f(text, pattern):
    brute = bf.search(text, pattern)
    return brute


def b_m(text, pattern):
    boyer = bm.search(text, pattern)
    return boyer


def r_k_mod(text, pattern):
    rabin = rk.search_mod_hash(text, pattern)
    return rabin


def r_k_mult(text, pattern):
    rabin = rk.search_mult_hash(text, pattern)
    return rabin


def r_k_brute(text, pattern):
    rabin = rk.search_brute_hash(text, pattern)
    return rabin


def k_m_p(text, pattern):
    knutt = kmp.search(text, pattern)
    return knutt


def universal(alg, length, left, right):
    """Метод, возвращающий время и объем затрачиваемой памяти для задаваемого случая"""
    text = gen.generate(length, alphabet)
    pattern = text[left:right]
    times_dry_run = timeit.Timer(partial(alg, text, pattern)).repeat(1, 1)
    times = timeit.Timer(partial(alg, text, pattern)).repeat(10, 10)
    time_working = times[2] / 10
    memory_dry_run = timeit.Timer(partial(alg, text, pattern)).repeat(1, 1)
    memory = memory_usage()[0] / 10
    dry_run = [times_dry_run, memory_dry_run]
    return time_working, memory


def count_cases_fix_sub(alg):
    """Метод, возвращающий результаты замеров по времени и памяти для лучшего и худшего случая для различной длины
    строки и фиксированной длины подстроки"""
    length = 100
    result_time_4_fix_sub = []
    result_memo_4_fix_sub = []
    # каждые 3 элемента в tuple: 1-длина, 2-лучшее время/память, 3-худшее время/память
    for i in range(6):
        good_begin = int(length/(i+2))
        good_time_case = universal(alg, length, good_begin, good_begin + 20)[0]
        worst_time_case = universal(alg, length, length - 20, length - 3)[0]
        result_time_4_fix_sub.append((length, good_time_case, worst_time_case))
        good_memo_case = universal(alg, length, good_begin, good_begin + 20)[1]
        worst_memo_case = universal(alg, length, length - 20, length - 3)[1]
        result_memo_4_fix_sub.append((length, good_memo_case, worst_memo_case))
        length *= 2
    return result_time_4_fix_sub, result_memo_4_fix_sub


def count_cases_chng_sub(alg):
    """Метод, возвращающий результаты замеров по времени и памяти для случая различной длины
    строки и различной длины подстроки"""
    result_time_4_chng_sub = []
    result_memo_4_chng_sub = []
    for length in range(20, 101, 10):
        for sub in range(2, 11, 2):
            begin = int(length/2)
            end = int(length/2 + sub)
            time_case = universal(alg, length, begin, end)[0]
            result_time_4_chng_sub.append((length, sub, time_case))
            memo_case = universal(alg, length, begin, end)[1]
            result_memo_4_chng_sub.append((length, sub, memo_case))
    return result_time_4_chng_sub, result_memo_4_chng_sub


def return_res_2d(alg, key):
    """Метод, возвращающий замеры для случая фиксированной длины подстроки"""
    return count_cases_fix_sub(alg)[key]


def return_res_3d(alg, key):
    """Метод, возвращающий замеры для случая различной длины подстроки"""
    return count_cases_chng_sub(alg)[key]


def return_algs(alg):
    """Метод, возвращающий алгоритмы"""
    algs = {'b_f': b_f, 'b_m': b_m, 'r_k_mod': r_k_mod, 'r_k_mult': r_k_mult, 'r_k_brute': r_k_brute, 'k_m_p': k_m_p}
    return algs[alg]
