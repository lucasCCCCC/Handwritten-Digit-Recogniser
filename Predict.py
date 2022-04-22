import cv2 as cv
from tensorflow.keras.models import load_model
import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400


MODEL = load_model("mnist.model")

'''
PREDICTIONS = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
               6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
'''


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill("white")

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
            pygame.draw.circle(screen, "black", (x, y), 17)


        if event.type == pygame.MOUSEBUTTONDOWN:
            writing = True


        if event.type == pygame.MOUSEBUTTONUP:
            writing = False

            pygame.image.save(screen, "img.png")
            screen.fill("white")

            img = cv.imread("img.png")[:, :, 0]
            img = cv.resize(img, (28, 28))
            img = np.invert(np.array([img]))
            prediction = MODEL.predict(img)
            print(np.argmax(prediction))


    pygame.display.update()

pygame.quit()
quit()
