# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            new_elem = Storm()
            return new_elem
        elif isinstance(other, Fire):
            new_elem = Steam()
            return new_elem
        elif isinstance(other, Earth):
            new_elem = Dirt()
            return new_elem


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            new_elem = Lightning()
            return new_elem
        elif isinstance(other, Earth):
            new_elem = Dust()
            return new_elem
        elif isinstance(other, Water):
            new_elem = Storm()
            return new_elem


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            new_elem = Lava()
            return new_elem
        elif isinstance(other, Water):
            new_elem = Steam()
            return new_elem
        elif isinstance(other, Air):
            new_elem = Lightning()
            return new_elem


class Earth:
    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Fire):
            new_elem = Lava()
            return new_elem
        elif isinstance(other, Water):
            new_elem = Dirt()
            return new_elem
        elif isinstance(other, Air):
            new_elem = Dust()
            return new_elem


class Storm:
    def __str__(self):
        return self.__class__.__name__


class Steam:
    def __str__(self):
        return self.__class__.__name__


class Dirt:
    def __str__(self):
        return self.__class__.__name__


class Lightning:
    def __str__(self):
        return self.__class__.__name__


class Dust:
    def __str__(self):
        return self.__class__.__name__


class Lava:
    def __str__(self):
        return self.__class__.__name__


water = Water()
air = Air()
fire = Fire()
earth = Earth()

print("water + air = ", water + air)
print("water + fire = ", water + fire)
print("water + earth = ", water + earth)
print("air + fire = ", air + fire)
print("air + earth = ", air + earth)
print("earth + fire = ", earth + fire)

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
