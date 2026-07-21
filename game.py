import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    pygame.draw.circle(screen, "red", (400, 300), 50)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
