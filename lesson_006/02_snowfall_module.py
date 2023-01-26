# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall_gen as sg

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


sd.resolution = (1200, 700)

sg.generate(10)

while True:
    sd.start_drawing()
    sg.draw(color=sd.background_color)
    sg.move()
    sg.draw(color=sd.COLOR_WHITE)
    if sg.got_down():
        sg.delete_fallen(sg.got_down())
        sg.generate(10)
    sd.finish_drawing()
    sd.sleep(0.005)
    if sd.user_want_exit():
        break

sd.pause()
