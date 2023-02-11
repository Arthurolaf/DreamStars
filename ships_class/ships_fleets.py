import random
from ship_modules import Base_of_module, ModuleFull, WrongModuleType
import time
import sys
# Here created classe's of Ship

class Ship_Not_ready(Exception):
    pass

def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1

        

class Base_of_any_ship():
    def __init__(self):
        self.name = "base_ship"
        self.mineral_cost = [0,0,0]
        self.resureses_cost = 0
        self.id = 0
        self.count = 1
        self.health = 0
        self.owner = 0
        self.slots = list()
        self.mass = 0

    def insert_slot(self, module):
        def accept():
            for k, v in module.items():
                if k == "mineral_cost":
                    var_list_set = []
                    for i in range(len(self.mineral_cost)):
                        var_list_set.append(module[k][i] + self.mineral_cost[i])
                    self.mineral_cost = var_list_set
                elif k == "module_type":
                    pass
                
                elif k in self.__dict__:
                    v2 = getattr(self, k)
                    setattr(self, k, v + v2)
                else:
                    setattr(self, k, v)
        
        module_keys = []
        for keys in module["module_type"].keys():
            module_keys.append(keys)

        for element in range(len(self.slots)):
            if module["module_type"][module_keys[0]] == element:
                #print(self.slots[element], "slots")
                for k in self.slots[element].keys():
                    ##print(k)
                    
                    if (k != "engine" and k !="number") and "engine" in module["module_type"]:
                        raise WrongModuleType ("Engine need to use in 'Engine' slot")
                    elif k != "number" and k in module["module_type"]:
                        self.slots[element][k] += module["module_type"][k]
                        if self.slots[element][k] > -1:
                            accept()
                        else:
                            raise ModuleFull ("Slot is full, no place for this module")
                    elif k == "any":
                        self.slots[element][k] += module["module_type"][module_keys[1]]
                        if self.slots[element][k] > -1:
                            accept()
                        else:
                            raise ModuleFull ("Slot is full, no place for this module")

    def check_ready(self):
        if self.slots[0]["engine"] == 0:
            return True    
        else:
            raise Ship_Not_ready ("Ship must be with engine")

    def class_info(self):
        return self.__class__.__bases__

    def create_ship(self, fleet, count=1):
        if self.check_ready() is True:
            self.count = count
            fleet.fleet_list.append(self)
            return fleet    
   
    def ship_info(self):
        return self.__dict__
    
    

class Orbital_fort(Base_of_any_ship):
    pass


class Fleet():
    def __init__(self):
        self.fleet_name = "base_ship"
        self.fleet_id = 0
        self.fleet_list = []

    def class_info(self):
        return self.__class__.__bases__

    def merge_old(self, add_fleet):
        """
        Фукнция добавляет в список новый флот или содзает новый
        принимая на себя все атрибуты класса из списка для отображения
        """
        if type(add_fleet) is type(Fleet()):
            new_fleet = Fleet()

            #sys.exit()
            for i in range(len(self.fleet_list)):
                for z in range(len(add_fleet.fleet_list)):
                    if self.fleet_list[i].id == add_fleet.fleet_list[z].id:
                        self.fleet_list[i].count = self.fleet_list[i].count + add_fleet.fleet_list[z].count

                        _tmp_mc_ = []
                        for element in self.fleet_list[i].mineral_cost:
                            _tmp_mc_.append(element * self.fleet_list[i].count)
                        self.fleet_list[i].mineral_cost = _tmp_mc_

                        self.fleet_list[i].resureses_cost *= 2
                        self.fleet_list[i].health *=2
                        self.fleet_list[i].mass *=2
                        self.fleet_list[i].full_tank *=2
                         
                        add_fleet.fleet_list.pop(z)
            self.fleet_list += add_fleet.fleet_list             
            new_fleet.fleet_list = self.fleet_list
            new_fleet.fleet_id = self.fleet_id + add_fleet.fleet_id
            return new_fleet 
 
        elif add_fleet.class_info()[0] is type(Base_of_any_ship()):
 
            self.fleet_list.append(add_fleet)
            
    def merge(self, joined_fleet):

        for fleet_n in range(len(joined_fleet.fleet_list)):
                time.sleep(1)
                print("-")
                print(self.fleet_list)
                print(joined_fleet.fleet_list[fleet_n])
                if self.fleet_list[fleet_n] is joined_fleet.fleet_list[fleet_n]:
                    self.fleet_list[fleet_n].count += 1 
                    return self
                else:
                    print("--")
                    print(self.fleet_list)
                    time.sleep(1)
                    self.fleet_list.append(joined_fleet.fleet_list[fleet_n])
                    print(self.fleet_list)
                    print("---")
                    print(f"fleet id is: {self.fleet_id}",joined_fleet.fleet_list[fleet_n].ship_info())
        return self
    def split():
        '''
        Функция удаляет выбраный флот из списка и создает новый класс
        '''
        pass
    def show_info(self, num=None):
        if num is not None:
            return self.fleet_list[num]
        else:
            print("check")
            for fleet_n in self.fleet_list :
                print(fleet_n)
                print(f"fleet id is: {self.fleet_id}",fleet_n.ship_info())
            
    def battle(self):
        """
        Используется только для битв (пока не факт, что понадобится)
        """
        pass

