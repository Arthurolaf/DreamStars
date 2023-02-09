from planet import Planet 
from ship_version_1 import Ship, uniqueid, Fleet
import sys
def test():
    planet = Planet()
    planet.set_owner(1)
    print("Созадим несолько планет.")

    def print_planet_info(planet):
        resurs_name = ["Ираниум","Бараниум","Германиум"]
        print(f"Название плануты {planet.get_name()}, и следующими параметрами.")
        print(f"Температура: {planet.get_temp()}")
        print(f"Гравитация: {planet.get_gravity()}")
        print(f"Уровень радиации: {planet.get_radiation()}")
        print(f"Видна играку номе 1: {planet.get_visiability()[1]}")
        print(f"Видна играку номе 2: {planet.get_visiability()[2]}")
        print("популяция планеты:", planet.get_population())
        print(f"Концентарция минералов следующия в недрах")
        for i in range(len(resurs_name)):
            print(f"\t{resurs_name[i]}: {planet.get_minerals_info()[0][i]}")
        print("Добыто минералов: ")
        for i in range(len(resurs_name)):
            print(f"\t{resurs_name[i]}: {planet.get_minerals_info()[1][i]}")
            
    print_planet_info(planet)
    print(planet.set_population(100))
    print(planet.set_parameter(0,10))
    print_planet_info(planet)
    planet.set_mine_minerals([0,10,1])
    print(type(planet))

    planet.set_mine_minerals([0,10,1])
    print_planet_info(planet)
    planet.set_mine_minerals([0,10,1])
    print_planet_info(planet)
    planet.set_mine_minerals([0,-40,1])
    print_planet_info(planet)
    print(planet.id)
    print(planet.id)
#test()
ship_types = {2: "transport",6:"colony",3:"scout",4:"cruser",5:"battle_ship",1:"starbase"}

#cruser = Ship()
cruser = Fleet()

battle_ship = Ship()
unique_sequence = uniqueid()

#print(cruser.get_ship_info())
#print(cruser_fleet.get_ship_info())
#print(battle_ship.get_ship_info())
own_cruser = cruser
#cruser = cruser_fleet

cruser_mineral_cost = [5,10,2]
cruser_resureses_cost = 20
cruser_slot_count = 3
cruser_health = 25
cruser_full_tank = 150
cruser_mass = 40
cruser_ship_type = 4
cruser_owner = 2
cruser_id = next(unique_sequence)
#        [mineral_cost = [0,0,0], resureses_cost = 0, slot_count = 1, health = 0, full_tank = 0, mass = 0, ship_type = 0, id = 0, owner = 0]

bs_mineral_cost = [15,20,4]
bs_resureses_cost = 100
bs_slot_count = 7
bs_health = 120
bs_full_tank = 500
bs_mass = 150
bs_ship_type = 5
bs_owner = 1
bs_id = next(unique_sequence)

cruser.create_ship(cruser_mineral_cost, cruser_resureses_cost, cruser_slot_count, cruser_health, cruser_full_tank, cruser_mass, cruser_ship_type, cruser_id, cruser_owner)    
cruser1 = Fleet()
cruser1.create_ship(cruser_mineral_cost, cruser_resureses_cost, cruser_slot_count, cruser_health, cruser_full_tank, cruser_mass, cruser_ship_type, cruser_id, cruser_owner)    
cruser2 = Fleet()
cruser2.create_ship(cruser_mineral_cost, cruser_resureses_cost, cruser_slot_count, cruser_health, cruser_full_tank, cruser_mass, cruser_ship_type, cruser_id, cruser_owner)    
cruser3 = Fleet()
cruser3.create_ship(cruser_mineral_cost, cruser_resureses_cost, cruser_slot_count, cruser_health, cruser_full_tank, cruser_mass, cruser_ship_type, cruser_id, cruser_owner)    

#cruser_fleet.create_ship(cruser_mineral_cost, cruser_resureses_cost, cruser_slot_count, cruser_health, cruser_full_tank, cruser_mass, cruser_ship_type, cruser_id, cruser_owner)

#cruser_fleet = cruser_fleet + cruser 

battle_ship.create_ship(bs_mineral_cost, bs_resureses_cost, bs_slot_count, bs_health, bs_full_tank, bs_mass, bs_ship_type, bs_id, bs_owner)
#print(cruser_fleet.get_ship_info())
print(cruser.get_ship_info())
print(battle_ship.get_ship_info())
print("======= created ========")
#sys.exit()

class item():
        def __init__(self):
            self.slot_count = -1
            
weapon = item()
armor = item()
shild = item()
engine = item()

weapon.__setattr__("atack_rocket_power", 10)
weapon.__setattr__("item_type", {3:1})

armor.__setattr__("health", 15)
armor.__setattr__("item_type", {2:1})

shild.__setattr__("shild", 7)
shild.__setattr__("item_type", {4:1})

engine.__setattr__("speed", 2)
engine.__setattr__("item_type", {1:1})


cruser.set_item(engine)
cruser.set_item(weapon)
cruser.set_item(armor)

cruser1.set_item(engine)
cruser1.set_item(weapon)
cruser1.set_item(armor)

cruser2.set_item(engine)
cruser2.set_item(weapon)
cruser2.set_item(armor)

cruser3.set_item(engine)
cruser3.set_item(weapon)
cruser3.set_item(armor)


#cruser.set_item(armor)
battle_ship.set_item(engine)
battle_ship.set_item(weapon)
battle_ship.set_item(weapon)
battle_ship.set_item(weapon)
battle_ship.set_item(shild)
battle_ship.set_item(shild)
battle_ship.set_item(shild)

#print()
#cruser_flet()
#
# self.mineral_cost = [1,2,2]
# self.item_type = {0:1}
# self.speed = 3
cruser_fleet = cruser + cruser2 + cruser1 + cruser3
print("cruser_fleet",cruser.id)
print("bs_fleet",battle_ship.id)
print("cruser_fleet",cruser.get_ship_info())
print("bs_fleet",battle_ship.get_ship_info())




def first_battle():
    def end_battle(winer, loser):
        print(f"Победа за {ship_types[winer.ship_type]}")
        print(winer.get_ship_info(), "winer final")
        print(loser.get_ship_info(), "loser final")
        
    def attack(atacker, defender):
        #print(type(atacker))
        if atacker.count > 1:
            one_ship_health_atacker = atacker.health / atacker.count
            one_ship_atack_atacker = atacker.atack_rocket_power / atacker.count
            one_ship_mass_atacker = atacker.mass /  atacker.count
        if defender.count > 1:
            one_ship_health_defender = defender.health / defender.count
            one_ship_atack_defender = defender.atack_rocket_power / defender.count
            one_ship_mass_defender = defender.mass / defender.count
        count = 0
        while True: 
            count += 1
            if atacker.count > 1:
                atacker_power = one_ship_atack_atacker * atacker.count
            else:
                atacker_power = atacker.atack_rocket_power
                    
            if defender.shild > 0:
                if atacker_power > defender.shild and defender.shild != 0:
                    defender.shild = 0
                    atacker_power = atacker_power - defender.shild    
                else:
                    atacker_power = atacker.atack_rocket_power/2   
                    defender.shild -= atacker_power
                    defender.health -= atacker_power
            else:
                defender.health -= atacker_power
            
            if defender.count > 1:
                defender_power = one_ship_atack_defender * defender.count   
            else:
                defender_power = defender.atack_rocket_power
            if defender.health <= 0:
                end_battle(atacker, defender)
                break

            if atacker.shild > 0:
                if defender_power > atacker.shild and atacker.shild != 0:
                    atacker.shild = 0
                    defender_power = defender_power - atacker.shild
                else:
                    defender_power = defender.atack_rocket_power/2   
                    atacker.shild -= defender_power
                    atacker.health -= defender_power
            else:
                atacker.health -= defender_power
            
            if atacker.count > 1:    
                #for i in range(atacker.count):
                if atacker.health < one_ship_health_atacker * (atacker.count - 1):
                    atacker.count -= 1
                    atacker.atack_rocket_power -= one_ship_atack_atacker
                    atacker.mass -= one_ship_mass_atacker
            if defender.count > 1:
#                for i in range(defender.count):
                if defender.health < one_ship_health_defender * (defender.count - 1):
                    defender.count -= 1
                    defender.atack_rocket_power -= one_ship_atack_defender
                    defender.mass -= one_ship_mass_defender

                
            print(atacker.get_ship_info())
            print(defender.get_ship_info())
            print("defender shild:", defender.shild)
            print("atacker shild:", atacker.shild)
            print("defender cont:", defender.count)
            print("atacker count:", atacker.count)

            print("round", count," finished")

            if atacker.health <= 0:
                end_battle(defender,atacker)
                break
    def battle(fleet, fleet2):
        if fleet.mass > fleet2.mass:
            attack(fleet2, fleet)
        else:
            attack(fleet, fleet2)
    print(type(cruser_fleet))
    print(type(battle_ship))
    battle(cruser_fleet, battle_ship)
first_battle()    
#fleet1 = Fleet(cruser,cruser)
#fleet2 = Fleet(fleet1,cruser)
#fleet2.get_ship_info()