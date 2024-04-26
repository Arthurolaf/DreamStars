'''
Модуль механики "Processing/Core" -- К этому модулю будут обращаться все остальные модули.
для расчета игровых событий и взаимодействия объектов всех процессов которые должны происходить на уровне вычислений для игры( движений флота, появления ресурсов, постройки кораблей, изменение статуса исследований, объединение объектов под одинм игроком владельцем т.д.)
Я разделил Processing/Core по названиям. Так как игроку все равно нужно будте взаимодействовать с ядром и перед передачей своего хода и после.
'''
import pandas as pd
import random
import logging as lg
import time
import math
from Core.Processing import *

def rendom_planet_name() -> str:
    path_file = "/Users/artur.abaidulov/Projects/DreamStars/data/stars_name.csv"
    file_size = os.path.getsize(path_file)
    with open(path_file, 'rb') as f:
        while True:
            pos = random.randint(0, file_size)
            if not pos:  # the first line is chosen
                return f.readline().decode()  # return str
            f.seek(pos)  # seek to random position
            f.readline()  # skip possibly incomplete line
            line = f.readline()  # read next (full) line
            if line:
                name = line.decode().replace("\n","")
                return name

class GameCore():
    def __init__(self):
        self.start_game()
    #Core будет объединять данные и проверять целостность и состояние данных и общую базу данных всех элементов игры

    # Так же тут обуде обрабатываться состояние хода игроаков, а так же сохраняться и загружаться игры
    # и проверяться подлинность игрока и какие данные можно отдать игроку через Processing
    # Как и Processing Тесно взаимодействует с дургими модулями
        self.df_game_data = pd.DataFrame()
        self.players_list = ["LostMirrage", "Telvar", "Edgarilla"]

    def game_data_save(self):

        pass

    def game_data_load(self):
        self.df_game_data = pd.read_csv("data/template_planetsv3.csv",sep=",")
        #print(self.df_game_data)
        # self.logger = lg.getLogger(f'GameCore game_data_load')
        # self.logger.info(f'{time.asctime()}: dataframe loaded {self.df_game_data}')
        #print(self.df_game_data.info())
        pass

    def merge_data(self):
        #print(self.df_game_data)
        pass


    def start_game(self):
#        self.game_data_load()
     #   self.merge_data()
        pass

    def gen_star_data(self):
        """
        generates a star map returns a dataframe with the coordinates of all the stars.

        The function is written with the expectation that it is used only when creating a new map (I also plan to fix a random_seed to generate identical maps)
        """
        cordinates = {"x": [], "y": [], "r": 6, "name": [], "id":[]}
        counter_id = 0
        new_stars = self.cluster_gen()
        for i in new_stars:
            counter_id += 1
            x = i[0]
            y = i[1]
            r = 6
            stline = rendom_planet_name()

            # r = random.randint(2, 4)
            cordinates["x"].append(x)
            cordinates["y"].append(y)
            cordinates["r"] = r
            cordinates["id"].append("P" + str(counter_id))
            cordinates["name"].append(stline)
        self.df = pd.DataFrame.from_dict(cordinates)
        return self.df
        #print(self.df)


    def cluster_gen(self):
        # размеры звездного полотна
        OUT_SIZE = [1000, 1000]

        # Отвечает за разброс между группами планет (плотность планет)
        SECTOR_SIZE = 100

        # Отвечате за  количество групп планет соотвественно и за количество планет
        #
        SECTOR_NUMBER = [int(OUT_SIZE[0]/100*0.8), int(OUT_SIZE[1]/100*0.8)]

        # размер рисунка планеты
        SECTOR_BLOCK = 25

        # Разброс планет по сектору
        BLOCK_IN_SECTOR = [random.randint(7,10), random.randint(7,10)]

        stars_list = []
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
                    for i in range(len(stars_list)):
                        sqx = (x - stars_list[i][0]) ** 2
                        sqy = (y - stars_list[i][1]) ** 2
                        if math.sqrt(sqx + sqy) < SECTOR_BLOCK:
                            x = random.randrange(x0, x1)
                            y = random.randrange(y0, y1)
                    return x, y

                check = True
                counter = 0
                while counter != 500:
                    x, y = check_radius(x, y)
                    counter += 1

                stars_list.append([x, y])
        return stars_list
NewGame = GameCore()

#NewGame.gen_star_data()
#print(NewGame.df)
#NewGame.game_data_load()
#print(NewGame.df_game_data.columns)

#print(NewGame.df_game_data[["x","y"]])
#NewGame.cluster_gen()


#NewGame.start_game()
