import abc
class Blueprint:
    def __init__(self, ship_type):
        self.ship_type = ship_type
        self.mineral_cost = [0,0,0]
        self.resureses_cost = 0
        self.id = 0
        self.count = 1
        self.health = 0
        self.owner = 0
        self.slots = list()
        self.mass = 0
    def rebuild_modules(self, modules):
        for _module_ in modules:
            self.insert_slot(_module_)    
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
    def ship_info(self):
        return self.__dict__


class Cruiser(Blueprint):
    def __init__(self):
        super().__init__("Cruiser")

class Frigate(Blueprint):
    def __init__(self, module_list):
        super().__init__("Frigate")
        self.mineral_cost = [2,1,1]
        self.id = 2
        self.health = 100
        self.full_tank = 140
        self.mass = 14
        self.resureses_cost = 10
        self.slots = [{"number":0,"engine":1},{"number":1,"weapon":2},{"number":2,"mech":1},{"number":3,"tech":1}, {"number":4, "scaner":1}]
        self.rebuild_modules(modules=module_list)

class Scout(Blueprint):
    def __init__(self, module_list):
        super().__init__("Scout")
        self.mineral_cost = [1,1,0]
        self.id = 1
        self.health = 50
        self.full_tank = 100
        self.mass = 10
        self.resureses_cost = 5
        self.slots = [{"number":0,"engine":1},{"number":1,"any":1}, {"number":2, "scaner":1}]
        self.rebuild_modules(modules=module_list)
    


class Fleet:
    def __init__(self, ships):
        self.ships = ships

    # need to rebuild def for all available attributes
    # def sum_ships_of_same_type(self):
    #     ships_by_type = {}
    #     for ship in self.ships:
    #         if ship.ship_type in ships_by_type:
    #             ships_by_type[ship.ship_type].hp += ship.hp
    #             ships_by_type[ship.ship_type].attack += ship.attack
    #             ships_by_type[ship.ship_type].defense += ship.defense
    #             ships_by_type[ship.ship_type].shield += ship.shield
    #         else:
    #             ships_by_type[ship.ship_type] = ship
    #     return ships_by_type

    def group_ships_by_type(self):
        ships_by_type = {}
        for ship in self.ships:
            if ship.ship_type in ships_by_type:
                ships_by_type[ship.ship_type].append(ship)
            else:
                ships_by_type[ship.ship_type] = [ship]
        return ships_by_type

    def count_ships_by_type(self):
        ships_by_type = self.group_ships_by_type()
        ship_count = {}
        for ship_type, ships in ships_by_type.items():
            ship_count[ship_type] = len(ships)
        return ship_count

    def split_by_ship_type(self, ship_type):
        ships_by_type = self.group_ships_by_type()
        if ship_type not in ships_by_type:
            return []
        else:
            return Fleet( ships_by_type[ship_type])
    
    def split_by_counter(self, counter=1):
        new_fleet = []
        if counter > len(self.ships):
            counter = len(self.ships)

        for count in range(counter):
            new_fleet.append(self.ships[count])
            self.ships.remove(self.ships[count])
        return Fleet( new_fleet)

import random
from ship_modules import Base_of_module

# Simple module attributes 
eng = {"speed":1,"mass":10,"mineral_cost":[2,1,2], "resureses_cost":5}
scn = {"simple_radar_power":1000,"deep_radar_power":0, "mass":2,"mineral_cost":[0,5,2], "resureses_cost":2}
scn2 = {"simple_radar_power":2000,"deep_radar_power":500, "mass":7,"mineral_cost":[10,5,2], "resureses_cost":10}
ftank = {"mass":5,"full_tank":200,"mineral_cost":[2,0,0]}
lsr = {"mass":2, "atack_beam_power":10,"mineral_cost":[12,0,2], "resureses_cost":5, "beam_range":1}

# simple modules
trans_travel = Base_of_module()
trans_travel.add_slot_attributes(eng)
simple_eye = Base_of_module()
simple_eye.add_slot_attributes(scn)
full_tank = Base_of_module()
full_tank.add_slot_attributes(ftank)
good_scan = Base_of_module()
good_scan.add_slot_attributes(scn2)
pure = Base_of_module()
pure.add_slot_attributes(lsr)

# construct module pack need to save by owner
mod_list = [trans_travel.insert(0,"engine"), simple_eye.insert(1,"scaner"),good_scan.insert(2,"scaner")]
mod2_list = [trans_travel.insert(0,"engine"), pure.insert(1,"weapoon"), pure.insert(1,"weapoon"), full_tank.insert(2,"mech")]
# build
fleet1 = Fleet([Scout(module_list=mod_list),Scout(module_list=mod_list),Scout(module_list=mod_list)])
fleet2 = Fleet([Frigate(mod2_list),Frigate(mod2_list),Frigate(mod2_list)])


#print(fleet1.ships,"232--023-481-09385")

def merge_fleets(fleet1, fleet2):
    return Fleet(fleet1.ships + fleet2.ships)

big_fleet = merge_fleets(fleet1, fleet2)
print(big_fleet.group_ships_by_type())
print(big_fleet.count_ships_by_type())

# sum = 0
for i in big_fleet.ships:
    sum = i.__dict__
    print(sum)

## fleet_2 = Fleet()
fleet_3 = big_fleet.split_by_ship_type("Scout")


# fleet_4 = fleet_3.split_by_counter(counter=2)
# print(fleet_4.ships)
