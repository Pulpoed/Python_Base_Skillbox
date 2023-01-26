import simple_draw as sd

sd.resolution = (1200, 600)

lines = {}
lines_qnt = 50

for i in range(lines_qnt):
    lines[i] = {'s_x': sd.random_number(0, sd.resolution[0]),
                's_y': sd.random_number(0, sd.resolution[1]),
                'e_x': sd.random_number(0, sd.resolution[0]),
                'e_y': sd.random_number(0, sd.resolution[1])}


while True:
    sd.start_drawing()
    for line_num, line_coord in lines.items():
        start_point = sd.get_point(line_coord['s_x'], line_coord['s_y'])
        end_point = sd.get_point(line_coord['e_x'], line_coord['e_y'])
        sd.line(start_point=start_point, end_point=end_point, color=sd.background_color)

        line_coord['s_y'] -= sd.random_number(0, 2)
        line_coord['e_y'] -= sd.random_number(0, 2)

        next_s_point = sd.get_point(line_coord['s_x'], line_coord['s_y'])
        next_e_point = sd.get_point(line_coord['e_x'], line_coord['e_y'])

        sd.line(start_point=next_s_point, end_point=next_e_point)
        if line_coord['s_y'] < 0:
            line_coord['s_y'] += sd.resolution[1]
        if line_coord['e_y'] < 0:
            line_coord['e_y'] += sd.resolution[1]
    sd.finish_drawing()
    sd.sleep(0.01)

    if sd.user_want_exit():
        break

sd.pause()
