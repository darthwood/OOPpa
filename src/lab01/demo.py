from model import Tool, Char, ConstructionSite

def run_demo():
    print(f"{Char.game_world} — ПОЛНОЕ ТЕСТИРОВАНИЕ СИСТЕМЫ")
    print("="*60)
    
    # Функции для тестирования
    def print_header(title):
        print("\n" + "="*60)
        print(title)
        print("="*60)
    
    def test_validation(case, func, *args):
        try:
            func(*args)
            print(f"Провал: {case} - должно было выкинуть ошибку")
        except ValueError as e:
            print(f"Ок: {case} - {e}")
    
    # 1. ТЕСТ ВАЛИДАЦИИ
    print_header("1. Проверка валидации")
    
    print("\n--- Tool ---")
    test_validation("пустое имя", Tool, "", 50)
    test_validation("отрицательная мощность", Tool, "Молоток", -10)
    
    print("\n--- Имя персонажа ---")
    test_cases = [
        ("пустое имя", "", 1, 100, 100),
        ("один символ", "A", 1, 100, 100),
        ("только пробелы", "   ", 1, 100, 100)
    ]
    for desc, name, lvl, hp, iq in test_cases:
        test_validation(desc, Char, name, lvl, hp, iq)
    
    print("\n--- Разряд ---")
    test_cases = [
        ("ноль", "Тест", 0, 100, 100),
        ("семь", "Тест", 7, 100, 100),
        ("минус один", "Тест", -1, 100, 100)
    ]
    for desc, name, lvl, hp, iq in test_cases:
        test_validation(desc, Char, name, lvl, hp, iq)
    
    print("\n--- Здоровье ---")
    test_cases = [
        ("отрицательное", "Тест", 3, -1, 100),
        ("больше ста", "Тест", 3, 101, 100)
    ]
    for desc, name, lvl, hp, iq in test_cases:
        test_validation(desc, Char, name, lvl, hp, iq)
    
    print("\n--- IQ ---")
    test_cases = [
        ("ниже -100", "Тест", 3, 100, -101),
        ("выше 200", "Тест", 3, 100, 201)
    ]
    for desc, name, lvl, hp, iq in test_cases:
        test_validation(desc, Char, name, lvl, hp, iq)
    
    # 2. ПОДГОТОВКА ДАННЫХ
    print_header("2. Подготовка персонажей")
    
    tools = [
        Tool("Ржавый мастерок", 5),
        Tool("Перфоратор Makita", 70),
        Tool("Промышленный робот", 200)
    ]
    
    workers = [
        Char("Петрович", 1, 100, 100, tools[0]),      # новичок
        Char("Михалыч", 6, 90, 150, tools[1]),        # профи
        Char("Колян", 2, 80, -50),                     # в запое
        Char("Димон", 3, 10, 90, tools[0]),            # слабый
        Char("Василич", 5, 100, 180),                   # без инструмента
        Char("Серёга", 3, 100, 19, tools[1])            # пограничный IQ
    ]
    
    names = ["новичок", "профи", "запойный", "слабый", "без инструмента", "пограничный"]
    for i, worker in enumerate(workers):
        print(f"{names[i]}: {worker}")
    
    # 3. ТЕСТ СЕТТЕРОВ
    print_header("3. Проверка граничных значений")
    
    test = Char("Тест", 3, 50, 100)
    print(f"Начало: {test}")
    
    print("\n--- Здоровье ---")
    for val in [-50, 150, 75]:
        test.health = val
        print(f"health = {val:3} -> {test.health}")
    
    # 4. ТЕСТ WORK() - ВСЕ ВЕТВЛЕНИЯ
    print_header("4. Проверка всех вариантов работы")
    
    sites = [
        ConstructionSite("Будка", 30),
        ConstructionSite("Забор", 40),
        ConstructionSite("Сарай", 30),
        ConstructionSite("Туалет", 20),
        ConstructionSite("Небоскреб", 1000)
    ]
    
    # 4.1 Нормальная работа
    print("\n--- Случай 1: IQ >= 20, с инструментом ---")
    sites[0].check_worker(workers[1])  # профи
    
    # 4.2 Без инструмента
    print("\n--- Случай 2: без инструмента ---")
    sites[1].check_worker(workers[4])  # василич
    
    # 4.3 Пограничный IQ
    print("\n--- Случай 3: IQ = 19 ---")
    sites[2].check_worker(workers[5])  # серёга
    
    # 4.4 Отрицательный IQ
    print("\n--- Случай 4: IQ < 0 ---")
    sites[3].check_worker(workers[2])  # колян
    
    # 4.5 Нехватка мощности -> увольнение
    print("\n--- Случай 5: недостаточно мощности ---")
    sites[4].check_worker(workers[0])  # петрович
    
    # 4.6 Работа после увольнения
    print("\n--- Случай 6: попытка работать после увольнения ---")
    workers[0].work()
    
    # 4.7 Повышение уровня
    print("\n--- Случай 7: повышение разряда ---")
    level_up = Char("Карьерист", 5, 100, 150, tools[2])
    for i in range(3):
        print(f"Попытка {i+1}:")
        level_up.work()
        print(f"Уровень: {level_up.level}")
    
    # 5. ТЕСТ ALCOHOL
    print_header("5. Влияние алкоголя")
    
    drunk = Char("Алкоголик", 3, 50, 100)
    print(f"До: {drunk}")
    
    for litres in [1, 2, 3, 5]:
        drunk.drink_vodka(litres)
        print(f"После {litres}л: {drunk}")
    
    # 6. МАГИЧЕСКИЕ МЕТОДЫ
    print_header("6. Магические методы")
    
    # repr
    w = Char("Репа", 4, 70, 120)
    print(f"repr: {repr(w)}")
    
    # str для разных статусов
    print("\n--- str для разных статусов ---")
    statuses = [
        Char("Трезвый", 3, 100, 50),
        Char("Запойный", 3, 100, -10)
    ]
    fired = Char("Уволен", 3, 100, 100)
    fired.fire()
    statuses.append(fired)
    
    for s in statuses:
        print(str(s))
    
    # eq
    print("\n--- eq ---")
    w1 = Char("Один", 3, 100, 100)
    w2 = Char("Один", 3, 50, 50)    # то же имя и уровень
    w3 = Char("Один", 4, 100, 100)   # другой уровень
    w4 = Char("Два", 3, 100, 100)     # другое имя
    
    print(f"w1 == w2: {w1 == w2} (должно быть True)")
    print(f"w1 == w3: {w1 == w3} (должно быть False)")
    print(f"w1 == w4: {w1 == w4} (должно быть False)")
    
    # 7. ТЕСТ УРОНА
    print_header("7. Получение урона")
    
    fighter = Char("Боец", 4, 80, 100)
    print(f"До: {fighter}")
    
    for dmg in [5, 30, 60, 100]:
        fighter.take_damage(dmg)
        print(f"После {dmg} урона: {fighter}")
    
    # 8. ТЕСТ УВОЛЬНЕНИЯ
    print_header("8. Увольнение")
    
    lazy = Char("Лодырь", 2, 100, 80)
    print(f"До: {lazy}")
    print(f"Статус: {lazy.is_fired}")
    
    lazy.fire()
    print(f"После: {lazy}")
    print(f"Статус: {lazy.is_fired}")
    
    # 9. КОМПЛЕКСНЫЙ ТЕСТ
    print_header("9. Полный рабочий день")
    
    worker = Char("Реальный мужик", 3, 100, 120, tools[1])
    sites = [
        ConstructionSite("Ларёк", 30),
        ConstructionSite("Баня", 50),
        ConstructionSite("Коттедж", 80),
        ConstructionSite("Мост", 150)
    ]
    
    for i, site in enumerate(sites, 1):
        print(f"\n--- Объект {i} ---")
        print(f"Состояние: {worker}")
        site.check_worker(worker)
        
        if i % 2 == 0:
            print("Перекур...")
            worker.drink_vodka(2)
    
    print_header("ИТОГ")
    print(f"Финальное состояние: {worker}")

if __name__ == "__main__":
    run_demo()