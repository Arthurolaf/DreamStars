def merge_fleets(fleet1, fleet2):
    """
    Функция для обхединения флотов.
    """
    return Fleet(fleet1.ships + fleet2.ships)



class Fleet:
    def __init__(self, ships):
        self.ships = ships

    
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
