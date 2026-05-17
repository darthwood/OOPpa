# src/lab06/container.py
from typing import TypeVar, Generic, List, Callable, Optional, Protocol, runtime_checkable

@runtime_checkable
class Displayable(Protocol):
    def display(self) -> str: ...

@runtime_checkable
class Scorable(Protocol):
    def score(self) -> float: ...

T = TypeVar('T')
R = TypeVar('R')

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        return next((item for item in self._items if predicate(item)), None)

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]

# src/lab06/demo.py
from container import TypedCollection, Displayable, Scorable

class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self._owner = owner
        self._balance = balance
    def display(self) -> str: return f"{self._owner}: {self._balance}"
    def score(self) -> float: return self._balance

def run_demo() -> None:
    accounts: TypedCollection[BankAccount] = TypedCollection()
    accounts.add(BankAccount("Иван", 1500.0))
    
    # Использование filter
    low_balance = accounts.filter(lambda a: a.score() < 1000)
    print(f"Счетов: {len(accounts)}")

if __name__ == "__main__":
    run_demo()
