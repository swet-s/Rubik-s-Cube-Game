from Puzzles_3D.Cubie import Cubie
from Engine_3D.Vector import Vector3 as V3


class Cube:
    def __init__(self, cube_centre, side_len, dim=2):
        self.face_centre = self.Centres()
        self.cube_centre = cube_centre
        self.side_len = side_len
        self.dim = int(dim)
        self.cubie_index = []
        self.cubies = self.cube_cubies()
        if self.dim > 2:
            self.no_cubies = pow(self.dim, 3) - pow(self.dim - 2, 3)
        else:
            self.no_cubies = pow(self.dim, 3)

    class Centres:
        def __init__(self):
            self.r = self.Centre(V3(1, 0, 0), False)
            self.u = self.Centre(V3(0, 1, 0), False)
            self.f = self.Centre(V3(0, 0, 1), False)
            self.l = self.Centre(V3(-1, 0, 0), False)
            self.d = self.Centre(V3(0, -1, 0), False)
            self.b = self.Centre(V3(0, 0, -1), False)

        def rotate_centres(self, axis, angle):
            self.r.rotate_cen(axis, angle)
            self.u.rotate_cen(axis, angle)
            self.f.rotate_cen(axis, angle)
            self.l.rotate_cen(axis, angle)
            self.d.rotate_cen(axis, angle)
            self.b.rotate_cen(axis, angle)

        def select_all(self, state):
            self.r.selected = state
            self.u.selected = state
            self.f.selected = state
            self.l.selected = state
            self.d.selected = state
            self.b.selected = state

        class Centre:
            def __init__(self, vector, is_selected=False):
                self.vector = vector
                self.selected = is_selected

            def rotate_cen(self, axis, angle):
                self.vector.rotate_deg(axis, angle)

    def index(self):
        rang = range(1 - self.dim, self.dim, 2)
        for i in rang:
            for j in rang:
                for k in rang:
                    self.cubie_index.append(V3(i, j, k))

    def cube_cubies(self):
        d = self.dim - 1
        cubie = []
        self.index()
        for i in range(0, pow(self.dim, 3)):
            if abs(self.cubie_index[i].x) == d or abs(self.cubie_index[i].y) == d or abs(self.cubie_index[i].z) == d:
                cubie.append(Cubie(self.cube_centre, self.side_len / self.dim, self.cubie_index[i]))
        return cubie

    def rotate_cube(self, axis, angle):
        for i in range(0, self.no_cubies):
            self.cubies[i].rotate_cubie(axis, angle)

    def sort_cubies(self):
        prior = []
        for i in range(0, self.no_cubies):
            for j in range(i, self.no_cubies):
                if self.cubies[i].cubie_centre.z > self.cubies[j].cubie_centre.z:
                    temp = self.cubies[i]
                    self.cubies[i] = self.cubies[j]
                    self.cubies[j] = temp
                # if abs(self.cubies[i].cubie_centre.y) < abs(self.cubies[j].cubie_centre.y) \
                #         or abs(self.cubies[i].cubie_centre.x) < abs(self.cubies[j].cubie_centre.x):
                #     temp = self.cubies[i]
                #     self.cubies[i] = self.cubies[j]
                #     self.cubies[j] = temp
            prior.append(self.cubies[i])
        return prior

    def draw_cube(self):
        prior = self.sort_cubies()

        for i in range(0, self.no_cubies):
            prior[i].draw_cubie()
