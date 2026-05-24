import storage  # Подключаем наш файловый склад
from app import BankApplication  # Подключаем бизнес-логику
from cli import BankCLI  # Подключаем интерфейс

DATABASE_FILE = "bank_database.json"  # Имя файла, где будут храниться все наши секреты

def main() -> None:
    """Главная функция, запускающая весь этот финансовый балаган."""
    app_core = BankApplication()  # 1. Создаем мозг системы
    
    # --- ЭТАП: АВТОЗАГРУЗКА ---
    print("Синхронизация с серверами на Каймановых островах...")
    loaded_data = storage.load(DATABASE_FILE)  # Дергаем метод загрузки из JSON
    app_core.set_items(loaded_data)  # Запихиваем воскрешенные данные в мозг
    print(f"База успешно подгружена! Найдено записей: {len(loaded_data)}")
    
    # 2. Создаем и запускаем интерфейс, передавая ему настроенный мозг
    cli_interface = BankCLI(app_core)
    cli_interface.run()  # Код проваливается в бесконечный цикл меню кли.пи
    
    # --- ЭТАП: АВТОСОХРАНЕНИЕ ---
    print("\nСохраняем награбленное... Не выключайте калькулятор...")
    current_data = app_core.get_all()  # Забираем актуальный список клиентов перед закрытием
    storage.save(current_data, DATABASE_FILE)  # Дампим всё в JSON-файл
    print("Все данные успешно сохранены в файл! До новых встреч!")

# Традиционная проверка: запускаем main только если файл кликнули напрямую
if __name__ == "__main__":
    main()
