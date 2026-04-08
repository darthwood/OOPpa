from model import BankAccount, Client
from collection import ClientCollection

def run_collection_test():
    print(f"===$$$ ТЕСТИРОВАНИЕ РЕЕСТРА БАНКА $$$=== \n")

    # 1. Создаем контейнер
    bank_registry = ClientCollection()

    # 2. Наполняем банк клиентами
    users_data = [
        ("Андрей Игоревич", "VIP-777-GOLD", 50000),
        ("Олег Пеньков", "SUN-101-RICH", 1000000),
        ("Иван Должник", "DEBT-666-BAD", -100),
        ("Анна-Николь Профит", "SAVE-999-GOOD", 15000)
    ]

    print("--- ТЕСТ 1: Массовое добавление ---")
   
    for name, acc_id, balance in users_data:
        acc = BankAccount(acc_id, balance)
        client = Client(name, acc)
        bank_registry.add(client)
    
    print(f"В базе сейчас клиентов: {len(bank_registry)}") # Работает благодаря __len__

    print("\n--- ТЕСТ 2: Человеческая итерация (цикл for) ---")

    for client in bank_registry:
        client.show_status()

    print("\n--- ТЕСТ 3: Поиск клиента по ID счета ---")
    
    search_id = "SUN-101-RICH"
    rich_client = bank_registry.get_by_id(search_id)
    if rich_client:
        print(f"Найден клиент: {search_id}. У него на счету {rich_client.account_id}")
    else:
        print(f"Клиент {search_id} не найден!")

    print("\n--- ТЕСТ 4: Удаление клиента ---")
   
    id_to_remove = "DEBT-666-BAD"
    if bank_registry.remove(id_to_remove):
        print(f"Клиент {id_to_remove} успешно изгнан из системы.")
    
    print(f"Осталось клиентов после зачистки: {len(bank_registry)}")

    print("\n--- ТЕСТ 5: Доступ по индексу ---")
    
    try:
        first_client = bank_registry[0]
        print(f"Первый клиент в списке: {first_client.account_id}")
    except IndexError:
        print("База пуста")

    print("\n--- ТЕСТ 6: Строевой смотр get_all ---")
    
    all_clients = bank_registry.get_all()

    print(f"Извлечено объектов: {len(all_clients)}")

    for item in all_clients:
        print(item._Client__name) 

    print("\n--- ТЕСТ 7: Точечный поиск по ID ---")
    res_id = bank_registry.find_by_id("SAVE-999-GOOD")
    print(f"Результат поиска по ID: {res_id._Client__name if res_id else 'Не найден'}")

    print("\n--- ТЕСТ 8: Где Олег? ---")
    
    name_to_find = "Олег Пеньков"
    olegs = bank_registry.find_by_name(name_to_find)
    print(f"По запросу '{name_to_find}' найдено: {len(olegs)} чел.")

    print("\n--- ТЕСТ 9: Поиск первых лиц ---")
   
    vips = bank_registry.find_by_title("VIP")
    print(f"Клиенты в категории VIP: {len(vips)}")
    for v in vips:
        print(f"  > {v._Client__name} [{v.account_id}]")    

    print("\n--- ТЕСТ 10: Сортировка коллекции ---")

    print("Сортировка по балансу (от меньшего к большему):")
    bank_registry.sort(key=lambda c: c._Client__account.balance)
    
    for client in bank_registry:
        print(f" - {client._Client__name}: {client._Client__account.balance}$")

    print("\nСортировка по имени (А-Я):")
    bank_registry.sort(key=lambda c: c._Client__name)
    
    for client in bank_registry:
        print(f" - {client._Client__name}")    

    print("\n--- ТЕСТ 11: Логические фильтры (новые коллекции) ---")
    
    print("Список VIP-клиентов (баланс > 40 000$):")
    rich_clients = bank_registry.get_expensive(40000)
    for c in rich_clients:
        print(f"SSSUPER {c._Client__name} ({c._Client__account.balance}$)")

    print("\nДоступные счета для перевода (баланс >= 0):")
    available = bank_registry.get_available()
    for c in available:
        print(f" <<АКТИВЕН>> {c._Client__name}")

    print(f"\nТип результата get_active: {type(available)}")
    print(f"Всего в базе: {len(bank_registry)}, активных: {len(available)}")    

   
    print("\n=== ТЕСТИРОВАНИЕ КОЛЛЕКЦИИ ЗАВЕРШЕНО ===")

if __name__ == "__main__":
    run_collection_test()


def run_business_scenarios():
    print(f"\n{'='*20} СЦЕНАРИИ РАБОТЫ БАНКА {'='*20}\n")
    
    # Исходные данные
    db = ClientCollection()
    db.add(Client("Андрей", BankAccount("VIP-777", 150000)))
    db.add(Client("Олег", BankAccount("DEBT-001", -500)))
    db.add(Client("Мария", BankAccount("VIP-888", 200000)))
    db.add(Client("Иван", BankAccount("STD-002", 5000)))
    
    print("--- Заморозим Олега для сценария ---") 
    db.find_by_id("DEBT-001").spend_money(60000) 

    print("<<< Сценарий 1: Поиск VIP-клиентов среди активных")
    
    top_active = db.get_active().get_expensive(100000)
    top_active.sort(key=lambda c: c._Client__account.balance, reverse=True)

    for client in top_active:
        print(f"Финалист: {client._Client__name} | Баланс: {client._Client__account.balance}$")


    print("\n<<< Сценарий 2: Выявление должников")
    
    debtors = db.get_available()
    for client in db:
        if client._Client__account.balance < 0:
            print(f"Отправлено SMS: {client._Client__name}, погасите задолженность {client._Client__account.balance}$!")


    print("\n<<< Сценарий 3: Работа с результатами поиска")
    
    found_vips = db.find_by_title("VIP")
    if found_vips:
    
        lucky_client = found_vips[0] 
        print(f"Первый найденный VIP: {lucky_client._Client__name}")
        
        raw_list = found_vips.get_all()
        print(f"Всего в этой категории {len(raw_list)} чел.")


    print("\n<<< Сценарий 4: Закрытие счетов")
    
    print(f"Клиентов до: {len(db)}")
    if db.remove("STD-002"):
        print("Счет STD-002 закрыт.")
    print(f"Клиентов после: {len(db)}")

    print(f"\n{'='*50}")

if __name__ == "__main__":
    run_business_scenarios()
