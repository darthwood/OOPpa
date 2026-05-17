from model import Client, SavingsAccount, CreditCard
from collections import ClientCollection
import strategies as st

def run_full_demo():

    bank = ClientCollection()
    
    
    c1 = Client("Иван", SavingsAccount("S-101", 10000, 5, 12))
    c2 = Client("Анна", CreditCard("C-202", 500, 5000, 30))
    c3 = Client("Петр", SavingsAccount("S-103", 50000, 8, 24)) 
    c4 = Client("Елена", CreditCard("C-204", 1500, 2000, 30))
    c5 = Client("Олег", SavingsAccount("S-105", 100, 3, 6))

    for c in [c1, c2, c3, c4, c5]: bank.add(c)
    
    c2.account.take_loan(3000) 
    c4.account.take_loan(500)  

    print("=== ЗАПУСК ПОЛНОЙ ДЕМОНСТРАЦИИ ЛР-5 ===")

    print("\n[СЦЕНАРИЙ 1] Цепочка: Богатые -> По убыванию баланса -> Налог")
    tax_05 = st.AnnualTaxStrategy(0.05) # 5% налог
    (bank
        .filter_by(lambda c: c.account.balance > 1000)
        .sort_by(st.sort_by_balance, reverse=True)
        .apply(tax_05)
        .show("Результат цепочки (только богатые после налога)"))

  
    print("\n[СЦЕНАРИЙ 2] Замена стратегий сортировки без изменения кода коллекции")
    print("--- Сортировка по имени (именованная функция) ---")
    bank.sort_by(st.sort_by_name).show("По имени")
    
    print("--- Сортировка по балансу (lambda) ---")
    bank.sort_by(lambda c: c.account.balance).show("По балансу")

    print("\n[СЦЕНАРИЙ 3] Использование фабрики функций для фильтрации должников")
    debt_filter_3000 = st.make_debt_filter(3000)
    debt_filter_100 = st.make_debt_filter(100)
    
    print("Должники > 3000:")
    bank.filter_by(debt_filter_3000).show("Крупные должники")
    print("Должники > 100:")
    bank.filter_by(debt_filter_100).show("Все должники")

    print("\n[СЦЕНАРИЙ 4] Работа с иерархией классов (только CreditCard)")
    only_cards = bank.filter_by(lambda c: isinstance(c.account, CreditCard))
    only_cards.show("Список владельцев кредитных карт")


    print("\n[СЦЕНАРИЙ 5] Один и тот же результат разными способами")
    
    res1 = bank.filter_by(st.is_active_savings if hasattr(st, 'is_active_savings') else (lambda c: c.account.balance > 0))
    
    res2 = bank.filter_by(lambda c: c.account.balance > 0)
    print(f"Результаты идентичны: {len(res1) == len(res2)}")

   
    print("\n[СЦЕНАРИЙ 6] Массовый запуск полиморфного метода process()")
    
    bank.apply(lambda c: c.account.process())

if __name__ == "__main__":
    run_full_demo()
