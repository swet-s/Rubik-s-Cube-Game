import pygame
from Engine_3D.Vector import Vector3 as V3


class GameInputs:
    def __init__(self, obj):
        self.obj = obj
        self.centre = obj.face_centre

    def Rotate_from_mouse(self, hardness=1, sens=30):
        if pygame.mouse.get_pressed()[0] == 1:
            mx, my = pygame.mouse.get_rel()
            if mx < sens and my < sens:
                self.obj.rotate_cube(V3(1, 0, 0), my / hardness)
                self.centre.rotate_centres(V3(1, 0, 0), my / hardness)
                self.obj.rotate_cube(V3(0, 1, 0), mx / hardness)
                self.centre.rotate_centres(V3(0, 1, 0), mx / hardness)

    def rotate_face(self, self_centre, angle, limit):
        for i in range(self.obj.no_cubies):
            if self_centre.vector.dot(self.obj.cubies[i].cubie_centre) > limit:
                self.obj.cubies[i].rotate_cubie(self_centre.vector, angle)
            self.obj.cubies[i].select_state = False

    def select_face(self, self_centre, limit):
        self.centre.select_all(False)
        self_centre.selected = True
        for i in range(self.obj.no_cubies):
            if self_centre.vector.dot(self.obj.cubies[i].cubie_centre) > limit:
                self.obj.cubies[i].select_state = True
            else:
                self.obj.cubies[i].select_state = False

    def check_input(self, event):
        if event.type == pygame.KEYDOWN:
            if self.obj.dim == 3:
                limit = self.obj.side_len / (2 * self.obj.dim)
            else:
                limit = 0
            if event.key == pygame.K_r:
                self.select_face(self.centre.r, limit)
            if event.key == pygame.K_u:
                self.select_face(self.centre.u, limit)
            if event.key == pygame.K_f:
                self.select_face(self.centre.f, limit)
            if event.key == pygame.K_l:
                self.select_face(self.centre.l, limit)
            if event.key == pygame.K_d:
                self.select_face(self.centre.d, limit)
            if event.key == pygame.K_b:
                self.select_face(self.centre.b, limit)
            if event.key == pygame.K_UP:
                if self.centre.r.selected:
                    self.rotate_face(self.centre.r, -90, limit)
                if self.centre.u.selected:
                    self.rotate_face(self.centre.u, -90, limit)
                if self.centre.f.selected:
                    self.rotate_face(self.centre.f, -90, limit)
                if self.centre.l.selected:
                    self.rotate_face(self.centre.l, -90, limit)
                if self.centre.d.selected:
                    self.rotate_face(self.centre.d, -90, limit)
                if self.centre.b.selected:
                    self.rotate_face(self.centre.b, -90, limit)
            if event.key == pygame.K_DOWN:
                if self.centre.r.selected:
                    self.rotate_face(self.centre.r, 90, limit)
                if self.centre.u.selected:
                    self.rotate_face(self.centre.u, 90, limit)
                if self.centre.f.selected:
                    self.rotate_face(self.centre.f, 90, limit)
                if self.centre.l.selected:
                    self.rotate_face(self.centre.l, 90, limit)
                if self.centre.d.selected:
                    self.rotate_face(self.centre.d, 90, limit)
                if self.centre.b.selected:
                    self.rotate_face(self.centre.b, 90, limit)
