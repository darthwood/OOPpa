from model01 import *

def run_full_test():
    print(f"===$$$ ТЕСТИРОВАНИЕ БАНКОВСКОЙ СИСТЕМЫ СТАРТУЕТ $$$=== \n")

    print("\n=== ВНИМАНИЕ! ТЕСТ 1 Валидация Кредита ===")
    try:
        bad_credit = Credit(1000, -5)
    except ValueError as e:
        print(f"Кредит отклонен: {e}")

    print("\n=== ВНИМАНИЕ! ТЕСТ 2 Валидация Счета ===")
    try:
        bad_acc = BankAccount("123", 0)
    except ValueError as e:
        print(f"Аккаунт отклонен: {e}")

    print("\n=== ВНИМАНИЕ! ТЕСТ 3 Валидация Клиента ===")
    try:
        valid_acc = BankAccount("ASS-123456", 1000)
        bad_client = Client("", valid_acc)
    except ValueError as e:
        print(f"Клиент отклонен: {e}")

    print("\n=== ВНИМАНИЕ! ТЕСТ 4 Минус на балансе ===")
    acc = BankAccount("VIP-777-GOLDEN", 5000)
    user = Client("Андрей Игоревич", acc)

    user.spend_money(10000)
    print(acc) #Должен показать что там теперь задолженность -5000 дораров

    print("\n=== ВНИМАНИЕ! ТЕСТ 5 Попытка - не пытка ===")
    user.take_loan(50000, 10.5) #Должен отказать, пока баланс минусовой

    print("\n=== ВНИМАНИЕ! ТЕСТ 6 Депозит и история ===")
    acc.change_balance(20000, "ВЗБЗДНОС   ") #выходим в плюс
    dep = Deposit(10000, 5.0)
    print(f"Создан объект вклада: {repr(dep)}")

    print("\n=== ВНИМАНИЕ! ТЕСТ 7 Ледниковый период ===")
    user.spend_money(70000) # уходим ниже -50000
    print(acc)
    user.spend_money(100) # Выводим что операция не прошла и счет заморожен

    print("\n=== ВНИМАНИЕ! ТЕСТ 8 Сравниваем сущностей ===")
    another_acc = BankAccount("VIP-777_GOLDEN", 0)
    another_user = Client("Андрей Игоревич", another_acc)
    print(f"Клиенты идентичны по номеру счета? {user == another_user}")

    print("\n=== ВНИМАНИЕ! ТЕСТ 9 Защита от умников ===")
    c = Credit(1000, 10)
    try:
        c.rate = -100 # кривая ставка
    except ValueError as e:
        print(f"Внимание! Нарушитель!: {e}")


if __name__ == "__main__":
    run_full_test()

