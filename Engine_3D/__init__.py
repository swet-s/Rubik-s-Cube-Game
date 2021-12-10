import pygame
from Engine_3D import Tools as T2, Tools3D as T3
from Engine_3D.Vector import Vector3 as V3, Vector2 as V2


class Py3:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.scr_dim = V2(width, height)
        self.screen = self.Canvas()
        # self.pix_arr = pygame.PixelArray(self.Canvas())
        self.mouse = V2(0, 0)

    def Canvas(self):
        return pygame.display.set_mode((self.width, self.height))

    def Mouse(self, hardness=1, sens=30):
        if pygame.mouse.get_pressed()[0] == 1:
            mx, my = pygame.mouse.get_rel()
            if mx < sens and my < sens:
                self.mouse += V2(mx / hardness, my / hardness)

    def To_camera(self, vector3, cam=800):
        vector3.rotate_deg(V3(1, 0, 0), self.mouse.y)
        vector3.rotate_deg(V3(0, 1, 0), self.mouse.x)
        point2 = T3.Displace_z(vector3, cam)
        return self.scr_dim // 2 + point2 * V2(1, -1)

    def Line(self, start_point, end_point, color=(255, 255, 255)):
        s = self.To_camera(start_point)
        e = self.To_camera(end_point)
        pygame.draw.line(self.screen, color, tuple(s), tuple(e))

    def AddPixel(self, point, color=(255, 255, 255)):
        s = self.To_camera(point)
        pygame.draw.line(self.screen, color, tuple(s), tuple(s))

    def Triangle(self, pointlist, width=0, color=(255, 255, 255)):
        a = tuple(self.To_camera(pointlist[0]))
        b = tuple(self.To_camera(pointlist[1]))
        c = tuple(self.To_camera(pointlist[2]))
        pygame.draw.polygon(self.screen, color, (a, b, c), width)

    def Quad(self, color, corners, width=0):
        a = tuple(self.To_camera(corners[0]))
        b = tuple(self.To_camera(corners[1]))
        c = tuple(self.To_camera(corners[2]))
        d = tuple(self.To_camera(corners[3]))
        pygame.draw.polygon(self.screen, color, (a, b, c, d), width)

    def AddGrid(self, depth=0, space=100, color=(100, 100, 0)):
        depth *= space
        for d in range(-depth // 2, depth // 2 + 1, space):
            for h in range(-self.width // 2, self.width // 2 + 1, space):
                self.Line(V3(h, -self.height // 2, d), V3(h, self.height // 2, d), color)
            for w in range(-self.height // 2, self.height // 2 + 1, space):
                self.Line(V3(-self.width // 2, w, d), V3(self.width // 2, w, d), color)

        for w in range(-self.width // 2, self.width // 2 + 1, space):
            for h in range(-self.height // 2, self.height // 2 + 1, space):
                self.Line(V3(w, h, -depth // 2), V3(w, h, depth // 2), color)
