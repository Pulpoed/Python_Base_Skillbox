# -*- coding: utf-8 -*-

import random
# (определение функций)
import simple_draw as sd

sd.resolution = (700, 700)


def face(x, y):
    big_round = sd.get_point(x, y)
    left_eye = sd.get_point(x + 17, y + 10)
    right_eye = sd.get_point(x - 15, y + 12)
    mouth_1 = sd.get_point(x - 10, y - 10)
    mouth_2 = sd.get_point(x, y - 15)
    mouth_3 = sd.get_point(x + 10, y - 10)
    sd.circle(center_position=big_round, radius=50, color=sd.COLOR_YELLOW, width=2)
    sd.circle(center_position=left_eye, radius=5, color=sd.COLOR_YELLOW, width=2)
    sd.circle(center_position=right_eye, radius=5, color=sd.COLOR_PURPLE, width=2)
    sd.lines([mouth_1, mouth_2, mouth_3], color=sd.COLOR_YELLOW, closed=False, width=2)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

for _ in range(10):
    face(random.randint(50, 600), random.randint(50, 600))
    sd.sleep(1)
sd.pause()
