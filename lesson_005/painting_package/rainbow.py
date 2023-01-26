import simple_draw as sd


def draw_rainbow(x, y, radius):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step_1 = 0
    sd.sleep(2)
    for color in rainbow_colors:
        sd.circle(center_position=sd.get_point(x, y), radius=radius + step_1, color=color, width=5)
        step_1 += 5
