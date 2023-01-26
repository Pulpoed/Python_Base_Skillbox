# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.resolution = (700, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

print('''Возможные цвета:
      0 : red
      1 : orange
      3 : yellow
      4 : cyan
      5 : blue
      6 : purple''')
color = input('Введите желаемый цвет:')
while int(color) > 6:
    print("Некорректный номер")
    color = input('Введите желаемый цвет:')


def draw_shape(sp_x, sp_y, angle, length, n_shape):
    v_init = sd.get_vector(start_point=sd.get_point(sp_x, sp_y), angle=angle, length=length, width=3)
    v_init.draw(color=rainbow_colors[int(color)])
    tuple_of_shapes = (angle + 120, angle + 240), \
                      (angle + 90, angle + 180, angle + 270), \
                      (angle + 72, angle + 144, angle + 216, angle + 288), \
                      (angle + 60, angle + 120, angle + 180, angle + 240, angle + 300)
    for next_angle in tuple_of_shapes[n_shape]:
        v_next = sd.get_vector(start_point=v_init.end_point, angle=next_angle, length=length, width=3)
        v_next.draw(color=rainbow_colors[int(color)])
        v_init = v_next


def draw_triangle(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=0)


def draw_rectangle(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=1)


def draw_pentagon(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=2)


def draw_hexagon(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=3)


draw_triangle(50, 370, 20, 200)
draw_rectangle(90, 50, 22, 200)
draw_pentagon(500, 320, 20, 130)
draw_hexagon(500, 50, 22, 100)

sd.pause()