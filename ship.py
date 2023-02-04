def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1
class Ship():
    """
    Этот класс основной для карабли и звездных базы (просто у базы скорость 0 и в некоторых случиях у нее буду колонисты)
    """

    def __init__(self):
        self.mineral_cost = [0,0,0]
        self.resureses_cost = 0
        self.slot_num = 1
        self.speed = 0
        self.health = 0
        self.shild = 0
        self.atack_rocket_power = 0
        self.rocket_defense = 0
        self.atack_beam_power = 0
        self.beam_range = 0
        self.beam_defense = 0
        self.rocket_range = 0
        self.stels = 0
        self.full_tank = 0
        self.corgo = 0
        self.mass = 0
        self.ship_type = 0
        self.attack_speed = 0
        self.regen = 0
        self.bomber_power = 0
        self.full_regen = 0
        self.mining_rate = 0
        self.detonator_power = 0
        self.gate = 0
        self.id = [0]
        self.count = 0
        self.mobility = 0
        self.lucky = 0
        self.radar_power = [0,0]
        self.owner = 0
        self.task = 0 # optional
        self.repare_fleat = 0
        

    def set_item(self, item,slot_num=0,):
        pass

ship = Ship()

