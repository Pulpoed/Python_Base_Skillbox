# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

def snowfall():
    x_gen = sd.random_number(100, 1100)
    y_gen = 500
    point_gen = sd.get_point(x_gen, y_gen)
    coeff_size = sd.random_number(7, 13) * 0.1
    size = 50 * coeff_size
    sd.snowflake(point_gen, size)
    sd.sleep(0.2)
    sd.snowflake(point_gen, size, sd.background_color)
    while True:
        x_move = x_gen + sd.random_number(-20, 20)
        y_move = y_gen - 20
        point_move = sd.get_point(x_move, y_move)
        sd.snowflake(point_move, size)
        sd.sleep(0.2)
        if y_move < 50:
            break
        sd.snowflake(point_move, size, sd.background_color)
        x_gen, y_gen = x_move, y_move


for x in range (1,20):
    snowfall()
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
