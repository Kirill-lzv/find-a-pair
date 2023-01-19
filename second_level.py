import pygame
import random
import sys
from settings import fps, size, clock
from cards import calc, clubn, grib, pers, strek, vishn, karta
from third_level import third_l

def second_l():
    screen = pygame.display.set_mode(size)

    num = 6
    coloda = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(coloda)
    PINK = (255, 228, 181)
    pygame.init()

    counter = 16
    RED = 255, 0, 0
    font = pygame.font.SysFont('arial', 45)
    open_cards = []

    for i in range(len(coloda)):
        open_cards.append(True)
    stroka = 4
    ryad = 4
    click = []
    F = True

    while F:
        clock.tick(fps)
        screen.fill(PINK)
        if counter > 0:
            text = font.render("До старта осталось:" + str(counter), True, RED)
            screen.blit(text, (1050, 100))
        elif counter == 0:
            for i in range(len(coloda)):
                open_cards[i] = False
        counter -= 1

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_m, y_m = pygame.mouse.get_pos()
                x_m = (x_m - 20) // 240
                y_m = y_m // 276
                card = y_m * stroka + x_m
                open_cards[card] = True
                click.append(card)
            if event.type is pygame.QUIT:
                sys.exit(0)
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                third_l()


        for i in range(len(coloda)):
            x = (i % stroka) * 240 + 20
            y = (256 + 20) * (i // ryad)
            if open_cards[i]:
                if coloda[i] == 1:
                    screen.blit(calc, (x, y))
                elif coloda[i] == 2:
                    screen.blit(clubn, (x, y))
                elif coloda[i] == 3:
                    screen.blit(grib, (x, y))
                elif coloda[i] == 4:
                    screen.blit(pers, (x, y))
                elif coloda[i] == 5:
                    screen.blit(strek, (x, y))
                elif coloda[i] == 6:
                    screen.blit(vishn, (x, y))
            else:
                screen.blit(karta, (x, y))
        if len(coloda) == 0:
            text2 = font.render("Молодец!", True, RED)
            screen.blit(text2, (1050, 100))
            F = False
            break

        pygame.display.flip()
        if len(click) == 2:
            if coloda[click[0]] == coloda[click[1]]:
                # pygame.time.delay (3000)
                coloda[click[0]] = 0
                coloda[click[1]] = 0

            else:
                open_cards[click[0]] = False
                open_cards[click[1]] = False
            click.clear()
