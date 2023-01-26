#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.


my_list = list(
    [my_favorite_movies[:10]] +
    [my_favorite_movies[12:25]] +
    [my_favorite_movies[27:33]] +
    [my_favorite_movies[35:40]] +
    [my_favorite_movies[42:]])
print(my_list[0] + ' ' + my_list[-1] + ' ' + my_list[1] + ' ' + my_list[-2])
