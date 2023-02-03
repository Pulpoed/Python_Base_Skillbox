# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (700, 600)

colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

print('''Возможные фигуры:
      0 : треугольник
      1 : квадрат
      2 : пятиугольник
      3 : шестиугольник''')
n_shape = input('Введите желаемую фигуру:')
while int(n_shape) > 3:
    print("Некорректный номер")
    n_shape = input('Введите желаемую фигуру:')

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
    v_init.draw(color=colors[int(color)])
    tuple_of_shapes = (angle + 120, angle + 240), \
                      (angle + 90, angle + 180, angle + 270), \
                      (angle + 72, angle + 144, angle + 216, angle + 288), \
                      (angle + 60, angle + 120, angle + 180, angle + 240, angle + 300)
    for next_angle in tuple_of_shapes[n_shape]:
        v_next = sd.get_vector(start_point=v_init.end_point, angle=next_angle, length=length, width=3)
        v_next.draw(color=colors[int(color)])
        v_init = v_next


draw_shape(200, 200, 5, 200, int(n_shape))

sd.pause()
