#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, строящий графики для случая различной длины подстроки"""
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def get_3d_graph(filename, name_algs):
    length = []
    sub = []
    res = []
    rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    i = 72
    key = 1
    while 72 <= i < len(rows)-45:
        begin = i
        if i < 347:
            title = 'время в сек * 10^8'
            value = 'времени'
        else:
            title = 'использование памяти MB/SEC * 10^4'
            value = 'памяти'
        for j in range(44):
            length.append(int(rows[begin][0].split('_')[0]))
            sub.append(int(rows[begin][0].split('_')[1]))
            res.append(float((rows[begin][1])))
            begin += 1
        dpi = 80
        fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(length, sub, res, c='r', marker='o')
        main_title = 'Сопоставление производительности по ' + value + ' с различной\nдлиной подстроки для ' \
                                                                      'алгоритма ' + name_algs[return_name(key)]
        plt.title(main_title)
        ax.set_xlabel('длина строки')
        ax.set_ylabel('длина подстроки')
        ax.set_zlabel(title)
        plt.show()
        plt.close()
        length.clear()
        sub.clear()
        res.clear()
        i += 44
        key += 1


def return_3d_graphs(file):
    algs = {'b_f': 'грубой силы', 'b_m': 'Бойера-Мура', 'r_k_mod': 'Рабина-Карпа (1)', 'r_k_mult': 'Рабина-Карпа (2)',
                  'r_k_brute': 'Рабина-Карпа (3)', 'k_m_p': 'Кнута-Морриса-Пратта'}
    get_3d_graph(file, algs)


def return_name(key):
    names = {1: 'b_f', 2: 'b_m', 3: 'r_k_mod', 4: 'r_k_mult', 5: 'r_k_brute', 6: 'k_m_p',
              7: 'b_f', 8: 'b_m', 9: 'r_k_mod', 10: 'r_k_mult', 11: 'r_k_brute', 12: 'k_m_p'}
    return names[key]
