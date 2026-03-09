class Smartphone:
    category = 'Electronics'

    def __init__(self, brand, model, price):
        if price < 0:
            raise ValueError('Это мы вам должны денег что-ли?')
        
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print('Цена не в ту сторону!')
        else:
            self.__price = value

    def apply_discount(self, percent):
        self.__price -= self.__price * (percent / 100)

    def __str__(self):
        return f"Смартфон {self.__brand} {self.__model} (Цена: {self.__price})"

    def __repr__(self):
        return f"Smartphone(brand='{self.__brand}', model='{self.__model}', price={self.__price})"

    def __eq__(self, other):
        if not isinstance(other, Smartphone):
            return False
        return self.__brand == other.__brand and self.__model == other.__model  


class Char:
    game_world = 'Builders in trouble'

    def __init__(self, name: str, level: int, health: int, iq: int):
        if level < 1:
            raise ValueError("Уровень не может быть меньше 1")
        if health < 0:
            raise ValueError("Уровень здоровья не может быть меньше 0")
        if iq < -100:
            raise ValueError("Такой уровень тупизма недосягаем даже для гориллы")
        if iq > 200:
            raise ValueError("Слишком умный для стройки!")
        

        self.__name = name
        self.__level = level
        self.__health = health 
        self.__iq = iq

    @property
    def health(self):
        return self.__health
    
    @property
    def name(self):
        return self.__name
    
    @property
    def level(self):
        return self.__level
    
    @property
    def iq(self):
        return self.__iq

    @health.setter
    def health(self,value):
        if value < 0:
            self.__health = 0 # не может быть ниже 0
        elif value > 100:
            self.__health = 100 # Ну границы то должны быть
        else:
            self.__health = value

    def take_damage(self, damage):
        print(f"Строитель {self.__name} получает {damage} звездюлей")
        self.health -= damage

    def heal(self, litres):
        print(f"Строитель {self.__name} употребляет {litres} водки, но тупеет на {litres}")
        self.health += litres
        self.__iq -= litres

    def level_up(self):
        self.__level += 1
        print(f"Уважение мужиков выросло! Теперь ты мастер {self.__level} разряда!")

    def work(self):
        if self.__iq < 20:
            print(f"{self.__name} сильно всандалил (Рассудок {self.__iq}), стена упала не него!")
            self.take_damage(20)

        elif self.__iq < 0:
            print(f"{self.__name} (IQ: {self.__iq}) перепутал чертеж с газетой. Штукатурщик теперь навсегда в этих стенах. Бригадир дает леща")
            self.take_damage(10)    
        else:
            print(f"{self.__name} ложит широкую на широкую! Мужики одобряют!")
            self.level_up()
            if self.__health < 20:
                print("... сил маловато, надо бы 'поправить здоровье'.")        

    def __str__(self):
        status = "в запое" if self.__iq < 0 else "в адеквате"      
        return f"Халтурщик {self.__name} (Уважение: {self.__level}, Здоровье: {self.__health}, Рассудок: {self.__iq})"

    def __repr__(self):
        return f"Char(name='{self.__name}', level={self.__level}, health={self.__health}, iq={self.__iq})"

    def __eq__(self, other):
        if not isinstance(other, Char):
            return False
        return self.__name == other.__name and self.__level == other.__level        

