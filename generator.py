#!/usr/bin/env python3
"""Модуль, осуществляющий генерацию текста"""
import random


class Generator:
    def generate(self, length, alphabet):
        return ''.join([random.choice(list(alphabet)) for x in range(length)])

    def generate_number(self, begin, end):
        return random.randint(begin, end)
