import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
XS = []
YS = []

PREDICTIONS = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
               6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}


pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.update()
pygame.display.set_caption("Digit recogniser")

running = True
writing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION and writing:
            x, y = event.pos
            pygame.draw.circle(screen, "white", (x, y), 5)

        if event.type == pygame.MOUSEBUTTONDOWN:
            writing = True

        if event.type == pygame.MOUSEBUTTONUP:
            writing = False

    pygame.display.update()

pygame.quit()
quit()