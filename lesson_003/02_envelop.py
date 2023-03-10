# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
paper_x, paper_y = 9, 8
paper_x, paper_y = 6, 8
paper_x, paper_y = 8, 6
paper_x, paper_y = 3, 4
paper_x, paper_y = 11, 9
paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код
print("Конверт:")
# если бумага лежит в книжной ориентации, поворачиваем ее в альбомную через служебную переменную paper_z
if paper_x < paper_y:
    paper_z = paper_x
    paper_x = paper_y
    paper_y = paper_z

if paper_x <= envelop_x:
    if paper_y <= envelop_y:
        print("бумага поместилась")
    else:
        print("бумага не поместилась")
else:
    print("бумага не поместилась")

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

print("Кирпичи:")
hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
brick_x, brick_y, brick_z = 11, 2, 10
brick_x, brick_y, brick_z = 10, 11, 2
brick_x, brick_y, brick_z = 10, 2, 11
brick_x, brick_y, brick_z = 2, 10, 11
brick_x, brick_y, brick_z = 2, 11, 10
brick_x, brick_y, brick_z = 3, 5, 6
brick_x, brick_y, brick_z = 3, 6, 5
brick_x, brick_y, brick_z = 6, 3, 5
brick_x, brick_y, brick_z = 6, 5, 3
brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

# длина самой длинной грани кирпича не имеет значения, поэтому сортируем грани по длине
# и переназначаем переменные по двум самым коротким граням
brick_list = [brick_x, brick_y, brick_z]
brick_x1 = sorted(brick_list)[0]
brick_y1 = sorted(brick_list)[1]

# потом решаем задачу так же как с листом бумаги в конверте
if brick_x1 < brick_y1:
    brick_z1 = brick_x1
    brick_x1 = brick_y1
    brick_y1 = brick_z1

if brick_x1 <= hole_x:
    if brick_y1 <= hole_y:
        print("кирпич поместился")
    else:
        print("кирпич не поместился")
else:
    print("кирпич не поместился")
