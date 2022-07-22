import pygame

# initialize the pygame
pygame.init()
scr_width = 600
scr_height = 600
time = 0
Centre_X = scr_width / 2
Centre_Y = scr_height / 2
# create the screen
screen = pygame.display.set_mode((scr_width, scr_height))


def get_fps():
    global time
    new_time = pygame.time.get_ticks()
    if new_time - time != 0:
        fps = int(1000 / (new_time - time))
    else:
        fps = "Very High"
    time = new_time
    return fps


def displace_z(point, cam=800):
    dx, dy, dz = point
    if dz < cam:
        pix_x = (dx * cam) / (cam - dz) + Centre_X
        pix_y = (-dy * cam) / (cam - dz) + Centre_Y
    else:
        pix_x = 800
        pix_y = 600
    return round(pix_x), round(pix_y)


def polygon3D(color, corners, width=0):
    PointList2D = []
    for v3 in corners:
        PointList2D.append(displace_z(v3))
    pygame.draw.polygon(screen, color, PointList2D, width)
