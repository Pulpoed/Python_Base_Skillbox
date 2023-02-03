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
class RawDict:

    def __init__(self, filename, encoding):
        self.filename = filename
        self.encoding = encoding
        self.stats_chars_qnt = {}
        self.stats_qnt_chars = {}
        self.char_total = 0

    def make_dicts(self):
        with open(self.filename, mode='r', encoding=self.encoding) as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char.lower() in self.stats_chars_qnt:
                            self.stats_chars_qnt[char.lower()] += 1
                        else:
                            self.stats_chars_qnt[char.lower()] = 1
                        self.char_total += 1

        for k, v in self.stats_chars_qnt.items():  # отзеркалил словарь
            self.stats_qnt_chars[v] = k


class DictSorting(RawDict):

    def __init__(self, filename, encoding):
        super().__init__(filename, encoding)
        self.make_dicts()
        self.list_by_sorting_criteria = []
        self.sorted_dict = {}

    def sorting(self):
        method = int(input("1: символы по возрастанию,\n"
                           "2: символы по убыванию,\n"
                           "3: количество по возрастанию,\n"
                           "4: количество по убиванию\n"))
        if method == 1:
            print("Выбран метод символы по возрастанию")
            self.list_by_sorting_criteria = sorted(self.stats_chars_qnt.keys())
            for char in self.list_by_sorting_criteria:
                self.sorted_dict[char] = self.stats_chars_qnt[char]

        elif method == 2:
            print("Выбран метод символы по убыванию")
            self.list_by_sorting_criteria = sorted(self.stats_chars_qnt.keys(), reverse=True)
            for char in self.list_by_sorting_criteria:
                self.sorted_dict[char] = self.stats_chars_qnt[char]

        elif method == 3:
            print("Выбран метод количество по возрастанию")
            self.list_by_sorting_criteria = sorted(self.stats_qnt_chars.keys())
            for qnt in self.list_by_sorting_criteria:
                self.sorted_dict[qnt] = self.stats_qnt_chars[qnt]

        elif method == 4:
            print("Выбран метод количество по убыванию")
            self.list_by_sorting_criteria = sorted(self.stats_qnt_chars.keys(), reverse=True)
            for qnt in self.list_by_sorting_criteria:
                self.sorted_dict[qnt] = self.stats_qnt_chars[qnt]
        else:
            print("Некорректный ввод")
            self.sorting()


class Table:
    def __init__(self, dictionary, column_width, first_col_head, second_col_head):
        self.column_width = column_width
        self.first_col_head = first_col_head
        self.second_col_head = second_col_head
        self.sum = 0
        self.dictionary = dictionary

    def print_table(self):
        print(f'+{"+" :-^{self.column_width * 2 + 2}}+')
        print(f'|{self.first_col_head:^{self.column_width}}|',
              f'{self.second_col_head:^{self.column_width}}|')
        print(f'+{"+" :-^{self.column_width * 2 + 2}}+')

        for line in self.dictionary:
            print(f'|{line:^{self.column_width}}|',
                  f'{self.dictionary.get(line):^{self.column_width}}|')

        print(f'+{"+" :-^{self.column_width * 2 + 2}}+')
        print(f'|{"Итого":^{self.column_width}}|',
              f'{"1488 плейсхолдер":^{self.column_width}}|')
        print(f'+{"+" :-^{self.column_width * 2 + 2}}+')


war_and_peace_stats = DictSorting(filename='voyna-i-mir.txt', encoding='cp1251')
war_and_peace_stats.sorting()

wp_table = Table(war_and_peace_stats.sorted_dict, 15, "символ", "число")
wp_table.print_table()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
