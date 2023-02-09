import random
from ship_modules import Base_of_module, ModuleFull, WrongModuleType
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
                print(self.slots[element], "slots")
                for k in self.slots[element].keys():
                    print(k)
                    
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
    #def get_info(self):
     
    def check_ready(self):
        if self.slots[0]["engine"] == 0:
            return True    
        else:
            raise Ship_Not_ready ("Ship must be with engine")

    def create_ship(self):
        if self.check_ready() is True:
            return self.__dict__    
 
    
    

class Orbital_fort(Base_of_any_ship):
    pass


class Fleet():
    pass


def test():
    class Scout(Base_of_any_ship):
        def __init__(self):
            super().__init__()
            self.name = "scout"
            self.mineral_cost = [1,1,0]
            self.id = 1
            self.health = 50
            self.full_tank = 100
            self.mass = 10
            self.resureses_cost = 5
            self.slots = [{"number":0,"engine":1},{"number":1,"any":1}, {"number":2, "scaner":1}]

    scout = Scout()


    engine = {"speed":1,"mass":10,"mineral_cost":[2,1,2], "resureses_cost":5}
    scaner = {"simple_radar_power":1000,"deep_radar_power":0, "mass":2,"mineral_cost":[0,5,2], "resureses_cost":2}
    scaner_2 = {"simple_radar_power":2000,"deep_radar_power":500, "mass":7,"mineral_cost":[10,5,2], "resureses_cost":10}
    full_tanker = {"mass":5,"full_tank":200,"mineral_cost":[2,0,0]}


    trans_travel = Base_of_module()
    trans_travel.add_slot_attributes(engine)
    simple_eye = Base_of_module()
    simple_eye.add_slot_attributes(scaner)
    full_tank = Base_of_module()
    full_tank.add_slot_attributes(full_tanker)
    good_scan = Base_of_module()
    good_scan.add_slot_attributes(scaner_2)


    #print(simple_eye.insert(1,"scaner"))
    scout.insert_slot(trans_travel.insert(0,"engine"))
    scout.insert_slot(simple_eye.insert(1,"scaner"))
    print(scout.create_ship())
    scout.insert_slot(good_scan.insert(2,"scaner"))
    print(scout.create_ship())
