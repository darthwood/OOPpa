from abc import ABC, abstractmethod

# Интерфейс Printable — обязывает классы уметь "показывать себя"
class Printable(ABC):
    @abstractmethod
    def display(self) -> str:
        """
        Абстрактный метод: кода нет, но каждый, кто 
        реализует этот интерфейс, ОБЯЗАН написать свой display.
        """
        pass

# Интерфейс Comparable — обязывает классы поддерживать сравнение
class Comparable(ABC):
    @abstractmethod
    def compare_with(self, other) -> str:
        """
        Контракт на сравнение: заставляет реализовать 
        логику сопоставления двух объектов.
        """
        pass
    