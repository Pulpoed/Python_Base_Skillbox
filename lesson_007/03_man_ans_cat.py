# -*- coding: utf-8 -*-

from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Cat:

    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот {}, сытость {}'.format(self.cat_name, self.fullness)

    def sleep(self):
        self.fullness -= 10
        print('{} поспал'.format(self.cat_name))

    def eat(self):
        if self.house.cat_food >= 10:
            print('{} поел'.format(self.cat_name))
            self.fullness += 10
            self.house.cat_food -= 10
        else:
            print('Для {} нет корма'.format(self.cat_name))
            self.fullness -= 10

    def mess(self):
        self.house.dirt += 5
        print('{} подрал обои'.format(self.cat_name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.cat_name))
            return
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.mess()
        else:
            self.sleep()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return '{} сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))
            self.fullness -= 10

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        print('{} геймил целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 10
        else:
            print('{} деньги кончились!'.format(self.name))

    def zoo_shopping(self):
        if self.house.money >= 50:
            print('{} сходил в зоомагазин за кошачьим кормом'.format(self.name))
            self.house.money -= 150
            self.house.cat_food += 150
            self.fullness -= 10
        else:
            print('{} деньги кончились!'.format(self.name))

    def clean(self):
        if self.fullness >= 21:
            print('{} затеял уборку'.format(self.name))
            self.house.dirt -= 100
            self.fullness -= 20
        else:
            print('В доме бардак, но сил на уборку нет')
            self.eat()

    def move_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def get_cat(self, some_cat):
        some_cat.house = self.house
        print('{} Взял домой кота'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 140:
            self.zoo_shopping()
        elif self.house.dirt > 100:
            self.clean()
        elif dice == 1:
            self.eat()
            print('Да и вообще можно побездельничать')
        else:
            self.gaming()


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 0
        self.money = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьего корма {}, денег осталось {}, беспорядок на {} баллов'.format(
            self.food, self.cat_food, self.money, self.dirt)


some_dude = Man(name='Вася')
sweet_home = House()
some_dude.move_to_the_house(house=sweet_home)

cats = [Cat(cat_name='Коржик'),
        Cat(cat_name='Соня'),
        Cat(cat_name='Ёлка'),
        Cat(cat_name='Бублик'),
        Cat(cat_name='Ромбик'),
        Cat(cat_name='Фантик')]

for cat in cats:
    some_dude.get_cat(some_cat=cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    some_dude.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    print(some_dude)
    for cat in cats:
        print(cat)
    print(sweet_home)

# Таким образом, на зарплату в 150 рублей за смену Вася может прокормить только ШЕСТЕРЫХ КОТОВ
