# -*- coding: utf-8 -*-

import simple_draw as sd


sd.resolution = (1200, 600)


def draw_snowfall(snowflake_count):
    snowflakes = {}

    for i in range(snowflake_count):
        snowflakes[i] = {'x': sd.random_number(50, sd.resolution[0]),
                         'y': sd.random_number(100, sd.resolution[1]),
                         'size': sd.random_number(5, 30)}

    while True:

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

        if sd.user_want_exit():
            break


draw_snowfall(30)

sd.pause()
