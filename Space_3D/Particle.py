import pygame
import Engine_3D
from Engine_3D import Tools
from Engine_3D.Vector import Vector3 as V3
from Space_3D import Attractor
import random
import numpy

# create the screen
width = 800
height = 500
py3 = Engine_3D.Py3(width, height)

# objects data
obj = []
no_particle = 10
all_par = range(0, no_particle)
for i in all_par:
    obj.append(Attractor.Attractor(py3))

# Game loop
running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    pygame.time.delay(0)
    py3.screen.fill((0, 0, 0))
    for i in all_par:
        obj[i].Displace(V3(random.randint(-400, 400), random.randint(-300, 300), random.randint(-300, 300)))
        obj[i].Addvelocity(V3(random.random(), random.random(), random.random()))
    Attractor.CoM(py3, obj, no_particle)
    Attractor.follow_CoM(py3, obj, no_particle)
    Attractor.intract_all(obj, no_particle)
    Attractor.add_all(obj, no_particle, 1)
    pygame.display.update()
pygame.quit()


