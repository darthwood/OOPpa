from model import Client  

class ClientCollection:
    """Контейнерный класс с поддержкой функционального стиля и цепочек."""

    # Притаскиваем пустую коробку или сразу засыпаем туда готовую толпу людей
    def __init__(self, clients=None):
        self.__clients = list(clients) if clients else []  # Запихиваем всех в приватный список

    # Ловим нового клиента и кидаем в коробку
    def add(self, client: Client):
        # Проверяем, нет ли в коробке точно такого же слоняры
        if client not in self.__clients:
            self.__clients.append(client)  # Если уникальный — добро пожаловать на борт
        return self  # Возвращаем саму коробочку с типами

    # Метод сортировки. 
    def sort_by(self, strategy_func, reverse=False):
        """Паттерн Стратегия: передача внешней функции сортировки."""
        self.__clients.sort(key=strategy_func, reverse=reverse)  # Сортируем список по указке сверху
        return self  # Возвращаем коробку

    # Метод жесткого отбора (оставляем только элиту или наоборот — только должников)
    def filter_by(self, predicate_func):
        """Функция высшего порядка: фильтрация через встроенный filter."""
        filtered_list = list(filter(predicate_func, self.__clients))  # Прогоняем толпу через сито фито
        return ClientCollection(filtered_list)  # Сгружаем выживших в НОВУЮ чистую коробку и отдаем её

    # Выдираем из клиентов только нужные показания
    def map_to_list(self, transform_func):
        """Трансформация элементов коллекции в обычный плоский список."""
        return list(map(transform_func, self.__clients))  # Перебираем всех, потрошим по правилу и отдаем обычный list

    # Метод массового поражения — применяет функцию ко всем вообще без разбора
    def apply(self, modify_func):
        """Метод трансформации: применяет func ко всем элементам."""
        for client in self.__clients:
            modify_func(client)  # Заставляем функцию отработать по печени текущего клиента
        return self  # Возвращаем коробку

    # Метод великого схлопывания: превращает толпу людей в одну общую например, сумму долгов
    def reduce_to_value(self, reducer_func, initial=None):
        """Агрегация (свертка) данных всей коллекции без использования модуля functools."""
        # Если коробка пустая, а считать надо с нуля, врубаем панику и визжим
        if not self.__clients and initial is None:
            raise ValueError("Нельзя свернуть пустую коллекцию без начального значения!") 
        
        # Рулим стартовой точкой через срезы, чтобы не сломать итератор
        if initial is None:
            accumulator = self.__clients  # Назначаем "жертвой" первого клиента из списка
            items_to_process = self.__clients[1:]  # А обрабатывать начнем со второго
        else:
            accumulator = initial  # Начинаем считать с той цифры, которую нам дали
            items_to_process = self.__clients  # В обработку пускаем вообще всех
            
        # Начинаем великий просчет
        for client in items_to_process:
            accumulator = reducer_func(accumulator, client)  # Варим кашу: нанизываем данные клиента на аккумулятор
            
        return accumulator  # Выдаем итоговый суп наружу

    # Ищет первого попавшегося счастливчика, который подошел под условия
    def find_first(self, predicate_func):
        """Возвращает первый найденный элемент по условию или None."""
        return next(filter(predicate_func, self.__clients), None)  # Хватаем первого встречного или отдаем None

    # Проверка: есть ли в нашей банде ХОТЬ ОДИН подходящий тип?
    def is_any(self, predicate_func):
        """Возвращает True, если хотя бы один элемент коллекции подходит под условие."""
        return any(map(predicate_func, self.__clients))  # Если хоть один нашелся — вернет True

    # Проверка на тотальное соответствие (все ли в этой коробке святые или богатые?)
    def is_all(self, predicate_func):
        """Возвращает True, если абсолютно все элементы подходят под условие."""
        return all(map(predicate_func, self.__clients))  # Вернет True, только если абсолютно все прошли проверку

    # Выводим весь наш зоопарк на экран
    def show(self, title="Состояние коллекции"):
        print(f"\n--- {title} ---") 
        # Если коробка пуста как моя голова на контрохе
        if not self.__clients:
            print("Пусто") 
        # Перебираем всех по очереди
        for c in self.__clients:
            print(c)  # Печатаем строковый образ текущего кожаного мешка
        return self  # Возвращаем коробку для бесконечных цепочек методов

    # Позволяем Python мерить длину коробки по-человечески
    def __len__(self):
        return len(self.__clients)  # Отдаем реальное число душ внутри коробки

    # Позволяет нагло тыкать в коробку квадратными скобками
    def __getitem__(self, index):
        return self.__clients[index]  # Достаем кента по его порядковому номеру
