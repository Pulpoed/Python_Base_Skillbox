# -*- coding: utf-8 -*-
from datetime import datetime
from pprint import pprint


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# _________
class Logger:

    def __init__(self, filename):
        self.parsed = []
        self.filename = filename

    def parse(self):
        log = open(file=self.filename, mode='r')
        for line in log:
            if 'NOK' in line[29:32]:
                line_cut = line[1:17]
                datetime_object = datetime.strptime(line_cut, '%Y-%m-%d %H:%M')
                self.parsed.append(datetime_object)
        log.close()


events = Logger('events.txt')
events.parse()

print(type(events.parsed[0]))

events_sorted = {}

for event in events.parsed:
    event_cut = event.year, event.month, event.day, event.hour, event.minute
    if event_cut in events_sorted:
        events_sorted[event_cut] += 1
    else:
        events_sorted[event_cut] = 1

print(events_sorted.keys())

file_out = 'file_out.txt'
file = open(file_out, mode='w')
for date, qnt in events_sorted.items():
    file_content = str(datetime(date[0],
                                date[1],
                                date[2],
                                date[3],
                                date[4]).isoformat(sep=' ', timespec='minutes')) + ' : ' + str(qnt) + '\n'
    file.write(file_content)
file.close()
# ___________
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
