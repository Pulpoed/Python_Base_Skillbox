# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    my_exceptions = (IamGodError('Я бог'),
                     DrunkError('Я напился'),
                     CarCrashError("Я в аварии"),
                     GluttonyError("Я обожрался"),
                     DepressionError("Я в депрессии"),
                     SuicideError("Я роскомнадзор"))
    if random.randint(1, 13) == 13:
        raise random.choice(my_exceptions)
    return random.randint(1, 7)


file_out = 'file_out.txt'
file = open(file_out, mode='w')
while True:
    try:
        carma += one_day()
        file.write(str(carma)+'\n')
        if carma >= ENLIGHTENMENT_CARMA_LEVEL:
            break
    except (IamGodError,
            DrunkError,
            CarCrashError,
            GluttonyError,
            DepressionError,
            SuicideError) as exc:
        file.write(f'{exc}, {exc.__class__.__name__}, {exc.args} \n')
file.write("Цикл завершен")
file.close()


# https://goo.gl/JnsDqu
