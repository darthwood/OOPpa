from model import Client

class ClientCollection:
    """Контейнерный класс для управления клиентами бонка"""

    def __init__(self):
        self.__clients = []

    def add(self, client: Client):
        """Добавить клиента в коллекцию"""
        if not isinstance(client, Client):
            raise TypeError("Можно добавлять только объекты класса Client")

        if client not in self.__clients:
            self.__clients.append(client)
        else:
            print(f"Клиент с ID {client.account_id} уже в базе имеется.")    

    def remove(self, acc_id:str):
        """Трем клиента по ID-месту"""
        target = self.get_by_id(acc_id)
        if target:
            self.__clients.remove(target)
            return True
        return False

    def get_by_id(self, acc_id:str):
        """Серч кента по ID счета"""
        for client in self.__clients:
            if client.account_id == acc_id:
                return client
        return None

    def __iter__(self):
        """Перебирай по одному! Я их карточку делал!"""
        return iter(self.__clients)

    def __len__(self):
        """Счет"""
        return len(self.__clients)

    def __getitem__(self, index):
        """Доступ по индексу""" 
        return self.__clients[index]

    def __repr__(self):
        return f"ClientCollection(count={len(self.__clients)})"  

    def get_all(self):
        """Огласите весь список, пожалуйста"""
        return self.__clients[:] #Это копия списка [:], чтоб никто ничего не менял  

    def find_by_id(self, acc_id: str):
        """Поиск одного клиента по уникальному ID счета"""
        for client in self.__clients:
            if client.account_id == acc_id:
                return client
        return None

    def find_by_name(self, name: str):
        """Поиск списка клиентов по имени"""
        result = ClientCollection()
        for c in self.__clients:
            if c._Client__name == name:
                result.add(c)
        return result

    def find_by_title(self, title_part: str):
        """Поиск по частичному совпадению в ID В НОВОЙ коллекции"""
        result = ClientCollection()
        for c in self.__clients:
            if title_part.lower() in c.account_id.lower():
                result.add(c)
        return result      

    def sort(self, key, reverse=False):
        """Сортирует объекты внутри коллекции"""
        self.__clients.sort(key=key, reverse=reverse)
        print("Коллекция отсортирована.") 

    def get_active(self):
        """Возвращает новую коллекцию с активными счетами"""
        result = ClientCollection()
        for c in self.__clients:
            if not c._Client__account._BankAccount__is_frozen:
                result.add(c)
        return result

    def get_available(self):
        """Возвращает новую коллекцию клиентов с положительным балансом"""
        result = ClientCollection()
        for c in self.__clients:
            if c._Client__account.balance >= 0:
                result.add(c)
        return result

    def get_expensive(self, threshold=100000):
        """Возвращает новую коллекцию богатых клиентов"""
        result = ClientCollection()
        for c in self.__clients:
            if c._Client__account.balance > threshold:
                result.add(c)
        return result 