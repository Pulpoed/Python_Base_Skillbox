#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка

import simple_draw as sd

sd.resolution = (1200, 700)
snowflakes = {}


# def generate(snowflake_count):
#     for i in range(snowflake_count):
#         snowflakes[i] = {'x': sd.random_number(50, sd.resolution[0]),
#                          'y': sd.random_number(sd.resolution[1] - 200, sd.resolution[1]),
#                          'size': sd.random_number(5, 30)}
#     return snowflakes


def generate(snowflake_count):
    for i in range(snowflake_count):
        snowflakes[i] = {'x': sd.random_number(50, sd.resolution[0]),
                         'y': sd.random_number(sd.resolution[1] - 200, sd.resolution[1]),
                         'size': sd.random_number(5, 30)}
    return snowflakes

# generate(2)
# print(snowflakes)
# del snowflakes[1]
# print(snowflakes)


def draw(color):
    for snowflake_num, snowflake_param in snowflakes.items():
        point = sd.get_point(snowflake_param['x'], snowflake_param['y'])
        sd.snowflake(center=point,
                     length=snowflake_param['size'],
                     color=color)


def move():
    for snowflake_num, snowflake_param in snowflakes.items():
        snowflake_param['x'] += sd.random_number(-2, 2)
        snowflake_param['y'] -= sd.random_number(2, 5)


def got_down():
    for snowflake_num, snowflake_param in snowflakes.items():
        if snowflake_param['y'] < 0:
            return snowflake_num


def delete_fallen(snowflake_num):
    del snowflakes[snowflake_num]
