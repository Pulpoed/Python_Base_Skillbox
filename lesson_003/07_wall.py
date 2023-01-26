# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (700, 700)
for row in range(0, 700, 50):
    for x in range(0, 1500, 100):
        for y in range(0, 1500, 100):
            start_point = sd.get_point(0 + x - row, 0 + row)
            end_point = sd.get_point(100 + y - row, 50 + row)
            if (x - row) < 0 or (y - row) > 700:
                break
            sd.rectangle(left_bottom=start_point, right_top=end_point, color=sd.COLOR_ORANGE, width=1)
sd.pause()
