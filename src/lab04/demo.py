from models import SavingsAccount, CreditCard
from interfaces import Printable, Comparable


def print_any_objects(items: list[Printable]): #Важно тольк опринтабл
    
    print("\n--- ИНТЕРФЕЙС PRINTABLE Универсальный вывод объектов ---")
    for item in items:
        print(item.display())

def compare_all_pairs(items: list[Comparable]): #Важно только компарабл
    
    print("\n--- ИНТЕРФЕЙС COMPARABLE Попарное сравнение счетов ---")
    for i in range(len(items) - 1):
        print(items[i].compare_with(items[i+1]))



rich_acc = SavingsAccount("SBER-VIP", 15000.0)
poor_acc = CreditCard("TINK-MIN", 500.0)
equal_acc1 = SavingsAccount("VTB-001", 2000.0)
equal_acc2 = CreditCard("ALFA-002", 2000.0)


portfolio = [rich_acc, poor_acc, equal_acc1, equal_acc2]



def run_demo():
    print("=== ЛАБОРАТОРНАЯ РАБОТА №4: ИНТЕРФЕЙСЫ И ПОЛИМОРФИЗМ ===")


    print_any_objects(portfolio)

    print("\n--- Проверка всех условий сравнения ---")
    

    print(f"Тест (>): {rich_acc.compare_with(poor_acc)}")
    

    print(f"Тест (<): {poor_acc.compare_with(rich_acc)}")
    

    print(f"Тест (==): {equal_acc1.compare_with(equal_acc2)}")
    

    print(f"Тест (self): {rich_acc.compare_with(rich_acc)}")

    
    print("\n--- ПРОВЕРКА ТИПОВ Кто реализует интерфейсы? ---")
    for obj in portfolio:
        printable = " Да" if isinstance(obj, Printable) else " Нет"
        comparable = " Да" if isinstance(obj, Comparable) else " Нет"
        print(f"Счет {obj._acc_id}: Printable={printable}, Comparable={comparable}")

    

    def get_printable_only(items):
        return [i for i in items if isinstance(i, Printable)]

    printable_list = get_printable_only(portfolio)
    print(f"\nИтого найдено объектов для печати: {len(printable_list)}")

    
    compare_all_pairs(portfolio)

if __name__ == "__main__":
    run_demo()
