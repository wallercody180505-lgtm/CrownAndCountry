import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Crown & Country')
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    screen.fill((15, 20, 30))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
    
