from Space_3D import Movment
import math
from Engine_3D import Tools


class Law(Movment.Law):
    pi = math.pi

    def __init__(self, screen, mass=1000, color=(255, 255, 255)):
        super().__init__(screen, mass, color)

    def revolve(self, centre, radius=100, ang_vel=1, dirc_vec=(1, 1, 0)):
        i, j, k = dirc_vec
        x, y, z = Tools.dir_cosine(i, j, k)
        self.Displace(centre[0] + radius*y, centre[1] - radius*x, centre[2])
        d_x = self.pos_x - centre[0]
        d_y = self.pos_y - centre[1]
        d_z = self.pos_z - centre[2]
        a, b, c = Tools.dir_cosine(d_x, d_y, d_z)
        vel_2 = self.vel_x ** 2 + self.vel_y ** 2 + self.vel_z ** 2
        self.Addvelocity(ang_vel*x, ang_vel*y, ang_vel*z)
        self.Acclerate(-vel_2/radius*a, -vel_2/radius*b, -vel_2/radius*c)
        self.Updparticle()
        self.Drawparticle(0)
