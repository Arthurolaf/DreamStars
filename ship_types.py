from ships_blueprint import Blueprint
from ship_modules import Base_of_module

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
