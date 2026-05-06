from model import BankAccount, SavingsAccount, CreditCard

ETO_BASA = [
    SavingsAccount("SBER-001", 1000.0, 5.0, 12),
    CreditCard("CRED-777", 0.0, 5000.0, 30),
    SavingsAccount("SBER-002", 5000.0, 7.5, 24),
    BankAccount("USER-99", 100.0) 
]

print("=== 1. ТЕСТ ПОЛИМОРФИЗМА  ===")
for acc in ETO_BASA:
    acc.process() 

print("\n=== 2. ТЕСТ ВЫВОДА (переопределение) ===")
for acc in ETO_BASA:
    print(acc)

print("\n=== 3. ФИЛЬТРАЦИЯ ПО ТИПУ (изинстанс) ===")
def get_only_savings(accounts):
    return [a for a in accounts if isinstance(a, SavingsAccount)]

savings = get_only_savings(ETO_BASA)
print(f"Найдено сберегательных счетов: {len(savings)}")
for s in savings:
    print(f" - {s}")

print("\n=== 4. РАБОТА С ДОЧЕРНИМИ МЕТОДАМИ ===")
for acc in ETO_BASA:
    if isinstance(acc, CreditCard):
        acc.take_loan(1500)
        print(acc)
