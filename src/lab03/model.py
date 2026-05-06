class BankAccount:

    def __init__(self, acc_id: str, balance: float):
        self._acc_id = acc_id  
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def change_balance(self, amount):
        self._balance += amount
        return True

    def __str__(self):
        return f"Счет {self._acc_id} | Баланс: {self._balance}$"

    def process(self):
        print(f"--- Базовая проверка счета {self._acc_id} ---")  #полиморф


class SavingsAccount(BankAccount):
    
    def __init__(self, acc_id: str, balance: float, interest_rate: float, term_months: int):
        super().__init__(acc_id, balance) 
        self.interest_rate = interest_rate 
        self.term_months = term_months     

    def apply_interest(self): #***
        bonus = self._balance * (self.interest_rate / 100)
        self.change_balance(bonus)
        return bonus

    def process(self): 
        super().process()
        bonus = self.apply_interest()
        print(f"Начислены проценты: +{bonus}$")

    def __str__(self): 
        return f"Денег на депозите: {super().__str__()} | Ставка: {self.interest_rate}%"


class CreditCard(BankAccount):
    
    def __init__(self, acc_id: str, balance: float, credit_limit: float, grace_period: int):
        super().__init__(acc_id, balance)
        self.credit_limit = credit_limit 
        self.grace_period = grace_period 
        self.debt = 0.0

    def take_loan(self, amount):
        if amount <= self.credit_limit:
            self.debt += amount
            self.change_balance(amount)
            print(f"Кредит на {amount}$ получен")
        else:
            print("Превышен лимит!")

    def process(self): 
        super().process()
        if self.debt > 0:
            fee = self.debt * 0.05
            self.change_balance(-fee)
            print(f"Удержана комиссия за кредит: -{fee}$")

    def __str__(self): 
        return f"Кредит: {super().__str__()} | Долг: {self.debt}$"
