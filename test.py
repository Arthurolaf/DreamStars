from ship_modules import Base_of_module, WrongModuleType, ModuleFull
from ship_types import Scout, Cruiser, Frigate
from ships_blueprint import Blueprint
from fleets import merge_fleets, Fleet

# Теst the class is below

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

# build fleet
fleet1 = Fleet([Scout(module_list=mod_list),Scout(module_list=mod_list),Scout(module_list=mod_list)])
fleet2 = Fleet([Frigate(mod2_list),Frigate(mod2_list),Frigate(mod2_list)])

big_fleet = merge_fleets(fleet1, fleet2)
print(big_fleet.group_ships_by_type())
print(big_fleet.count_ships_by_type())

for i in big_fleet.ships:
    sum = i.__dict__
    print(sum)

fleet_3 = big_fleet.split_by_ship_type("Scout")


