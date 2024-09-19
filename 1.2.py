import pygame
import math

pygame.init()

win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("moving lines")

black = (0, 0, 0)
white = (255, 255, 255)

line1_angle = 0
line2_angle = 0
line_length = 100
center_distance = 200


clock = pygame.time.Clock()

running = True
while running:
    win.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        center_distance += 1
    if keys[pygame.K_DOWN]:
        center_distance -= 1

    line1_x1 = win_width // 2 - center_distance // 2
    line1_y1 = win_height // 2
    line1_x2 = line1_x1 + line_length * math.cos(math.radians(line1_angle))
    line1_y2 = line1_y1 - line_length * math.sin(math.radians(line1_angle))

    line2_x1 = win_width // 2 + center_distance // 2
    line2_y1 = win_height // 2
    line2_x2 = line2_x1 + line_length * math.cos(math.radians(line2_angle))
    line2_y2 = line2_y1 - line_length * math.sin(math.radians(line2_angle))

    pygame.draw.line(win, black, (line1_x1, line1_y1), (line1_x2, line1_y2), 2)
    pygame.draw.line(win, black, (line2_x1, line2_y1), (line2_x2, line2_y2), 2)

    line1_angle += 1
    line2_angle += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()