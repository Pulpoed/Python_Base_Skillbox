# -*- coding: utf-8 -*-
import simple_draw as sd

# sd.resolution = (1200, 700)


def draw_tree(x, y, start_branch_length):
    def draw_branch(start, angle, length):
        if length < 5:
            return
        coef_length = sd.random_number(8, 12)
        coef_angle = sd.random_number(6, 14)
        b_init = sd.get_vector(start, angle, length)
        b_init.draw()
        b_next_point = b_init.end_point
        draw_branch(b_next_point, angle + (30 * coef_angle * 0.1), length * 0.7 * coef_length * 0.1)
        draw_branch(b_next_point, angle - (30 * coef_angle * 0.1), length * 0.7 * coef_length * 0.1)
    point = sd.get_point(x, y)
    draw_branch(point, 90, start_branch_length)


# draw_tree(300, 200, 60)
#
# sd.pause()
