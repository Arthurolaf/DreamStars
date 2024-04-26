"""
Использовав функцию из интернета по падающий снег, я ее изменил для получения звездного неба для игры.

Теперь снежинки это звезды, и при нажатии на звезду, мы ее окрашиваем в красный свет

Долго бился над возможностью генерации планет группами и иметь возможность регулировать разброс.

"""

# Импортируем модуль для игр pygame
import pygame
import random
import math, os
from pygame.image import load
from pygame.math import Vector2
import sys


class GameObject():
    def __init__(self, position, sprite, step=0):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = 4
        self.step = Vector2(step)

    def draw(self, front):
        blit_position = self.position - Vector2(self.radius)
        front.blit(self.sprite, blit_position)

    pass


def load_sprit(name, alpha=True):
    path = f"images/{name}"
    loaded_image = load(path)
    if alpha:
        return loaded_image.convert_alpha()
    else:
        return loaded_image.convert()


class Chousen_planet(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprit("simple_planet.png"))


# Инициализируем движок pygame
pygame.init()

# цвета звезд
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

# размеры звездного полотна
OUT_SIZE = [2000, 2000]

# Отвечает за разброс между группами планет
SECTOR_SIZE = 100

# Отвечате за  количество групп планет
# не должно превышать 100 размера галактики
SECTOR_NUMBER = [15, 15]

# размер рисунка планеты
SECTOR_BLOCK = 25

# Разброс планет по сектору
BLOCK_IN_SECTOR = [7, 8]

snow_list = []
for snx in range(0, SECTOR_NUMBER[0]):
    for sny in range(0, SECTOR_NUMBER[1]):
        # print(snx, SECTOR_NUMBER[0])
        planets_count = random.randrange(1, 3)
        # for planets_count in range(1,2):
        # print(planets_count,'-------ad-ds-fadsf-adsf')
        if planets_count == 1:
            x_block = random.randrange(1, 2)
            y_block = random.randrange(1, 2)
        if planets_count == 2:
            x_block = random.randrange(2, 4, 2)
            y_block = random.randrange(2, 4, 2)
        if planets_count == 3:
            x_block = random.randrange(1, 5)
            y_block = random.randrange(1, 5)

        x0 = SECTOR_SIZE // SECTOR_BLOCK + SECTOR_BLOCK + SECTOR_SIZE * snx + SECTOR_BLOCK * x_block
        x1 = x0 + (SECTOR_BLOCK * BLOCK_IN_SECTOR[0] + x_block) // x_block
        # print(x0,x1)
        x = random.randrange(x0, x1)

        y0 = SECTOR_SIZE // SECTOR_BLOCK + SECTOR_BLOCK + SECTOR_SIZE * sny + SECTOR_BLOCK * y_block
        y1 = y0 + (SECTOR_BLOCK * BLOCK_IN_SECTOR[1] + y_block) // y_block

        y = random.randrange(y0, y1)


        def check_radius(x, y):
            z = True
            for i in range(len(snow_list)):
                sqx = (x - snow_list[i][0]) ** 2
                sqy = (y - snow_list[i][1]) ** 2
                if math.sqrt(sqx + sqy) < SECTOR_BLOCK:
                    x = random.randrange(x0, x1)
                    y = random.randrange(y0, y1)
            return x, y


        check = True
        counter = 0
        while counter != 500:
            x, y = check_radius(x, y)
            counter += 1

        snow_list.append([x, y])
print(snow_list)
# sys.exit()
screen = pygame.display.set_mode(OUT_SIZE)
pygame.display.set_caption("Star Animation")

screen.fill(BLACK)


def drow_random_planet(planet):
    """
    Функция рисования планет, пока не идеальна.. Уже рандомно рисует изображения планеты, но в будущем будет правляемо перерисовывать данные.

    Исходя из объектов на карте.

    """
    n = random.randint(0, 4)
    # print(n,planet)
    red_planet = Chousen_planet(position=(planet[0] - 8, planet[1] - 8))
    if n == 0:
        pygame.draw.circle(screen, WHITE, planet, 3)
    elif n == 1:
        red_planet.sprite = load_sprit("of_planet.png")
        red_planet.draw(screen)
    elif n == 2:
        red_planet.sprite = load_sprit("sb_planet.png")
        red_planet.draw(screen)
    elif n == 3:
        red_planet.sprite = load_sprit("sd_planet.png")
        red_planet.draw(screen)
    elif n == 4:
        red_planet.sprite = load_sprit("fleet_planet.png")
        red_planet.draw(screen)


# Рисуем все планеты  на холст исходя из координат
for i in range(len(snow_list)):
    drow_random_planet(snow_list[i])


def check_pos(pos):
    """ функция проверки позици клика мышки (нужно переименовать чтобы было ясно.)
    А лучше выделить ее как отдельнуюф функцию которая отвечат только за пределения клика мышки и поиска объектвов связаных с этим местом, но тут позже

    Пока что эта функция перерисовывания планет я бы сказал так (просто для тригера используется мышка)

    """
    for i in range(len(snow_list)):
        # print(i,pos)

        x = pos[0]
        y = pos[1]

        sqx = (x - snow_list[i][0]) ** 2
        sqy = (y - snow_list[i][1]) ** 2

        if math.sqrt(sqx + sqy) < 4:
            print('inside')

            red_planet = Chousen_planet(position=(snow_list[i][0] - 8, snow_list[i][1] - 8))
            if chousen_one['xy'] != [snow_list[i][0], snow_list[i][1]]:
                red_planet.draw(screen)

                chousen_one['xy'] = snow_list[i]
            else:

                pygame.draw.circle(screen, BLACK, snow_list[i], 12)
                pygame.draw.circle(screen, WHITE, snow_list[i], 3)
                print(pygame.draw.circle(screen, WHITE, snow_list[i], 3))
                chousen_one['xy'] = [999999, 999999]

    else:
        pass
    return snow_list[i]


chousen_one = {'color': WHITE, 'xy': [999999, 999999], 'size': 1}


def move_snow():
    done = False
    while not done:

        for event in pygame.event.get():  # Пользователь сделал что-то
            if event.type == pygame.QUIT:  # Если нажато стоп
                done = True  # выходим из цикла
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # print(pos)
                # if pos in snow_list:
                #    sys.exit()
                check_pos(pos)
            # if event.type == pygame.MOUSEBUTTONDOWN:

            # # снежинка вниз на 1
            # snow_list[i][1] += 1

            # if snow_list[i][1] > 400:
            #     y = random.randrange(-50, -10)
            #     snow_list[i][1] = y
            #     x = random.randrange(0, 400)
            #     snow_list[i][0] = x

        # обновление screen с новыми данными и позициями снежинок
        pygame.display.flip()
    #        clock.tick(20)
    pygame.quit()


move_snow()