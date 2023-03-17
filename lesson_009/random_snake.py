import simple_draw as sd
import random

sd.resolution = (1200, 700)

while True:
    x = random.randint(0, sd.resolution[0])
    y = random.randint(0, sd.resolution[1])
    point = sd.get_point(x, y)
    color = sd.random_color()
    random_angle = random.randint(0, 359)
    while True:
        sd.start_drawing()
        random_angle += random.randint(-90, 90)
        vector = sd.get_vector(start_point=point, angle=random_angle, length=12, width=4)
        vector.draw(color=color)
        point = vector.end_point
        if point.x < 0 or point.y < 0:
            break
        sd.finish_drawing()
        sd.sleep(0.01)
