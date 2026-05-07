from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def display(self) -> str:
        
        pass


class Comparable(ABC):
    @abstractmethod
    def compare_with(self, other) -> str:
        
        pass
    