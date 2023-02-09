
class ModuleFull(Exception):
    pass
    
class WrongModuleType(Exception):
    pass
    

class Base_of_module():
    """
    Базовый класс модуля из него будем строить остальные
    используется для создания других полноценных модулей путем внесения из словоря атрибутов для модуля

    """
    def __init__(self):
        self.mineral_cost = [0,0,0]
        self.resureses_cost = 0
    def add_slot_attributes (self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)       
    def insert(self, slot_num, slot_type):
        self.module_type = {"number":slot_num, slot_type:-1}
        return self.__dict__