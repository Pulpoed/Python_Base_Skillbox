# -*- coding: utf-8 -*-
import zipfile as zf_module
from pprint import pprint


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности.
# Делать сразу на классах.

# cp1251
class Lists:

    def __init__(self, filename, encoding):
        self.filename = filename
        self.encoding = encoding
        self.stats = {}
        self.count_list = []
        self.char_list = []
        self.char_total = 0

    def make_lists(self):
        with open(self.filename, mode='r', encoding=self.encoding) as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stats:
                            self.stats[char] += 1
                        else:
                            self.stats[char] = 1
                        self.char_total += 1
                    else:
                        pass

        for char, count in self.stats.items():
            self.count_list.append(count)
            self.char_list.append(char)


# форматирование


count_char = Lists(filename='voyna-i-mir.txt', encoding='cp1251')
count_char.make_lists()

column_width = 15

print(f'+{"+" :-^{column_width * 2 + 2}}+')
print(f'|{"Буква":^{column_width}}|',
      f'{"Частота":^{column_width}}|')
print(f'+{"+" :-^{column_width * 2 + 2}}+')

char_ascend = sorted(count_char.stats.keys())
char_decsend = sorted(count_char.stats.keys(), reverse=True)
count_ascend = sorted(count_char.stats.values())
count_decsend = sorted(count_char.stats.values(), reverse=True)

for char in char_ascend:
    print(f'|{char:^{column_width}}|',
          f'{count_char.stats.get(char):^{column_width}}|')


print(f'+{"+" :-^{column_width * 2 + 2}}+')
print(f'|{"Итого":^{column_width}}|',
      f'{count_char.char_total:^{column_width}}|')
print(f'+{"+" :-^{column_width * 2 + 2}}+')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
