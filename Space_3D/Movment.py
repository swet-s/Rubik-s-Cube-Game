from Engine_3D import Tools3D as T3, Tools
from Engine_3D.Vector import Vector3 as V3


class Law:
    def __init__(self, canvas, mass, color):
        self.pos = V3(0, 0, 0)
        self.vel = V3(0, 0, 0)
        self.frame = 0
        self.mass = mass
        self.color = color
        self.canvas = canvas

    def Displace(self, vec=V3(0, 0, 0)):
        if self.frame == 0:
            self.pos += vec

    def Addvelocity(self, vec=V3(0, 0, 0)):
        if self.frame == 0:
            self.vel += vec

    def Acclerate(self, vec=V3(0, 0, 0)):
        self.vel += vec

    def AddForce(self, vec=V3(0, 0, 0)):
        if self.mass == 0:
            pass
        else:
            self.vel += vec / self.mass

    def Kin_energy(self):
        return 0.5 * self.mass * (self.vel.mang() ** 2)

    def Updparticle(self):
        self.pos += self.vel
        self.frame += 1

    def Drawparticle(self, size=2):
        rx, ry, rz = self.pos
        for i in range(-size, size + 1):
            for j in range(-size, size + 1):
                for k in range(-size, size + 1):
                    if i == j == 0:
                        index = 1
                    elif abs(i) == abs(j) == size:
                        index = 0.3
                    else:
                        index = 0.8
                    self.canvas.AddPixel(V3(rx + i, ry + j, rz + k), tuple(V3(*self.color) * index))
