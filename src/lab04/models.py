from interfaces import Printable, Comparable
from abc import ABC


class BankAccount(Printable, Comparable, ABC):
    def __init__(self, acc_id: str, balance: float):
        self._acc_id = acc_id
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    
    def compare_with(self, other: 'BankAccount') -> str:
        
        if not isinstance(other, BankAccount):
            return "Ошибка: Сравнение возможно только с другим банковским счетом"
            
        
        if self.balance > other.balance:
            return f" {self._acc_id} ({self.balance}$) богаче, чем {other._acc_id} ({other.balance}$)"
        
        
        elif self.balance < other.balance:
            return f" {self._acc_id} ({self.balance}$) беднее, чем {other._acc_id} ({other.balance}$)"
        
        
        else:
            return f" {self._acc_id} и {other._acc_id} имеют одинаковый баланс ({self.balance}$)"



class SavingsAccount(BankAccount):
    
    def display(self) -> str:
        return f"[СБЕРЕГАТЕЛЬНЫЙ] {self._acc_id} | Баланс: {self._balance}$"


class CreditCard(BankAccount):
    
    def display(self) -> str:
        return f"[КРЕДИТКА] {self._acc_id} | Баланс: {self._balance}$"
