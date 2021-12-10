from Space_3D import Movment
from Engine_3D.Vector import Vector3 as V3


class Attractor(Movment.Law):

    def __init__(self, canvas, mass=1000, color=(255, 255, 255)):
        super().__init__(canvas, mass, color)
        self.g = 1

    def sqr_dist(self, other):
        d_vec = other.pos - self.pos
        dist_sqr = d_vec.mang() ** 2
        return dist_sqr

    def rel_dirCos(self, other):
        d_vec = other.pos - self.pos
        cosine = d_vec.identity()
        return cosine

    def intract(self, other):
        dist_sq = self.sqr_dist(other)
        if dist_sq == 0:
            dist_sq = 0.1
        force = self.g * self.mass * other.mass / dist_sq

        # Just to avoid infinite force
        if force > self.mass/10:
            force = self.mass/10
        self.AddForce(self.rel_dirCos(other) * force)


def intract_all(obj, no_particle):
    for i in range(0, no_particle):
        for j in range(0, no_particle):
            if i != j:
                obj[i].intract(obj[j])

    for i in range(0, no_particle):
        obj[i].Updparticle()


def CoM(canvas, obj, no_particle, show_red=True):
    CoG = V3(0, 0, 0)
    tot_mass = 0
    all_par = range(0, no_particle)
    for i in all_par:
        tot_mass += obj[i].mass

    for i in all_par:
        CoG += (obj[i].pos * obj[i].mass)/tot_mass
    if show_red:
        a = (-1, 0, 1)
        for i in a:
            for j in a:
                for k in a:
                    canvas.AddPixel(CoG + V3(i, j, k), (255, 100, 100))

    return CoG


i_cog = V3(0, 0, 0)


def follow_CoM(canvas, obj, no_particle):
    global i_cog
    CoG = CoM(canvas, obj, no_particle, False)
    all_par = range(0, no_particle)
    if obj[0].frame == 0:
        i_cog = CoG
    C_vec = CoG - i_cog
    for i in all_par:
        obj[i].pos -= C_vec


last_x, last_y, last_z = (0, 0, 0)


# def trace_path(obj, no_particle):
#     global last_x, last_y, last_z
#     all_par = range(0, no_particle)
#
#     for i in all_par:
#         # if Movment.Law.frame == 0:
#         last_x, last_y, last_z = obj[i].pos_x, obj[i].pos_y, obj[i].pos_z
#
#     for i in all_par:
#         obj[i].pos_x -= last_x
#         obj[i].pos_y -= last_y
#         obj[i].pos_z -= last_z


def add_all(obj, no_particle, size=2):
    for i in range(0, no_particle):
        obj[i].Drawparticle(size)
