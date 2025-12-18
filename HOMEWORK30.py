#Normal Writing Editon
import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Rectangle and Text Example")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 36)
text = font.render("NAMASKAR", True, BLACK)
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (200, 150, 200, 100))
    screen.blit(text, (220, 170))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()