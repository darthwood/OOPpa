from typing import TypeVar, Generic, Callable, Optional  
from models import Client, BankAccount 
from exceptions import ClientNotFoundError, DuplicateClientError  

T = TypeVar('T', bound=Client)  # дженерик работает строго с клиентами

class BankApplication(Generic[T]):
    """Мозг всей системы. Управляет коллекцией и делает вид, что проводит аудит."""
    def __init__(self) -> None:
        self.__items: list[T] = []  # Наш приватный сейф с данными

    def set_items(self, items: list[T]) -> None:
        """Загружает готовый список клиентов (используется при автозагрузке)."""
        self.__items = items  # Просто перезаписываем внутренности сейфа

    def get_all(self) -> list[T]:
        """Отдает список всех клиентов."""
        return list(self.__items)  # Отдаем копию, чтобы никто снаружи не сломал оригинал

    def add_client(self, name: str, acc_id: str, balance: float) -> None:
        """Создает и добавляет клиента. Если такой ID уже есть — бьет тревогу!"""
        for item in self.__items:
            if item.account.acc_id == acc_id:
                raise DuplicateClientError(f"Счет с ID {acc_id} уже обчищается нашей системой!")  # Замыкание на дубликате
        acc = BankAccount(acc_id, balance)  # Рождаем кошелек
        new_client = Client(name, acc)  # Рождаем самого счастливчика
        self.__items.append(new_client)  # Закидываем в общую кучу

    def remove_client(self, acc_id: str) -> None:
        """Выкидывает клиента из банка по ID его счета."""
        target = self.find_by_id(acc_id)  # Пытаемся найти бедолагу
        if not target:
            raise ClientNotFoundError(f"Клиент со счетом {acc_id} не найден. Наверное, сбежал за границу.")  # Ругаемся
        self.__items.remove(target)  # Убираем его из списка

    def find_by_id(self, acc_id: str) -> Optional[T]:
        """Ищет одного конкретного клиента по его ID счета."""
        for item in self.__items:
            if item.account.acc_id == acc_id:
                return item  # Нашли голубчика
        return None  # Никого не нашли, грустим

    def filter_by_balance(self, min_balance: float) -> list[T]:
        """Фильтрует клиентов, оставляя только тех, у кого баланс выше порога."""
        return [item for item in self.__items if item.score() >= min_balance]  # Чистый списковый генератор

    def sort_by_strategy(self, choice: int) -> None:
        """Сортирует коллекцию по выбранной пользователем стратегии."""
        if choice == 1:
            self.__items.sort(key=lambda c: c.name)  # Стратегия: по алфавиту имен
        elif choice == 2:
            self.__items.sort(key=lambda c: c.score(), reverse=True)  # Стратегия: от мажоров к беднякам
