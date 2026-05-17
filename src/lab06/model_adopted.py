class BankAccount:
    # Обычный счет: нужен ID для налоговой и баланс для списаний
    def __init__(self, acc_id: str, balance: float) -> None:
        self._acc_id: str = acc_id
        self._balance: float = balance 

    # Метод изменения баланса (пополнение или грабеж)
    def change_balance(self, amount: float) -> bool:
        # Если после списания баланс улетит в жесткий минус
        if self._balance + amount < 0:
            return False  # банк не благотворительный фонд
        self._balance += amount 
        return True  

    # Как напечатать счет, чтобы не плакать
    def __str__(self) -> str:
        return f"Счет {self._acc_id} | {self._balance}$"


class Client:
    """Кожаный мешок, который мы упакуем в Протоколы этой лабы."""
    # Создаем клиента, привязывая его к аккаунту
    def __init__(self, name: str, account: BankAccount) -> None:
        self.__name: str = name  # Прячем имя за два подчеркивания чтоб не убег
        self.__account: BankAccount = account  # Прячем его кошелек туда же

    @property
    def name(self) -> str:
        return self.__name 

    @property
    def account(self) -> BankAccount:
        return self.__account

    # --- ЗАКРЫВАЕМ ТРЕБОВАНИЕ ПРОТОКОЛА DISPLAYABLE ---
    def display(self) -> str:
        return f"Клиент: {self.__name} | Аккаунт: {self.__account}" # Выдаем рожи

    # --- ЗАКРЫВАЕМ ТРЕБОВАНИЕ ПРОТОКОЛА SCORABLE ---
    def score(self) -> float:
        return self.__account._balance  # Сливаем баланс клиента по первому требованию

    def __str__(self) -> str:
        return self.display()  # Прост есть и все
