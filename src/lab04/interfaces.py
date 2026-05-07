from abc import ABC, abstractmethod

# Интерфейс Printable — обязывает классы уметь "показывать себя"
class Printable(ABC):
    @abstractmethod
    def display(self) -> str:
        
        pass

# Интерфейс Comparable — обязывает классы поддерживать сравнение
class Comparable(ABC):
    @abstractmethod
    def compare_with(self, other) -> str:
        
        pass
    