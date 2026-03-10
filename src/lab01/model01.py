class Transaction:
    """Транзация"""
    def __init__(self, t_type: str, amount: float):
        self.__t_type = t_type
        self.__amount = amount

    def __repr__(self):
        return f"[{self.__t_type}: {self.__amount:>8}$]"
    


class Credit:
    """Кредит"""
    def __init__(self, amount: float, rate: float):
        self.__amount = amount
        self.__rate = rate
        self.__is_paid = False

    def _validate(self, val, name):
        if val <= 0: raise ValueError(f"{name} Должна быть > 0")
        return val
    
    @property
    def amount(self):return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = self._validate(value, "Сумма кредита")

    @property
    def rate(self):
        return self.__rate
    
    @rate.setter
    def rate(self, value):
        self.__rate = self._validate(value, "Ставка")
    
    def get_full_debt(self):
        return self.__amount * (1 + self.__rate / 100)
    
    def __str__(self):
        return f"Кредит на {self.__amount}$ (Ставка: {self.__rate}%)"
    


class Deposit:
    """Депозит под процент""" 
    def __init__(self, amount: float, rate: float):
        self.__amount = amount
        self.__rate = rate

    def calculate_profit(self, months: int):
        return self.__amount * (self.__rate / 100 / 12) * months

    def __repr__(self):
        return f"Депозит (сумма={self.__amount}, ставка={self.__rate}%)"



class BankAccount:
    """Банквский счет"""
    bank_name = "NoMoney-NoHoney Group"

    def __init__(self, acc_id: str, balance: float):
        self.__acc_id = self._validate_id(acc_id)
        self.__balance = balance
        self.__history = []
        self.__is_frozen = False

    def _validate_id(self, val):
        if len(val) < 5: raise ValueError("ID счета слишком короткий")
        return val
    
    @property
    def balance(self): return self.__balance

    @property
    def acc_id(self): return self.__acc_id

    def change_balance(self, amount, op_type):
        if self.__is_frozen:
            print("Счет заморожен в морозилке")
            return False

        self.__balance += amount 
        self.__history.append(Transaction(op_type, amount))

        if self.__balance < -50000:
            print("Слишком большой долг. Счет заморожен, продавай почку")
            self.__is_frozen = True
        return True
    
    def __str__(self):
        status = "Заморожен" if self.__is_frozen else "Активен"
        msg = f"Счет {self.__acc_id} | Баланс: {self.__balance}$ | {status}"
        if self.__balance < 0:
            msg == "!!! ВНИМАНИЕ: ДОЛЖНИК !!!"
        return msg



class Client:
    """Клиент"""
    def __init__(self, name: str, account: BankAccount):
        self.__name = self._validate_name(name)
        self.__account = account
        self.__credits = []
        self.__deposits = []

    def _validate_name(self, name):
        if not name: raise ValueError("Пустое значение!")
        return name

    def take_loan(self, amount: float, rate: float):
        """Разрешение на кредит, проверка на задолженность"""
        if self.__account.balance < 0:
            print(f"{self.__name}, необходимо сначала погасить задолженность {self.__account.balance}$!")
        else:
            new_credit = Credit(amount, rate)
            self.__credits.append(new_credit)
            self.__account.change_balance(amount, "КРЕДИТ   ")
            print(f"Кредит одобрен. деньги поступили на счет. Текущий баланс: {self.__account.balance}$")

    def spend_money(self, amount: float):
        """Уход баланса в минус"""
        print(f"Попытка оплаты на {amount}$...")
        if not self.__account.change_balance(-amount, "ОПЛАТА   "):
            print(f"Транзакция отклонена! Счет заблокирован")

    def show_status(self):
        print(f"\n{self.__account}")
        print(f"Долгов по кредитам: {len(self.__credits)}")

    def __eq__(self, other):
        if not isinstance(other, Client): return False
        return self.__account.acc_id == other.__account.acc_id      

