# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 700)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(50, sd.resolution[0])
        self.y = sd.random_number(sd.resolution[1] - 500, sd.resolution[1])
        self.size = sd.random_number(8, 20)
        self.factor_a = sd.random_number(1, 10) / 10
        self.factor_b = sd.random_number(1, 10) / 10
        self.factor_c = sd.random_number(1, 120)

    def __str__(self):
        return 'x {}, y {}, size {}'.format(self.x, self.y, self.size)

    def draw(self, color=sd.COLOR_WHITE):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point,
                     length=self.size,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c, )

    def move(self):
        self.y -= sd.random_number(2, 5)
        self.x += sd.random_number(-2, 2)

    def hide(self, color=sd.background_color):
        self.draw(color)

    def cant_fall(self):
        if self.y <= sd.random_number(0, 30):
            return True


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

# создать список снежинок
# flakes = get_flakes(count=N)

snowfall = {}
flakes_count = 30

for i in range(flakes_count):
    snowfall[i] = Snowflake()

while True:
    for num, flake in snowfall.items():
        sd.start_drawing()
        flake.hide()
        flake.move()
        flake.draw()
        if flake.cant_fall() is True:
            flake.y = flake.y + 700
            flake.x = flake.x + sd.random_number(-400, +400)
        sd.finish_drawing()
        sd.sleep(0.0005)
    if sd.user_want_exit():
        break

# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
