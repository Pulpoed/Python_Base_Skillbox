# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __str__(self):
        return 'Денег {}, еды {}, грязно на {}'.format(self.money, self.food, self.dirt)

    def __init__(self, money, dirt, food):
        self.money = money
        self.dirt = dirt
        self.food = food

    def new_day(self):
        self.dirt += 5


class Human:
    total_food = 0

    def __init__(self, name, fullness=30, happiness=100):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.house = None

    def __str__(self):
        return '{}, сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def move_into_house(self, house):
        self.house = house
        print('{} въехал в дом'.format(self.name))

    def check_life(self):
        if self.fullness <= 0 or self.happiness <= 10:
            return False
        else:
            return True

    def eat(self):
        if self.house.food < 30:
            self.fullness -= 10
            print('{} не хватает еды!'.format(self.name))
            return False
        self.fullness += 30
        self.house.food -= 30
        Human.total_food += 30
        print('{} поел'.format(self.name))
        return True


class Husband(Human):
    capital = 0

    def act(self):
        if self.check_life():
            if self.fullness <= 10:
                self.eat()
            elif self.happiness <= 20:
                self.gaming()
            elif self.house.money <= 400:
                self.work()
            else:
                self.gaming()
            if self.house.dirt >= 90:
                self.happiness -= 10
        else:
            print('{} умер....'.format(self.name))

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        Husband.capital += 150
        print('{} пошел на работу'.format(self.name))

    def gaming(self):
        self.happiness += 5
        self.fullness -= 10
        print('{} поиграл в Танки'.format(self.name))


class Wife(Human):
    fur_coats = 0

    def act(self):
        dice = randint(1, 5)
        if self.check_life():
            if self.fullness <= 10:
                self.eat()
            elif self.happiness <= 20:
                self.buy_fur_coat()
            elif self.house.food <= 60:
                self.shopping()
            elif self.house.dirt >= 90:
                self.clean_house()
            else:
                print('{} занималась саморазвитием'.format(self.name))
                self.fullness -= 10
            if self.house.dirt >= 90:
                self.happiness -= 10
        else:
            print('{} умерла....'.format(self.name))

    def shopping(self):
        if self.house.money >= 50:
            self.fullness -= 10
            self.house.money -= 70
            self.house.food += 70
            print('{} сходила за продуктами'.format(self.name))
        else:
            print('На продукты не хватает денег....'.format(self.name))

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.fullness -= 10
            self.happiness += 60
            self.house.money -= 350
            Wife.fur_coats += 1
            print('{} купила шубу'.format(self.name))
        else:
            print('На шубу не хватает денег....'.format(self.name))

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        print('{} прибралась в доме'.format(self.name))


sweet_home = House(money=100, dirt=0, food=50)
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

serge.move_into_house(sweet_home)
masha.move_into_house(sweet_home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    sweet_home.new_day()
    print(serge)
    print(masha)
    print(sweet_home)
print('Всего куплено шуб', masha.fur_coats)
print('Всего заработано денег', serge.capital)
print('Всего съедено еды', serge.total_food + masha.total_food)


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
