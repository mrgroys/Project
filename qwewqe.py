import pygame
import sys
import time
from random import randint

pygame.init()
size = width, height = (600, 600)
screen = pygame.display.set_mode(size)
fon1 = pygame.image.load('fon1.png')
new = pygame.transform.scale(fon1, (600, 600))
fon2 = pygame.image.load('fon2.png')
new2 = pygame.transform.scale(fon2, (600, 600))
screen.blit(new, (0, 0))
blocks = 3
n = 0
k2 = 0
apple = 0
clock = pygame.time.Clock()


def start():
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render('(для начала игры нажмите пробел)', True, (0, 0, 0))
    screen.blit(text, (130, 300))
    pygame.display.update()


start()

start_game = False
while start_game is False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.blit(new2, (0, 0))
                pygame.display.update()
                start_game = True

d = [(300, 420, 20, 20), (300, 440, 20, 20)]
k = 0

x_apple = randint(40, 460)
y_apple = randint(80, 460)
while y_apple % 20 != 0:
    y_apple = randint(80, 460)
while x_apple % 20 != 0:
    x_apple = randint(40, 460)

x = 0
y = -20
x2 = 300
y2 = 440
last = ''
last_K = 'UP'

game = True
while game is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == ord('d') or event.key == ord('D')) and last_K != 'LEFT':
                x = 20
                y = 0
                n += 1
                last_K = 'RIGHT'
            elif (event.key == pygame.K_LEFT or event.key == ord('a') or event.key == ord('A')) and last_K != 'RIGHT':
                x = -20
                y = 0
                n += 1
                last_K = 'LEFT'
            elif (event.key == pygame.K_UP or event.key == ord('w') or event.key == ord('W')) and last_K != 'DOWN':
                x = 0
                y = -20
                n += 1
                last_K = 'UP'
            elif (event.key == pygame.K_DOWN or event.key == ord('s') or event.key == ord('S')) and last_K != 'UP':
                x = 0
                y = 20
                n += 1
                last_K = 'DOWN'
    screen.blit(new2, (0, 0))
    font2 = pygame.font.Font(pygame.font.get_default_font(), 30)
    text1 = font2.render(f'Apples: {apple}', True, (0, 0, 0))
    screen.blit(text1, (230, 30))
    x4 = x2
    y4 = y2
    x2 += x
    y2 += y
    g2 = (x2, y2, 20, 20)

    for i in d[1:]:
        if g2[0] == i[0] and g2[1] == i[1]:
            game = False

    if x_apple == x2 and y_apple == y2:
        x_apple = randint(40, 460)
        y_apple = randint(80, 460)
        while y_apple % 20 != 0:
            y_apple = randint(80, 460)
        while x_apple % 20 != 0:
            x_apple = randint(40, 460)
        pygame.draw.rect(screen, 'red', [x_apple, y_apple, 20, 20])
        k2 += 1
        apple += 1
    else:
        pygame.draw.rect(screen, 'red', [x_apple, y_apple, 20, 20])

    if x2 >= 600:
        x2 = 0
    elif x2 <= -10:
        x2 = 600
    elif y2 >= 600:
        y2 = 0
    elif y2 <= -10:
        y2 = 600
    for i in range(0, blocks):
        if i == 0:
            pygame.draw.rect(screen, 'gold', [x2, y2, 20, 20])
            g = (x4, y4, 20, 20)
            d.insert(0, g)
            del d[-1]
            if k2 == 1:
                blocks += 1
                d.append(last)
        else:
            pygame.draw.rect(screen, 'yellow', d[k])
            if d[k] == d[-1]:
                last = d[k]
            k += 1
    pygame.display.update()
    clock.tick(3)
    k = 0
    k2 = 0

font3 = pygame.font.Font(pygame.font.get_default_font(), 39)
text3 = font3.render('Game over', True, (0, 0, 0))
screen.blit(text3, (190, 200))
pygame.display.update()
time.sleep(4)
pygame.quit()
sys.exit()
