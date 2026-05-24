class BankAccount:
    """Класс обычного счета, куда капает зарплата и откуда списывается налог на воздух."""
    def __init__(self, acc_id: str, balance: float) -> None:
        self.acc_id: str = acc_id  # Номер счета, по которому нас найдет налоговая
        self.balance: float = balance  # Сумма денег (вечно стремящаяся к нулю)

    def change_balance(self, amount: float) -> bool:
        """Метод изменения баланса. Возвращает False, если клиент пытается украсть у банка."""
        if self.balance + amount < 0:
            return False  # Денег нет, держитесь там
        self.balance += amount  # Корректируем сумму
        return True  # Машем ручкой и подтверждаем операцию

    def __str__(self) -> str:
        return f"Счет {self.acc_id} | {self.balance}$"  # Как выглядит счет, если его распечатать


class Client:
    """Сам кожаный мешок (клиент), которого мы будем обслуживать и обдирать."""
    def __init__(self, name: str, account: BankAccount) -> None:
        self.name: str = name  # Имя жертвы капитализма
        self.account: BankAccount = account  # Привязанный кошелек

    def display(self) -> str:
        """Ориентировка на клиента для вывода в консоль."""
        return f"Клиент: {self.name} | {self.account}" 

    def score(self) -> float:
        """Сливает баланс клиента по первому требованию системы."""
        return self.account.balance  # Просто возвращаем число с баланса

    def __str__(self) -> str:
        return self.display()  # Делаем так, чтобы обычный принт вызывал display()
