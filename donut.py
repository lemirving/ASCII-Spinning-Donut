import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH = 1920
HEIGHT = 1080

xStart, yStart = 0, 0
xSeparator = 10
ySeparator = 20

rows = HEIGHT // ySeparator
columns = WIDTH // xSeparator
screenSize = rows * columns

xOffset = columns / 2
yOffset = rows / 2

A, B = 0, 0

thetaSpacing = 10
phiSpacing = 1
chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('donut')
font = pygame.font.SysFont('Arial', 14, bold=True)

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(letter, xStart, yStart):
    text = font.render(str(letter), True, hsv_to_rgb(hue, 1, 1))
    display_surface.blit(text, (xStart, yStart))

run = True
while run:

    screen.fill((black))

    z = [0] * screenSize
    b = [' '] * screenSize

    for j in range(0, 628, thetaSpacing):
        for i in range(0, 628, phiSpacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(xOffset + 40 * D * (l * h * m - t * n))
            y = int(yOffset + 20 * D * (l * h * n + t * m))

            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if yStart == rows * ySeparator - ySeparator:
        yStart = 0

    for i in range(len(b)):
        A += 0.000002
        B += 0.000001
        if i == 0 or i % columns:
            text_display(b[i], xStart, yStart)
            xStart += xSeparator
        else:
            yStart += ySeparator
            xStart = 0
            text_display(b[i], xStart, yStart)
            xStart += xSeparator

    pygame.display.update()
    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False