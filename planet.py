import random

def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1
class Planet():
    """
    Класс отображает состояние планеты.
     имеет три параметра гравитацию
    """
    def __init__(self):
        """
        Инициализация
        """
        # Собственное название планеты
        self.name = "Planet name"
        unique_sequence = uniqueid()
        self.id = next(unique_sequence)
        
        # Переменные дефолтного значения параметров для планеты не изменяемый играком параметр. может быть сменен событием или при генерации планеты.
        
        self.defaultparametrs = [0,0,0]
        self.parametrs = [0,0,0]

        # Максимальные и минималные значения для параметров планеты (праверяется внутри класса)
        self.maxminp = [list(range(10,50,5)),list(range(0,2000,200)),list(range(-100,120,20))]
        
        # plaers_visiability позволяет видить игрокам основные характеристики планеты это пригодность и концентрацию рессурсов.
        self.plaers_visiability = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

        # plaers_fullvisibal  позволяет видеть точное количество населения, добытых минералов.
        self.plaers_fullvisibal = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        
        # mumber of player who is owner of planet (1-16) if zero planet is free 
        self.owner = 0
        
        # Количество населения на планете может быть задано лишь когда есть owner (нет четкого ограничения т.к. для каждой рассы будут свои ограничения)
        self.population = 0

        # коофициент концентрации миниралов на планете, а так же коофицент скорости добычи минералов. от 0.1 до 1
        self.mineral_concentration = [random.choice(range(1,10)),random.choice(range(1,10)),random.choice(range(1,10))]
        
        # Максимальное количество минералов для планеты
        self.mineral_reserves = 1_000_000

        self.current_minerals_reserve = [0,0,0]
        
        # При создании планеты задаются ее основные параметры 
        self.create()
 
        # производит генерацию минералов на планете в момент создания. Так же можно использовать при событиях (при параметре -1)
        self.gen_count = 0 # Only for _minerals_generate function
        self._minerals_generate(self.gen_count)
        
        # Переменная содержить  количество добытых минералов
        self.minerals_on_surfice = [0,0,0]
        
        
    def _minerals_generate(self, count):
        """
        Высчитываем количество минералов сиходя из рандома 
        """
        if count < 0:
            self.gen_count = 0
        if count > 0:
            return False
        else:
            self.gen_count += 1
            for i in range(len(self.mineral_concentration)):
                self.current_minerals_reserve[i] = int((self.mineral_concentration[i]/10 * self.mineral_reserves))
        return True

        
    def create(self):
        """
        Создает параметры гравиации температуры и радиации
        """
        for i in range(len(self.defaultparametrs)):
            self.defaultparametrs[i] = random.choice(self.maxminp[i])
        self.parametrs = self.defaultparametrs.copy()
        

    # geters
    def get_parametrs(self, parametr_num):
        if self.owner > 0:
            return self.parametrs[parametr_num]
        else:
            return self.defaultparametrs[parametr_num]

    def get_gravity(self):
        return self.get_parametrs(0)

    def get_radiation(self):
        return self.get_parametrs(1)

    def get_temp(self):
        return self.get_parametrs(2)

    def get_name(self):
        name = self.name
        return name

    def get_visiability(self):
        return self.plaers_visiability

    def get_minerals_info(self):
        return  [self.current_minerals_reserve,self.minerals_on_surfice] 
    
    def get_population(self):
        if self.owner > 0 and self.population !=0 :
            return self.population
        else:
            return 0

    #seters
    def set_parameter(self,parametr_num, parametr_valume):
        '''
        Принимает номер параметра (parametr_num) который нужно изменить и его значение (parametr_valume)
        Проверяет если параметр вышел за диапозон минимума или максимума принимает крайнее допустимое значение.
        или же значение меняется если оно уже допустимое.

        Так же возвращает true или false для понимания удачно ли выполненна комманда.
        '''
        if self.owner > 0:
            tmp_ = self.parametrs[parametr_num] + parametr_valume
            
            if tmp_ > max(self.maxminp[parametr_num]):
                self.parametrs[parametr_num] = max(self.maxminp[parametr_num])
                return True
            elif tmp_ < min(self.maxminp[parametr_num]):
                self.parametrs[parametr_num] = min(self.maxminp[parametr_num])
                return True
            elif tmp_ in self.maxminp[parametr_num]:
                self.parametrs[parametr_num] = tmp_
                return True
            else:
                return False

    def set_name(self,name):
        self.name = name

    def set_id(self,id):
        self.id = id

    def set_visiability(self, visiability=False, player=0):
        self.plaers_visiability[player] = visiability

    def set_owner(self,player=0):   
        if player != 0:
            self.plaers_visiability[player] = True
            self.plaers_fullvisibal[player] = True
        self.owner = player

    def set_population(self, population):
        if self.owner > 0 and self.population >= 0:
            self.population += population

        if self.owner > 0 and self.population <= 0:
            self.owner = 0
            self.population = 0
            return f"owner 0 now population 0 too on {self.name}"
        
        if self.owner == 0 and population > 0:
            return "set owner first (colonize)"

    def set_mine_minerals(self, mine_one_round):
        """
        Расчет добычи минералов, или их использоваение если отрицательное
        return false for every mineral if try to take more then alredy mined
        """
        mineralscheck = [False,False,False]
        for i in range(len(self.minerals_on_surfice)):
            self.minerals_on_surfice[i] += mine_one_round[i]
            self.current_minerals_reserve[i] -= mine_one_round[i]
            if self.minerals_on_surfice[i] < 0:
                self.current_minerals_reserve[i] += mine_one_round[i]
                self.minerals_on_surfice[i] -= mine_one_round[i]
            else:
                mineralscheck[i] = True          
        return mineralscheck


"""
Пример использования
"""
# # def first_test():
#     def test():
#         planet = Planet()
#         planet.set_owner(1)
#         print("Созадим несолько планет.")

#         def print_planet_info(planet):
#             resurs_name = ["Ираниум","Бараниум","Германиум"]
#             print(f"Название плануты {planet.get_name()}, и следующими параметрами.")
#             print(f"Температура: {planet.get_temp()}")
#             print(f"Гравитация: {planet.get_gravity()}")
#             print(f"Уровень радиации: {planet.get_radiation()}")
#             print(f"Видна играку номе 1: {planet.get_visiability()[1]}")
#             print(f"Видна играку номе 2: {planet.get_visiability()[2]}")
#             print("популяция планеты:", planet.get_population())
#             print(f"Концентарция минералов следующия в недрах")
#             for i in range(len(resurs_name)):
#                 print(f"\t{resurs_name[i]}: {planet.get_minerals_info()[0][i]}")
#             print("Добыто минералов: ")
#             for i in range(len(resurs_name)):
#                 print(f"\t{resurs_name[i]}: {planet.get_minerals_info()[1][i]}")
                
#         print_planet_info(planet)
#         print(planet.set_population(100))
#         print(planet.set_parameter(0,10))
#         print_planet_info(planet)
#         planet.set_mine_minerals([0,10,1])
#         print(type(planet))

#         planet.set_mine_minerals([0,10,1])
#         print_planet_info(planet)
#         planet.set_mine_minerals([0,10,1])
#         print_planet_info(planet)
#         planet.set_mine_minerals([0,-40,1])
#         print_planet_info(planet)
#         print(planet.id)
#         print(planet.id)
#     #test()
