import simple_draw as sd

sd.resolution = (700, 600)


def draw_shape(sp_x, sp_y, angle, length, n_shape):
    v_init = sd.get_vector(start_point=sd.get_point(sp_x, sp_y), angle=angle, length=length, width=3)
    v_init.draw()
    tuple_of_shapes = (angle + 120, angle + 240), \
                      (angle + 90, angle + 180, angle + 270), \
                      (angle + 72, angle + 144, angle + 216, angle + 288), \
                      (angle + 60, angle + 120, angle + 180, angle + 240, angle + 300)
    for next_angle in tuple_of_shapes[n_shape]:
        v_next = sd.get_vector(start_point=v_init.end_point, angle=next_angle, length=length, width=3)
        v_next.draw()
        v_init = v_next


def draw_triangle(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=0)


def draw_rectangle(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=1)


def draw_pentagon(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=2)


def draw_hexagon(sp_x, sp_y, angle, length):
    draw_shape(sp_x=sp_x, sp_y=sp_y, angle=angle, length=length, n_shape=3)


draw_triangle(50, 370, 20, 200)
draw_rectangle(90, 50, 22, 200)
draw_pentagon(500, 320, 20, 130)
draw_hexagon(500, 50, 22, 100)

sd.pause()
