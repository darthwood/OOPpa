class Tool:
    def __init__(self, title: str, power: int):
        self.__title = self._validate_str(title)
        self.__power = self._validate_int(power)

    def _validate_str(self, val):
        if not val : raise ValueError("название инструмента не может быть пустым")
        return val

    def _validate_int(self, val):
        if val < 0: raise ValueError("Мощность не может быть отрицательной")
        return val

    @property
    def power(self): return self.__power

    def use(self):
        return True

    def __repr__(self):
        return f"Инструмент('{self.__title}', {self.__power})"

class Char:
    game_world = "Гордость бригады"

    def __init__(self, name: str, level: int, health: int, iq: int, tool: Tool = None):
        self.__name = self._validate_name(name)
        self.__level = self._validate_level(level)
        self.__iq = self._validate_iq(iq)
        self.__health = self._validate_health(health)
        self.__tool = tool
        self.__is_fired = False

    def _validate_name(self, name):
        if not name or len(name.strip()) < 2:
            raise ValueError("Имя слишком короткое")
        return name

    def _validate_level(self, level):
        if not (1 <= level <= 6):
            raise ValueError("Разряд должен быть от 1 до 6")
        return level

    def _validate_health(self, health):
        if not (0 <= health <= 100):
            raise ValueError("Здоровье при спавне должно быть от 0 до 100")
        return health

    def _validate_iq(self, val):
        if val < -100: raise ValueError("Такой уровень тупизма недосягаем даже для гориллы!")
        if val > 200: raise ValueError("Слишком умный для стройки!")
        return val

    @property
    def health(self): return self.__health

    @health.setter
    def health(self, val):
        if val < 0: self.__health = 0
        elif val > 100: self.__health = 100
        else: self.__health = val

    @property
    def name(self): return self.__name

    @property
    def level(self): return self.__level

    @property
    def iq(self): return self.__iq

    @iq.setter
    def iq(self, val):
        self.__iq = val

    @property
    def is_fired(self): return self.__is_fired

    def fire(self):
        self.__is_fired = True
        print(f"{self.__name} уволен! Трудовая книжка выброшена в бетономешалку")

    def take_damage(self, damage):
        print(f"Строитель {self.__name} получает {damage} звездюлей")
        self.health -= damage  

    def drink_vodka(self, litres):
        print(f"{self.__name} всандалил {litres} литров. Здоровье поправили, IQ убавилось")
        self.__health += litres * 15
        self.__iq -= litres * 20     

    def work(self):
        if self.__is_fired:
            print(f"{self.__name} не может работать, он уволен и спит в бытовке")
            return 0

        power = self.__level * 10
        bonus = self.__tool.power if self.__tool else 0

        if self.__tool and self.__tool.use():
            power += 20
            print(f"{self.__name} (Разряд: {self.__level}) использует {repr(self.__tool)}")

        if self.__iq < 0:
            print(f"{self.__name} (IQ: {self.__iq}) перепутал чертеж с газетой. Штукатрущик замурован в стену. Бригадир дает леща")
            self.take_damage(10)
            power = (power + bonus) // 2
        elif self.__iq < 20:
            print(f"{self.__name} сильно всандалил и криво ложил кирпич, (ICQ: {self.__iq}), стена упала на него!")
            self.take_damage(20)
            power = 10 + bonus
        else:
            print(f"{self.__name} ложит широкую на широкую! Мужики одобряют!")
            if self.__level < 6: 
                self.__level += 1
                print(f"Разряд повышен до {self.__level}!")
            power += 20 + bonus

        self.health -= 10
        return power    
                  
    def __str__(self):
        status = "В ЗАПОЕ" if self.__iq < 0 else "ТРЕЗВ"
        if self.__is_fired: status = "УВОЛЕН"
        return f"{self.__name:<10} | Разряд: {self.__level} | Здоровье: {self.__health} | IQ: {self.__iq:>3} | [{status}]"

    def __repr__(self):
        return f"Халтурщик(name='{self.__name}', level={self.__level}, iq={self.__iq})"

    def __eq__(self, other):
        if not isinstance(other, Char): return False
        return self.__name == other.__name and self.__level == other.__level
     


class ConstructionSite:
    def __init__(self, title: str, required_power: int):
        self.__title = title
        self.__req = required_power

    def check_worker(self, worker: Char):
        print(f"\n Объект: {self.__title} (Сложность: {self.__req})")
        effort = worker.work()

        if effort >= self.__req:
            print(f"Успешно построили!")
        else:
            print(f"Мощей не хватило. Только сырье перевели")
            worker.fire()



