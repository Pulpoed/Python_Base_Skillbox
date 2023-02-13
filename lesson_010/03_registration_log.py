# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def reg(line):
    """Пытается вписать в три переменные имя, почту и возраст"""
    name, mail, age = line.split(' ')
    age = int(age)
    for char in name:
        if not char.isalpha():
            raise NotNameError('Некорректное имя')
    if not '@' in line or not '.' in line:
        raise NotEmailError('Некорректная почта')
    if not 10 <= age <= 99:
        raise ValueError('Некорректный возраст')
    return name, mail, age


file_raw = 'registrations.txt'
file_out = 'end_clear.txt'
file_errors = 'end_errors.txt'
new_file = open(file_out, mode='w')
new_file_errors = open(file_errors, mode='w')
with open(file_raw, mode='r', encoding='utf8') as file:
    for line in file:
        try:
            new_line = f'{reg(line)[0]} {reg(line)[1]} {reg(line)[2]}\n'
            new_file.write(new_line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                new_file_errors.write(f'Недостаточно полей {exc} в строке {line}')
            elif 'Некорректный' in exc.args[0]:
                new_file_errors.write(f'{exc} в строке {line}')
            else:
                new_file_errors.write(f'{exc} в строке {line}')
        except NotNameError as exc:
            new_file_errors.write(f'{exc} в строке {line}')
        except NotEmailError as exc:
            new_file_errors.write(f'{exc} в строке {line}')

new_file.close()
new_file_errors.close()