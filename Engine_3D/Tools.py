import math
from math import *


def direction(iposX, iposY):
    if iposX == 0:
        if iposY >= 0:
            return math.pi / 2
        else:
            return 3 * math.pi / 2
    elif iposX < 0:
        return math.pi + math.atan(iposY / iposX)
    else:
        return math.atan(iposY / iposX)


def mangnitude(x=0, y=0, z=0):
    mang = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    return mang


def dir_cosine(x=0, y=0, z=0):
    mang = mangnitude(x, y, z)
    if mang != 0:
        cos_a = x / mang
        cos_b = y / mang
        cos_c = z / mang
        return cos_a, cos_b, cos_c
    else:
        return 0, 0, 0


def angle(ang):
    x = math.cos(ang)
    y = math.sin(ang)
    return x, y


def rotate(point, centre, ang):
    ang = radians(ang)
    cx, cy = centre
    dx = point[0] - cx
    dy = point[1] - cy
    i, j, k = dir_cosine(dx, dy)
    if j != 0:
        theta1 = j / abs(j) * acos(i)
    else:
        theta1 = acos(i)
    dx, dy = mangnitude(dx, dy) * cos(theta1 + ang), mangnitude(dx, dy) * sin(theta1 + ang)
    return dx + cx, dy + cy


def polar_coor(point, centre=(0, 0, 0)):
    cx, cy, cz = centre
    dx = point[0] - cx
    dy = point[1] - cy
    dz = point[2] - cz
    mang = mangnitude(dx, dy, dz)
    i, j, k = dir_cosine(dx, dy, dz)
    phi = acos(k)
    if abs(k) != 1:
        try:
            theta = (sign_of(j) | 1) * acos(i / sin(phi))
        except ValueError:
            if i / sin(phi) < -1:
                theta = (sign_of(j) | 1) * acos(-1)
            else:
                theta = (sign_of(j) | 1) * acos(1)
    else:
        theta = 0
    return mang, theta, phi


def zero_one(x, wid=38):
    fraction = 1 / math.pi * math.atan(x / wid) + 0.5
    return fraction


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sign_of(x):
    if x == 0:
        return 0
    elif x / abs(x) == 1:
        return 1
    else:
        return -1
