# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)


# месяцы с 31 днем (1 3 5 7 8 10 12)
# месяцы с 30 днями (4 6 9 11)
# IN - поиск элемента в кортеже
tr_one = (1, 3, 5, 7, 8, 10, 12)
tr_zer = (4, 6, 9, 11)
if month in tr_one:
    print("31 день")
elif month in tr_zer:
    print("30 дней")
elif month == 2:
    print("28 дней")
else:
    print("Месяца с таким количеством дней нет")