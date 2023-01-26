import simple_draw as sd

# sd.resolution = (100, 200)


def draw_wall(x_left_bottom,
              y_left_bottom,
              x_right_top,
              y_right_top):
    sd.rectangle(left_bottom=sd.get_point(x_left_bottom, y_left_bottom),
                 right_top=sd.get_point(x_right_top, y_right_top),
                 color=sd.COLOR_ORANGE,
                 width=1)
    for row in range(y_left_bottom, y_right_top, 50):
        for x in range(0, 1500, 100):
            for y in range(0, 1500, 100):
                start_point = sd.get_point(x_left_bottom + x - row, 0 + row)
                end_point = sd.get_point(100 + y - row, 50 + row)
                if (x - row) < 0 or (y - row) > x_right_top - 100:
                    break
                sd.rectangle(left_bottom=start_point, right_top=end_point, color=sd.COLOR_ORANGE, width=1)


# draw_wall(x_left_bottom=300,
#           y_left_bottom=200,
#           x_right_top=700,
#           y_right_top=300)
#
# sd.pause()
