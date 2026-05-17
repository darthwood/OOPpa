from container import TypedCollection, D, S  
from model_adopted import Client, BankAccount 


if __name__ == "__main__":
    print("================== ЭТАП 1: ТЕСТИРУЕМ ДЖЕНЕРИКИ И ВАЛИДАЦИЮ ТИПОВ ==================")
    
    client_box: TypedCollection[Client] = TypedCollection()
    

    c1 = Client("Анна", BankAccount("ACC-01", 700.0)) 
    c2 = Client("Борис", BankAccount("ACC-02", 1500.0))  
    c3 = Client("Владимир", BankAccount("ACC-03", 50.0))  
    
    
    client_box.add(c1).add(c2).add(c3)
    
    print(f"В сейф успешно забито кожаных мешков: {len(client_box)}")

    print("\n================== ЭТАП 2: ТЕСТИРУЕМ МЕТОДЫ FIND, FILTER, MAP ==================")
    # 1. Проверяем работу find (ищем богача с балансом > 1000)
    rich_bro = client_box.find(lambda c: c.score() > 1000.0)
    print(f"Ищем мажора (>1000$): {rich_bro}")
    
    # Ищем того, кого в нашей базе точно нет
    ghost = client_box.find(lambda c: c.score() > 99999.0)
    print(f"Ищем Илона Макса (>99999$): {ghost} (Никого нет, вернулся честный None)")

    # 2. Проверяем работу filter (отбираем бедных с балансом < 600)
    poop_bros = client_box.filter(lambda c: c.score() < 600.0)
    print(f"Список тех, у кого на счету мышь повесилась (<600$):")
    
    for p in poop_bros:
        print(f"  -> {p.name} ({p.score()}$)") 

    # 3. Проверяем работу map и ДОКАЗЫВАЕМ смену типов
    # Превращаем список клиентов [Client, Client] в список строк [str, str]
    names_list: list[str] = client_box.map(lambda c: c.name)
    print(f"Выкрали только имена через map(): {names_list} | Тип данных: {type(names_list)}")
    
    # Превращаем список клиентов в список чисел list[float]
    balances_list: list[float] = client_box.map(lambda c: c.score())
    print(f"Выкрали только балансы через map(): {balances_list} | Тип данных: {type(balances_list)}")

    print("\n================== ЭТАП 3: ОГНЕННЫЙ ТЕСТ ПРОТОКОЛОВ ==================")
    
    # Сценарий 1: Заставляем коллекцию работать через ограничение bound=Displayable
    # Теперь коробка принимает ВСЁ, у чего есть метод .display()
    display_box: TypedCollection[D] = TypedCollection()
    display_box.add(c1).add(c2)  # Наши клиенты подходят, у них этот метод на месте!
    
    print("Трясем с объектов их рожи по протоколу Displayable:")
    # Циклом вытягиваем все элементы
    for item in display_box.get_all():
        print(item.display())

    # Сценарий 2: Та же самая коллекция, но теперь с ограничением bound=Scorable
    # Коробка резко переобулась и теперь трясет с нас метод .score()
    score_box: TypedCollection[S] = TypedCollection()
    score_box.add(c2).add(c3)  # Подходят, у них скор тоже есть
    
    print("\nТрясем с объектов их балансы по протоколу Scorable:")
    for item in score_box.get_all():
        print(f"Объект слил свой баланс системе: {item.score()}$")
