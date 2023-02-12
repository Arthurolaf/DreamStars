from ship_modules import Base_of_module, WrongModuleType, ModuleFull

class Blueprint:
    """
    Этот класс является основой для большинства короблей, имеет множество атрибутов (жизни, стоимость, и т.д)

    """
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
        """
        Функция принимает список модулей которые поставили на карабль, и пытается их поставить по очереди через функцию self.insert_slot()
        """
        for _module_ in modules:
            self.insert_slot(_module_)    

    def insert_slot(self, module):
        """
        Функция принимает параметры модуля который хотят поставить на карабль, проверяет можно ли вообще поставить такой модуль в указаный слот.
        Если нет то функция сообщает об этом, что модуль ошибочный или что метса в этом слоте больше нету.
        Возможно эту функцию я еще перепишу или попробую вынести за пределы класса. (хотя чувствую это плохая идея)
        """
        def add_atributes_from_module():
            """
            Добавляет большенство тарибутов с модуля на карабль.(которые не были добавлены)
            """
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
                            add_atributes_from_module()
                        else:
                            raise ModuleFull ("Slot is full, no place for this module")
                    elif k == "any":
                        self.slots[element][k] += module["module_type"][module_keys[1]]
                        if self.slots[element][k] > -1:
                            add_atributes_from_module()
                        else:
                            raise ModuleFull ("Slot is full, no place for this module")
    def ship_info(self):
        """
        Возвращаем общее название атрибутов и их значение в виде словоря
        """
        return self.__dict__