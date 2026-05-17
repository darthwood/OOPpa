from typing import TypeVar, Generic, Callable, Optional, Protocol 

# Рождаем универсальный кирпич для любых типов данных. Назовем его Т
T = TypeVar('T')
# Рождаем второй кирпич, чтобы превращать одни типы в другие (например, клиентов в баксы)
R = TypeVar('R')

# Протоколы (Утиная полиция моды) ---
class Displayable(Protocol):
    """Этот протокол клянется, что объект умеет красиво пиариться в консоли."""
    def display(self) -> str:
        ...  # Метод-пустышка

class Scorable(Protocol):
    """Этот протокол клянется, что у объекта можно нагло отжать его баланс."""
    def score(self) -> float:
        ...  # Тоже пустышка


# Создаем спец-кирпичи с ограничениями: D обязан уметь в display, а S — в score
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


class TypedCollection(Generic[T]):
    """Умный сейф, который теперь точно знает, чьи кошельки лежат внутри."""

    # Конструктор: принимает готовый список строго типа T или оставляет пустым
    def __init__(self, items: Optional[list[T]] = None) -> None:
        self.__items: list[T] = list(items) if items else [] 

    # Метод добавления элемента в сейф
    def add(self, item: T) -> 'TypedCollection[T]':
        # Если такого клона у нас еще нет в базе
        if item not in self.__items:
            self.__items.append(item)  # Кидаем его в общую кучу
        return self  #это чтобы строить цепочки методов через точку

    # Метод выгрузки всех запасов
    def get_all(self) -> list[T]:
        return list(self.__items)  # Отдаем копию списка, от греха подальше

    # Метод поиска первого выжившего по условию
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self.__items:
            # Если предикат заорал True на этот элемент
            if predicate(item):
                return item  # Срочно отдаем везунчика наружу
        return None  # Если обошли всех, а кругом одни бомжи — отдаем честный None

    # Метод массовой фильтрации толпы
    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        # Собираем в новый список только тех, на кого предикат выдал True
        return [item for item in self.__items if predicate(item)]

    # Метод тотальной мутации
    def map(self, transform: Callable[[T], R]) -> list[R]:
        # Берем каждого, потрошим функцией transform и на выходе получаем ВООБЩЕ другой тип R
        return [transform(item) for item in self.__items]

    # Метод массового поражения (применяет функцию к элементам на месте)
    def apply(self, modify_func: Callable[[T], None]) -> 'TypedCollection[T]':
        for item in self.__items:
            modify_func(item)  # Заставляем функцию отработать по печени элемента
        return self 

    # Позволяет понимать длину коробки через len()
    def __len__(self) -> int:
        return len(self.__items)  # Просто отдаем размер списка

    # Позволяет нагло тыкать в коробку квадратными скобками: collection[0]
    def __getitem__(self, index: int) -> T:
        return self.__items[index] 
