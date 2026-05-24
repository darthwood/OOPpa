from app import BankApplication 
from exceptions import ClientNotFoundError, DuplicateClientError  

class BankCLI:
    """Лицо нашего банка. Текстовая консоль, которая общается с пользователем."""
    def __init__(self, app: BankApplication) -> None:
        self.app = app  # Привязываем бизнес-логику к интерфейсу

    def print_menu(self) -> None:
        """Печатает на экране варианты действий для пользователя."""
        print("\n" + "="*50)
        print("ДОБРО ПОЖАЛОВАТЬ В БАНК 'ЗОЛОТОЙ НАСОС'")
        print("="*50)
        print("1. Показать всю базу кожаных мешков")
        print("2. Завести новое дело (Добавить клиента)")
        print("3. Объявить банкротом (Удалить клиента)")
        print("4. Найти человека по ID счета")
        print("5. Фильтрация (Показать тех, у кого еще есть деньги)")
        print("6. Сортировка (Перетасовать колоду клиентов)")
        print("0. Свалить в туман (Выход с автосохранением)")
        print("="*50)

    def show_table(self) -> None:
        """Выводит данные в виде аккуратной таблицы."""
        clients = self.app.get_all()  # Берем актуальный список
        if not clients:
            print("В банке пусто. Даже крысы ушли. Добавьте кого-нибудь через пункт 2!")
            return
        # Рисуем красивую шапку таблицы
        print(f"\n| {'Имя клиента':<15} | {'Номер счета':<12} | {'Баланс ($)':<10} |")
        print("-" * 48)
        for c in clients:
            # Выводим форматированные строки 
            print(f"| {c.name:<15} | {c.account.acc_id:<12} | {c.score():<10.2f} |")

    def run(self) -> None:
        """Главный бесконечный цикл меню."""
        while True:
            self.print_menu()  # Показываем менюшку
            try:
                choice = int(input("Выберите пункт меню (0-6): "))  # Просим юзера ткнуть цифру
            except ValueError:
                print("ОШИБКА: Вы ввели буквы! Наш калькулятор понимает только ЧИСЛА!")  # Ловим неверный тип ввода
                continue  # Пинком отправляем в начало цикла

            if choice == 0:
                print("Выходим... Все данные упакованы и отправлены в офшор. Пока!")
                break  # Ломаем цикл, завершаем работу

            elif choice == 1:
                self.show_table()  # Просто распечатываем таблицу

            elif choice == 2:
                # Сценарий добавления
                name = input("Введите имя нового спонсора банка: ")
                acc_id = input("Придумайте ID счета (например, ACC-77): ")
                try:
                    balance = float(input("Сколько денег на счету ($): "))
                    self.app.add_client(name, acc_id, balance)  # Пытаемся добавить через app
                    print(f"Успех! {name} теперь официально спонсирует наш банк.")
                except ValueError:
                    print("ОШИБКА: Сумма баланса должна быть числом!")
                except DuplicateClientError as e:
                    print(f"ПРЕДУПРЕЖДЕНИЕ: {e}")  # Поймали наш собственный эксепшен!

            elif choice == 3:
                # Сценарий удаления с ПОДТВЕРЖДЕНИЕМ опасной операции
                acc_id = input("Введите ID счета несчастного, которого хотим удалить: ")
                confirm = input(f"ВНИМАНИЕ: Вы точно хотите выкинуть счет {acc_id}? (y/n): ")
                if confirm.lower() == 'y':
                    try:
                        self.app.remove_client(acc_id)  # Пробуем удалить
                        print("Стерто! Клиент удален из базы, его деньги ушли директору на кофе.")
                    except ClientNotFoundError as e:
                        print(f"ОШИБКА: {e}")  # Перехватили ошибку отсутствия
                else:
                    print("Операция отменена. Клиент может спать спокойно.")

            elif choice == 4:
                acc_id = input("Введите ID счета для розыска: ")
                client = self.app.find_by_id(acc_id)  # Дергаем поиск из app
                if client:
                    print(f"НАЙДЕН: {client.display()}")  # Показываем ориентировку
                else:
                    print("Хмм... Человек с таким счетом у нас не числится.")

            elif choice == 5:
                try:
                    min_bal = float(input("Показать клиентов с балансом НЕ НИЖЕ ($): "))
                    filtered = self.app.filter_by_balance(min_bal)  # Фрильтруем
                    print(f"\nНайдено клиентов с балансом >= {min_bal}$: {len(filtered)}")
                    for c in filtered:
                        print(f"  -> {c.name} ({c.score()}$)")
                except ValueError:
                    print("ОШИБКА: Баланс должен быть числом!")

            elif choice == 6:
                print("\nКак перетасовать список клиентов?")
                print("1. По алфавиту (по имени)")
                print("2. По богатству (от мажоров к беднякам)")
                try:
                    strat = int(input("Выберите стратегию сортировки (1-2): "))
                    if strat in [1, 2]:
                        self.app.sort_by_strategy(strat)  # Сортируем внутри app
                        print("Вуаля! Список успешно перетасован. Проверьте через пункт 1.")
                    else:
                        print("ОШИБКА: Такой стратегии в нашей методичке нет!")
                except ValueError:
                    print("ОШИБКА: Введите число 1 или 2!")
            else:
                print("❓ Неизвестный пункт меню. Попробуйте еще раз, будьте внимательнее!")
