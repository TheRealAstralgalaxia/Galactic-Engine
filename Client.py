import pygame
import sys
import math

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Galactic Engine Build 1 - Q2 2024')


cube_size = 200
cube_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
angle = 0

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)


    angle += 1
    if angle >= 360:
        angle = 0


    rotation_angle = math.radians(angle)
    cos_angle = math.cos(rotation_angle)
    sin_angle = math.sin(rotation_angle)


    vertices = [
        (cube_center[0] + cos_angle * cube_size, cube_center[1] + sin_angle * cube_size),
        (cube_center[0] + cos_angle * cube_size, cube_center[1] + sin_angle * cube_size - cube_size),
        (cube_center[0] + cos_angle * cube_size + cube_size, cube_center[1] + sin_angle * cube_size - cube_size),
        (cube_center[0] + cos_angle * cube_size + cube_size, cube_center[1] + sin_angle * cube_size),
        (cube_center[0], cube_center[1]),
        (cube_center[0], cube_center[1] - cube_size),
        (cube_center[0] + cube_size, cube_center[1] - cube_size),
        (cube_center[0] + cube_size, cube_center[1])
    ]


    pygame.draw.line(screen, WHITE, vertices[0], vertices[1])
    pygame.draw.line(screen, WHITE, vertices[1], vertices[2])
    pygame.draw.line(screen, WHITE, vertices[2], vertices[3])
    pygame.draw.line(screen, WHITE, vertices[3], vertices[0])
    pygame.draw.line(screen, WHITE, vertices[4], vertices[5])
    pygame.draw.line(screen, WHITE, vertices[5], vertices[6])
    pygame.draw.line(screen, WHITE, vertices[6], vertices[7])
    pygame.draw.line(screen, WHITE, vertices[7], vertices[4])
    pygame.draw.line(screen, WHITE, vertices[0], vertices[4])
    pygame.draw.line(screen, WHITE, vertices[1], vertices[5])
    pygame.draw.line(screen, WHITE, vertices[2], vertices[6])
    pygame.draw.line(screen, WHITE, vertices[3], vertices[7])


    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont(None, 30)
    fps_text = font.render("FPS: " + fps, True, WHITE)
    screen.blit(fps_text, (10, 10))


    pygame.display.flip()


    clock.tick(FPS)
