#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, строящий графики для случая фиксированной длины подстроки"""
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl


def get_2d_graph(filename, name_algs):
    length = []
    good = []
    worst = []
    rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    i = 0
    key = 1
    while 0 <= i <= 72 - 6:
        begin = i
        if i < 35:
            title = 'время в сек * 10^8'
            value = 'времени'
        else:
            title = 'использование памяти MB/SEC * 10^4'
            value = 'памяти'

        for j in range(6):
            length.append(int(rows[begin][0].split('_')[0]))
            t = rows[begin][1][1:-1].split(',')
            g = float(t[0])
            w = float(t[1])
            good.append(g)
            worst.append(w)
            begin += 1
        main_title = 'Сопоставление производительности по ' + value + ' с различной\nдлиной строки для алгоритма ' \
                     + name_algs[return_name(key)]

        dpi = 80
        plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
        mpl.rcParams.update({'font.size': 9})
        plt.title(main_title)
        plt.xlabel('длина строки')
        plt.ylabel(title)
        plt.plot(length, good, 'bo-', label='good case', color='blue')
        plt.plot(length, worst, 'r^-', label='worst case', color='red')
        plt.legend(loc='upper right')
        plt.show()
        plt.close()
        i += 6
        key += 1
        length.clear()
        good.clear()
        worst.clear()


def return_2d_graphs(file):
    algs = {'b_f': 'грубой силы', 'b_m': 'Бойера-Мура', 'r_k_mod': 'Рабина-Карпа (1)', 'r_k_mult': 'Рабина-Карпа (2)',
            'r_k_brute': 'Рабина-Карпа (3)', 'k_m_p': 'Кнута-Морриса-Пратта'}
    get_2d_graph(file, algs)


def return_name(key):
    names = {1: 'b_f', 2: 'b_m', 3: 'r_k_mod', 4: 'r_k_mult', 5: 'r_k_brute', 6: 'k_m_p',
             7: 'b_f', 8: 'b_m', 9: 'r_k_mod', 10: 'r_k_mult', 11: 'r_k_brute', 12: 'k_m_p'}
    return names[key]
