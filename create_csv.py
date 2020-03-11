#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, возвращающий результаты производительности работы для алгоритмов поиска"""
import csv
import os

from pip._vendor.distlib._backport import shutil

from timing_and_capacity import return_res_2d
from timing_and_capacity import return_res_3d
from timing_and_capacity import return_algs


def get_csv_4_fix(key, filename, increment, name_algs):
    """Метод, заполняющий таблицу для случая фиксированной длины подстроки"""
    res = []
    for n in name_algs.keys():
        alg = return_algs(n)
        data = return_res_2d(alg, key)
        for i in data:
            name = str(i[0]) + '_' + n
            r = [name, (i[1] * increment, i[2] * increment)]
            res.append(r)
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(res)
            res.clear()


def get_csv_4_chng(key, filename, increment, name_algs):
    """Метод, заполняющий таблицу для случая различной длины подстроки"""
    res = []
    for n in name_algs.keys():
        alg = return_algs(n)
        data = return_res_3d(alg, key)
        for i in data:
            name = str(i[0]) + '_' + str(i[1]) + '_' + n
            r = [name, i[2] * increment]
            res.append(r)
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(res)
            res.clear()


def return_table(file):
    """Метод, заполняющий таблицу целиком"""
    algs = {'b_f': 'грубой силы', 'b_m': 'Бойера-Мура', 'r_k_mod': 'Рабина-Карпа (1)', 'r_k_mult': 'Рабина-Карпа (2)',
            'r_k_brute': 'Рабина-Карпа (3)', 'k_m_p': 'Кнута-Морриса-Пратта'}
    get_csv_4_fix(0, file, 100000000, algs)
    get_csv_4_fix(1, file, 10000, algs)
    get_csv_4_chng(0, file, 100000000, algs)
    get_csv_4_chng(1, file, 10000, algs)
