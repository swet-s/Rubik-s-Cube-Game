from Engine_3D.Vector import Vector3 as V3
from Puzzles_3D.Screen import polygon3D


class Cubie:
    def __init__(self, cubie_centre, side_len, pos_index=V3(0, 0, 0)):
        self.cubie_centre = V3(*(cubie_centre + pos_index * side_len * 0.5))
        self.side_len = side_len
        self.pos_index = pos_index
        self.select_state = False
        self.faces = self.cubie_faces()

    def cubie_faces(self):
        h = self.side_len * 0.5
        u = Squares(self.cubie_centre + V3(0, h, 0), "Up", self.side_len, (255, 255, 255))
        d = Squares(self.cubie_centre + V3(0, -h, 0), "Down", self.side_len, (255, 255, 0))
        r = Squares(self.cubie_centre + V3(h, 0, 0), "Right", self.side_len, (255, 0, 0))
        l = Squares(self.cubie_centre + V3(-h, 0, 0), "Left", self.side_len, (255, 128, 0))
        f = Squares(self.cubie_centre + V3(0, 0, h), "Front", self.side_len, (0, 255, 0))
        b = Squares(self.cubie_centre + V3(0, 0, -h), "Back", self.side_len, (0, 0, 255))
        return [u, d, l, r, f, b]

    def rotate_cubie(self, axis, angle):
        for i in range(0, 6):
            self.faces[i].rotate(axis, angle)
        self.cubie_centre.rotate_deg(axis, angle)

    def sort_faces(self):
        prior = []
        for i in range(0, 6):
            for j in range(i, 6):
                if self.faces[i].centre.z > self.faces[j].centre.z:
                    temp = self.faces[i]
                    self.faces[i] = self.faces[j]
                    self.faces[j] = temp

            prior.append(self.faces[i])
        return prior

    def draw_cubie(self):
        prior = self.sort_faces()
        for i in range(0, 6):
            prior[i].draw_square(self.select_state)


class Squares:
    def __init__(self, centre, face, side_len, color):
        self.centre = centre
        self.color = color
        self.face = face
        self.side_len = side_len
        self.vertices = self.get_vertices()

    def get_vertices(self):
        h = self.side_len * 0.5
        if self.face == "Up" or self.face == "Down":
            face_coor = [V3(-h, 0, -h), V3(-h, 0, h), V3(h, 0, h), V3(h, 0, -h)]
        elif self.face == "Right" or self.face == "Left":
            face_coor = [V3(0, -h, -h), V3(0, -h, h), V3(0, h, h), V3(0, h, -h)]
        else:
            face_coor = [V3(-h, -h, 0), V3(-h, h, 0), V3(h, h, 0), V3(h, -h, 0)]
        vertex = []
        for i in range(0, 4):
            vertex.append(self.centre + face_coor[i])
        return vertex

    def rotate(self, axis, angle):
        for i in range(0, 4):
            self.vertices[i].rotate_deg(axis, angle)
        self.centre.rotate_deg(axis, angle)

    def draw_square(self, selected=False):
        polygon3D(self.color, self.vertices)
        if not selected:
            polygon3D((55, 55, 55), self.vertices, 3)
        else:
            polygon3D((0, 155, 0), self.vertices, 3)
