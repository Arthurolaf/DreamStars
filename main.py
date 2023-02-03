from planet import Planet 


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

test()

