'''
Модуль механики "Processing/Core" -- К этому модулю будут обращаться все остальные модули.
для расчета игровых событий и взаимодействия объектов всех процессов которые должны происходить на уровне вычислений для игры( движений флота, появления ресурсов, постройки кораблей, изменение статуса исследований, объединение объектов под одинм игроком владельцем т.д.)
Я разделил Processing/Core по названиям. Так как игроку все равно нужно будте взаимодействовать с ядром и перед передачей своего хода и после.
'''
import sys
import os
import random

# Processing Тут будет основная колькуляция ходов, движений корабля, уровень скрытности, маршруты игрока,
# задачи по планетам, и запланированных действий игрока
# Внутреигровых событий сообщений между играками, отображение всех события. отчеты о битвах и т.д
# ВОзможно даже механика битвы тоже тут будет
# Как и Core тесно взаимодействует с другими модулями

def chat():
    pass

def messages():
    pass

def own_events():
    pass

def global_events():
    pass

def battle_events():
    pass

def Planet_status():
    pass
def Cloaking():
    pass

def get_Production_task():
    pass

def set_Production_task():
    pass

def remove_Production_task():
    pass

def build_way():
    pass

def change_way():
    pass

def waypoint_task():
    pass

def get_fleet_items():
    pass


def get_planetary_items():
    pass

def get_fleets():
    pass

def get_groups():
    pass

def show_groups():
    pass


def get_planets():
    pass
##########

def set_fleet_items():
    pass

def set_planetary_items():
    pass

def add_fleet():
    pass

def destroy_fleet():
    pass

def group_fleet():
    pass

def diplomathy():
    pass

def mining_minerals():
    pass

def produce_resurses():
    pass

def scaner_recheck():
    pass

def research_result():
    pass

def trader():
    pass
