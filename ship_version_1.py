import random
def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1
ship_types = {2: "transport",6:"colony",3:"scout",4:"cruser",5:"battle_ship",1:"starbase"}


class Ship():
    """
    Этот класс основной для карабли и звездных базы (просто у базы скорость 0 и в некоторых случиях у нее буду колонисты)
    У класса много атрибутов по этому буду часто передавать аргументы листами по несколько элементов, и уже их обрабатывать внутри метода класса
    """
    
    def __init__(self):
        
        self.mineral_cost = [0,0,0]
        self.resureses_cost = 0
        self.slot_count = 1
        self.speed = 0
        self.health = 0
        self.full_tank = 0
        self.mass = 0
        self.ship_type = 0
        self.id = [0]
        self.owner = 0
        

        self.shild = 0
        self.atack_rocket_power = 0
        self.rocket_defense = 0
        self.atack_beam_power = 0
        self.beam_range = 0
        self.beam_defense = 0
        self.rocket_range = 0
        self.cloacking = 0
        self.corgo = [0,0,0,0,0]
        self.attack_speed = 0
        self.regen = 0
        self.bomber_power = 0
        self.full_regen = 0
        self.mining_rate = 0
        self.detonator_power = 0
        self.gate = 0
        self.count = 1
        self.mobility = 0
        self.lucky = 0
        self.radar_power = [0,0]
        self.task = 0 # optional
        self.repare_fleat = 0
        self.speed = 0
        self.fleat = {id:[]}
        self.item_type = {0:0}
#    def __add__(self, cls):
 #           return add_item(self, cls).sum

    class add_item():
        def __init__(self, class_1, class_2, remove=False):
            self.sum = class_1
            self.class_2 = class_2
            for attr in self.class_2.__dict__:
                if attr in self.sum.__dict__:
                    if getattr(self.sum, "slot_count") > -1:
                        if type(getattr(self.sum, attr)) is list:
                            var_list_set = []
                            for i in range(len(getattr(self.class_2, attr))): 
                                if remove is False:
                                    var_list_set.append(getattr(self.class_2, attr)[i] + getattr(self.sum, attr)[i])         
                                elif remove is True:
                                    var_list_set.append(getattr(self.sum, attr)[i] - getattr(self.class_2, attr)[i])
                                else:
                                    var_list_set = getattr(self.sum,attr) 
                            setattr(self.sum, attr, var_list_set)
                        
                        elif type(getattr(self.sum, attr)) is dict:
                            for key,value in getattr(self.class_2, attr).items():
                                if remove is False:
                                    getattr(self.sum, attr).setdefault(key,value)
                                elif remove is True:
                                    del getattr(self.sum, attr)[key]
                        
                        else:
                                if remove is False:
                                    setattr(self.sum, attr, getattr(self.class_2, attr) + getattr(self.sum, attr))
                                if getattr(self.sum, "slot_count") == -1:
                                    raise Exception("can't add item no emply slots")
                        
                                elif remove is True:
                                    setattr(self.sum, attr, getattr(self.sum, attr) - getattr(self.class_2, attr))
                                    
                else:
#                    print(attr)
                    if attr == "shild":
                        print("not in",getattr(self.class_2, attr), getattr(self.sum, attr))

                    setattr(self.sum, attr, getattr(self.class_2, attr))


    def create_ship(self, *args):
        """
        take list of *args must include

        [mineral_cost = [0,0,0], resureses_cost = 0, slot_count = 1, health = 0, full_tank = 0, mass = 0, ship_type = 0, id = 0, owner = 0]

        """
        self.mineral_cost = args[0]
        self.resureses_cost = args[1]
        self.slot_count = args[2]
        self.health = args[3]
        self.full_tank = args[4]
        self.mass = args[5]
        self.ship_type = args[6]
        self.id = args[7]
        self.owner = args[8]

    def get_ship_info(self, debug=False):
        if debug is False:
            attributes = [self.atack_beam_power, self.atack_rocket_power, self.attack_speed, self.beam_defense, self.beam_range, self.bomber_power, 
                        self.cloacking, self.corgo, self.count, self.detonator_power, self.full_regen, self.full_tank, self.gate, 
                        self.health, self.id, self.lucky, self.mass, self.mineral_cost, self.mining_rate, self.mobility, self.owner, 
                        self.radar_power, self.regen, self.repare_fleat, self.resureses_cost, self.rocket_defense, self.rocket_range,
                        self.shild, self.ship_type, self.slot_count, self.speed, self.task]
            return attributes
        else:
            attributes = {"mass":self.mass, "id":self.id, "speed":self.speed, "resuses_cost":self.resureses_cost, 
                        "mineral_cost":self.mineral_cost, "health":self.health, "type":ship_types[self.ship_type], "item_type": self.item_type}
            return attributes

    def set_item(self, item):
        self.add_item(self, item)
        if self.ship_type == 1:
            self.speed = 0
    
    def remove_item(self, item):
        self.add_item(self, item, remove=True)
        if self.ship_type == 1:
            self.speed = 0


def test():
    class item():
    
        def __init__(self):
            self.item_type = {1:0}
            self.speed = 3
            self.mass = 10
            self.slot_count = -1
            self.mineral_cost = [1,2,2]


    ship = Ship()
    ship_attributes = []
    for z in range(32):
        ship_attributes.append(0)
    #print(len(ship_attributes))
    #print(len(ship.get_ship_info()))


    mineral_cost = [3,5,3]
    resureses_cost = 10
    slot_count = 1
    health = 10
    full_tank = 100
    mass = 10
    ship_type = 1
    owner = 0
    unique_sequence = uniqueid()
    id = next(unique_sequence)
            

        
    ship.create_ship(mineral_cost, resureses_cost, slot_count, health , full_tank, mass , ship_type , id , owner)
    engine = item()
    engine.__setattr__("health", 100)
    print(ship.get_ship_info(debug=True))
    print("")
    ship.set_item(engine)
    print(ship.get_ship_info(debug=True))
    ship.remove_item(engine)
    print(ship.get_ship_info(debug=True))
    print(ship.id)

#test()


# нужно еще документация написать к этому классу (он чуть сложнее чем планеты)
class Fleet(Ship):
    def __add__(self, cls):
        return self.megre(self, cls).sum            
    class megre():
        def __init__(self, class_1, class_2):
            self.attributes_to_join = ["atack_beam_power", "atack_rocket_power", "bomber_power", "cloacking", "corgo", "count", "detonator_power", "full_regen", "full_tank", 
                        "health", "mass", "mineral_cost", "mining_rate", "repare_fleat", "resureses_cost", "rocket_defense", "shild"]
            self.sum = class_1
            self.class_2 = class_2
            for attr in self.class_2.__dict__:
                if attr in self.attributes_to_join:
                    self.sum_attr(attr)
    
    

        def sum_attr(self,attr):
            if attr in self.sum.__dict__:
                if type(getattr(self.sum, attr)) is list:
                    var_list_set = []
                    for i in range(len(getattr(self.class_2, attr))): 
                        var_list_set.append(getattr(self.class_2, attr)[i] + getattr(self.sum, attr)[i])         
                    setattr(self.sum, attr, var_list_set)
                else:
                    setattr(self.sum, attr, getattr(self.class_2, attr) + getattr(self.sum, attr))
                   # print("sum", attr, getattr(self.sum, attr))
            else:
                setattr(self.sum, attr, getattr(self.class_2, attr))
               # print("add", attr, getattr(self.sum, attr))      