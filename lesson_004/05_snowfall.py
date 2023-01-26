# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# x1 = sd.random_number(50, 1000)
# y1 = 500
#
# x2 = sd.random_number(50, 1000)
# y2 = 500

snowflakes = {}
snowflake_count = 30

for i in range(snowflake_count):
    snowflakes[i] = {'x': sd.random_number(50, sd.resolution[0]),
                     'y': sd.random_number(100, sd.resolution[1]),
                     'size': sd.random_number(5, 30)}

while True:

    sd.start_drawing()
    for snowflake_num, snowflake_param in snowflakes.items():
        point = sd.get_point(snowflake_param['x'], snowflake_param['y'])
        sd.snowflake(center=point,
                     length=snowflake_param['size'],
                     color=sd.background_color)

        snowflake_param['x'] += sd.random_number(-2, 2)
        snowflake_param['y'] -= sd.random_number(2, 5)
        next_point = sd.get_point(snowflake_param['x'], snowflake_param['y'])

        sd.snowflake(center=next_point,
                     length=snowflake_param['size'])
        if snowflake_param['y'] < sd.random_number(0, 30):
            snowflake_param['y'] += 600

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


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
