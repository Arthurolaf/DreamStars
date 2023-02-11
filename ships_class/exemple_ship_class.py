import abc
class Blueprint:
    def __init__(self, ship_type, hp, attack, defense, shield):
        self.ship_type = ship_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.shield = shield
        

class Cruiser(Blueprint):
    def __init__(self, hp, attack, defense, shield):
        super().__init__("Cruiser", hp, attack, defense, shield)

class Frigate(Blueprint):
    def __init__(self, hp, attack, defense, shield):
        super().__init__("Frigate", hp, attack, defense, shield)

class Scout(Blueprint):
    def __init__(self, hp, attack, defense, shield):
        super().__init__("Frigate", hp, attack, defense, shield)

class Fleet:
    def __init__(self, ships):
        self.ships = ships

    def sum_ships_of_same_type(self):
        ships_by_type = {}
        for ship in self.ships:
            if ship.ship_type in ships_by_type:
                ships_by_type[ship.ship_type].hp += ship.hp
                ships_by_type[ship.ship_type].attack += ship.attack
                ships_by_type[ship.ship_type].defense += ship.defense
                ships_by_type[ship.ship_type].shield += ship.shield
            else:
                ships_by_type[ship.ship_type] = ship
        return ships_by_type

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

def generate_random_attributes():
    return random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

fleet1 = Fleet([Cruiser(*generate_random_attributes()), Cruiser(*generate_random_attributes()), Frigate(*generate_random_attributes())])
fleet2 = Fleet([Frigate(*generate_random_attributes()), Cruiser(*generate_random_attributes())])

#print(fleet1.ships,"232--023-481-09385")

def merge_fleets(fleet1, fleet2):
    return Fleet(fleet1.ships + fleet2.ships)

big_fleet = merge_fleets(fleet1, fleet2)
print(big_fleet.group_ships_by_type())
print(big_fleet.count_ships_by_type())
sum = 0
for i in big_fleet.ships:
    sum += i.attack
print(sum)

#fleet_2 = Fleet()
fleet_3 = big_fleet.split_by_ship_type("Cruiser")

print(fleet_3.ships)
fleet_4 = fleet_3.split_by_counter(counter=2)
print(fleet_4.ships)
