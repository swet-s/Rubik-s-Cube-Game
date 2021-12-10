import pygame
from Puzzles_3D import Cube, GameInputs
from Engine_3D.Vector import Vector3 as V3
from Puzzles_3D.Screen import screen

rubik = Cube.Cube(V3(0, 0, 0), 200, 2)
Moves = GameInputs.GameInputs(rubik)


font = pygame.font.Font("freesansbold.ttf", 20)
lasttick = 0

running = True
# Game loop
while running:
    thistick = pygame.time.get_ticks()
    if thistick-lasttick != 0:
        fps = int(1000/(thistick - lasttick))
    else:
        fps = "Very High"
    lasttick = thistick

    screen.fill((0, 0, 0))
    screen.blit(font.render(f'{fps}', True, (155, 155, 00)), (10, 10))

    rubik.draw_cube()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        Moves.check_input(event)
    Moves.Rotate_from_mouse()

pygame.quit()

