import sys
import math

# Save the Planet.
# Use less Fossil Fuel.
surface = []
n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append((land_x, land_y))

global start_flat_land

global end_flat_land
step = 0


def find_flat_ground():
    global surface
    global start_flat_land
    global end_flat_land
    x = iter(surface)
    # print(x)
    for _ in range(len(surface)):
        k, v = next(x)
        k1, v1 = next(x)

        if v == v1:
            start_flat_land = (k, v)
            end_flat_land = (k1, v1)
            break


def easy_onthe_right(vs) -> tuple:
    global step
    lst = [(-15, 1), (-30, 2), (-45, 3), (-60, 4), (-75, 4), (-90, 4), (-90, 3), (-75, 3), (-60, 2), (-15, 1), (0, 2),
           (0, 3), (0, 4)]
    if step < len(lst):
        return lst[step]
    else:
        if vs < -10:
            return (0, 4)
        else:
            return (0, 2)


def correction_left(hs, vs) -> tuple:
    if 4 < hs > 0:
        return (45, 4)
    else:
        return (0, 3)


find_flat_ground()

# game loop
while True:

    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if x < start_flat_land[0] - 500:
        r, p = easy_onthe_right(vs)


    elif x >= start_flat_land[0] and step > 90:
        r, p = correction_left(hs, vs)
    #         r = 0
    #         r=4

    # elif x > end_flat_land[0]:
    #     r = 60
    #     p = 4
    # else:
    #     if -40 < hs < 0:
    #         r = -45
    #         p = 4
    #     if 40 > hs > 0:
    #         r = 45
    #         p = 4
    #     else:
    #         r = 0
    if y < start_flat_land[1] + 100:
        p = 4
        r = 0
    # if y < start_flat_land[1] + 50:
    #     p = 4
    #     r  = 0
    # R P. R is the desired rotation angle. P is the desired thrust power.
    step += 1
    print(r, p)
