import pygame

# initialize the pygame
pygame.init()
scr_width = 600
scr_height = 600
Centre_X = scr_width / 2
Centre_Y = scr_height / 2
# create the screen
screen = pygame.display.set_mode((scr_width, scr_height))


def Displace_z(point, cam=800):
    dx, dy, dz = point
    if dz < cam:
        pix_X = (dx * cam) / (cam - dz) + Centre_X
        pix_Y = (-dy * cam) / (cam - dz) + Centre_Y
    else:
        pix_X = 800
        pix_Y = 600
    return round(pix_X), round(pix_Y)


def polygon3D(color, corners, width=0):
    PointList2D = []
    for v3 in corners:
        PointList2D.append(Displace_z(v3))
    pygame.draw.polygon(screen, color, PointList2D, width)
