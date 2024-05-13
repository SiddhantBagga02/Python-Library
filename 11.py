import pygame, math
pygame.init() # Initialize Pygame
WIDTH, HEIGHT = 800, 600
FPS =30
c1 = (0, 0, 0)
c2 = ( 0, 255, 232 )
def calculate_position(a, b, angle):
    x = a * math.cos(angle)
    y = b * math.sin(angle)
    return int(x), int(y)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elliptical Orbit Simulation")
clock = pygame.time.Clock()
semimajor_axis = 200
semiminor_axis = 100
angular_speed = 0.01 # Adjust this value to change the speed of the orbit
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    obj_x, obj_y = calculate_position(semimajor_axis, semiminor_axis, angle)
    screen.fill(c1)
    pygame.draw.ellipse(screen, c2, (WIDTH // 2 - semimajor_axis, HEIGHT // 2 - semiminor_axis,2 * semimajor_axis, 2 * semiminor_axis), 1)
    pygame.draw.circle(screen, c2, (WIDTH // 2 + obj_x, HEIGHT // 2 + obj_y), 10)
    angle += angular_speed
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()