import pygame
from Puzzles_3D import Cube, GameInputs
from Engine_3D.Vector import Vector3 as V3
from Puzzles_3D.Screen import screen, get_fps

rubik = Cube.Cube(V3(0, 0, 0), 200, 3)
Moves = GameInputs.GameInputs(rubik)

font = pygame.font.Font("freesansbold.ttf", 20)

running = True

# Game loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(font.render(f'{get_fps()}', True, (155, 155, 00)), (10, 10))

    rubik.draw_cube()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        Moves.check_input(event)
    Moves.Rotate_from_mouse()

pygame.quit()
