import pygame
from settings import size


screen = pygame.display.set_mode(size)
# first
pygame.display.set_caption("ИГРА")
liza = pygame.image.load("images/лиза.png").convert_alpha()
liza = pygame.transform.scale(liza, (215, 256))
baby = pygame.image.load("images/малыш.png").convert_alpha()
baby = pygame.transform.scale(baby, (215, 256))
friend = pygame.image.load("images/дружок.png").convert_alpha()
friend = pygame.transform.scale(friend, (215, 256))
gena = pygame.image.load("images/гена.png").convert_alpha()
gena = pygame.transform.scale(gena, (215, 256))
compot = pygame.image.load("images/компот.png").convert_alpha()
compot = pygame.transform.scale(compot, (215, 256))
roza = pygame.image.load("images/роза.png").convert_alpha()
roza = pygame.transform.scale(roza, (215, 256))
karta = pygame.image.load("images/карта1.png").convert_alpha()
karta = pygame.transform.scale(karta, (215, 256))

# second
calc = pygame.image.load("images/calc.png").convert_alpha()
calc = pygame.transform.scale(calc, (215, 256))
clubn = pygame.image.load("images/clubn.png").convert_alpha()
clubn = pygame.transform.scale(clubn, (215, 256))
grib = pygame.image.load("images/grib.png").convert_alpha()
grib = pygame.transform.scale(grib, (215, 256))
pers = pygame.image.load("images/pers.png").convert_alpha()
pers = pygame.transform.scale(pers, (215, 256))
strek = pygame.image.load("images/strek.png").convert_alpha()
strek = pygame.transform.scale(strek, (215, 256))
vishn = pygame.image.load("images/vishn.png").convert_alpha()
vishn = pygame.transform.scale(vishn, (215, 256))

# third
earth = pygame.image.load("images/earth.png").convert_alpha()
earth = pygame.transform.scale(earth, (215, 256))
ball = pygame.image.load("images/ball.png").convert_alpha()
ball = pygame.transform.scale(ball, (215, 256))
pizza = pygame.image.load("images/pizza.png").convert_alpha()
pizza = pygame.transform.scale(pizza, (215, 256))
conus = pygame.image.load("images/conus.png").convert_alpha()
conus = pygame.transform.scale(conus, (215, 256))
piramida = pygame.image.load("images/piramida.png").convert_alpha()
piramida = pygame.transform.scale(piramida, (215, 256))
cookie = pygame.image.load("images/cookie.png").convert_alpha()
cookie = pygame.transform.scale(cookie, (215, 256))