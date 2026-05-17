class BankAccount:
    # Рожаем базовый счет: нужен ID, чтоб налоговая нашла, и баланс, чтоб было что списывать
    def __init__(self, acc_id: str, balance: float):
        self._acc_id = acc_id  # Прячем ID за одно подчеркивание, типа мы эксперты в приватности
        self._balance = balance  # Баланс тоже прячем. Меньше видят — крепче спят

    @property
    # Разрешаем позырить на ID счета, но руками не трогать!
    def acc_id(self):
        return self._acc_id  # На, посмотри, жалко что ли

    @property
    # Позволяем клиенту всплакнуть, глядя на свой баланс
    def balance(self):
        return self._balance  # Показываем циферки на экране

    # Главный метод любого банка: пополнение или грабеж
    def change_balance(self, amount: float) -> bool:
        # Если клиент пытается уйти в суровый минус, включаем режим жадности
        if self._balance + amount < 0:
            return False  # Сорри, бро, ты нищий для этой операции, отмена
        self._balance += amount  # Если все ок, меняем баланс 
        return True  # Машем ручкой и говорим, что все прошло успешно

    # Как счет выглядит в консоли (чтобы не смотреть на унылый адрес в памяти <object at 0x...>)
    def __str__(self):
        return f"Счет {self._acc_id} | Баланс: {self._balance}$"  # Выдаем красивую строчку

    # Ритуал базовой проверки. Пока ничего не делает, но выглядит солидно
    def process(self):
        print(f"--- Базовая проверка счета {self._acc_id} ---")  # Имитируем бурную деятельность


class SavingsAccount(BankAccount):
    # Копируем обычный счет, но добавляем обещания легких денег
    def __init__(self, acc_id: str, balance: float, interest_rate: float, term_months: int):
        super().__init__(acc_id, balance)  # Пинком отправляем ID и баланс старшему классу BankAccount
        self.interest_rate = interest_rate  # Запоминаем процент
        self.term_months = term_months  # Запоминаем, сколько месяцев нельзя трогать заначку

    # Насыпаем клиенту копеечку со щедрого барского
    def apply_interest(self):
        bonus = self._balance * (self.interest_rate / 100)  # Считаем сумму халявы
        self.change_balance(bonus)  # Кидаем эти центы на счет
        return bonus  # Возвращаем сумму бонуса, чтоб было чем хвастаться

    # Особая магия для вкладов
    def process(self):
        super().process()  # Сначала делаем вид, что просто проверяем счет
        bonus = self.apply_interest()  # Бабах! Начислили проценты
        print(f"Начислены проценты: +{bonus}$")  # Радуем клиента (или бесим, если там 7 рублей, как у меня)

    # Печать вклада на экране
    def __str__(self):
        return f"Денег на депозите: {super().__str__()} | Ставка: {self.interest_rate}%"  # Склеиваем инфу в кучу


class CreditCard(BankAccount):
    # Самый прибыльный инструмент банка: кредитка с лучшими условиями
    def __init__(self, acc_id: str, balance: float, credit_limit: float, grace_period: int):
        super().__init__(acc_id, balance)  # Скидываем базу родителю
        self.credit_limit = credit_limit  # Сколько денег клиент может просадить в баре за наш счет
        self.grace_period = grace_period  # Дни, когда мы притворяемся добрыми и не берем проценты
        self.debt = 0.0  # Изначально ловушка захлопнута, долг на нуле

    # Метод «Залезть в долги по уши»
    def take_loan(self, amount):
        #Проверяем, не обалдел ли клиент и не превысил ли суммарный лимит карты
        if self.debt + amount <= self.credit_limit:
            self.debt += amount  # Увеличиваем его личный сорт долгового ада
            self.change_balance(amount)  # Докидываем виртуальные баксы на карту
            print(f"Кредит на {amount}$ получен")  # Пишем, что сделка с дьяволом совершена
        else:
            print("Превышен лимит!")  # Губозакаточную машинку этому господину, лимит исчерпан!

    # Проверка кредитки (время грабить)
    def process(self):
        super().process()  # Проверяем базовые штуки
        # Если на бедолаге висит долг, врубаем скрытые комиссии
        if self.debt > 0:
            fee = self.debt * 0.05  # Снимаем скромные 5%
            self.change_balance(-fee)  # Списываем комиссию прямо с карты себе в карман
            print(f"Удержана комиссия за кредит: -{fee}$")  # Радуем клиента уведомлением

    # Как напечатать кредитку и не заплакать
    def __str__(self):
        return f"Кредит: {super().__str__()} | Долг: {self.debt}$"  # Показываем клиенту смысл ходить на работу


class Credit:
    # Микро-блокнот для записи кредитов
    def __init__(self, amount: float, rate: float):
        self.amount = amount  # Сколько этот смертный у нас занял
        self.rate = rate  # Под какой процент мы ему это впарили


class Client:
    # Создаем работягу
    def __init__(self, name: str, account: BankAccount):
        self.__name = self._validate_name(name)  # Проверяем имя и защищаем от хакеров
        self.__account = account  # Привязываем кошелек к человеку и тоже замуровываем
        self.__credits = []  # Тут будут лежать обычные кредиты 
        self.__deposits = []  # Тут вклады 

    @property
    # Подглядываем за счетом клиента извне
    def account(self):
        return self.__account  # Отдаем объект кошелька

    @property
    # Узнаем, как зовут этого несчастного
    def name(self) -> str:
        return self.__name  # Выдаем имя

    @property
    # Быстрый способ узнать номер счета, не ковыряясь в чужих карманах напрямую
    def account_id(self):
        return self.__account.acc_id  # Выдает номер акка
    @property
    # Считаем, сколько раз клиент уже подписывал кредитный договор
    def active_credits_count(self) -> int:
        return len(self.__credits)  

    # Метод борьбы с анонимусами
    def _validate_name(self, name):
        # Если вместо имени прислали пустоту
        if not name:
            raise ValueError("Пустое значение!")  # Закатываем истерику
        return name  

    # Оформление классического кредита
    def take_loan(self, amount: float, rate: float):
        # Если у клиента на счету уже шкила в сокс играет
        if self.__account.balance < 0:
            print(f"{self.__name}, необходимо сначала погасить задолженность {self.__account.balance}$!")  # Шлем в кассу
        else:
            new_credit = Credit(amount, rate)  
            self.__credits.append(new_credit)  
            self.__account.change_balance(amount)  
            print(f"Кредит одобрен. Деньги поступили на счет. Текущий баланс: {self.__account.balance}$")  

    # Метод «Ни в чем себе не отказывай» 
    def spend_money(self, amount: float):
        print(f"Попытка оплаты на {amount}$...")  # Пишем лог, пока терминал на кассе думает
        # Пробуем списать
        if not self.__account.change_balance(-amount):
            print(f"Транзакция отклонена! Недостаточно средств.")

    # Показать всю подноготную клиента
    def show_status(self):
        print(f"\n{self.__account}")  # Печатаем состояние его кошелька
        print(f"Долгов по кредитам: {len(self.__credits)}")  # Палим количество кредитов

    # Сравниваем двух клиентов через `==`. Ибо люди равны, только если у них одинаковые ID счетов
    def __eq__(self, other):
        # Если нам подсунули для сравнения кота или кирпич вместо клиента
        if not isinstance(other, Client):
            return False  # Сразу говорим, что это не наш пассажир
        return self.__account.acc_id == other.__account.acc_id  # Равны, если номера карт совпали (мистика!)

    # Текстовый образ клиента для вывода на экран
    def __str__(self):
        return f"Клиент: {self.__name} | {self.__account}"  # Склеиваем имя и его финансовые страдания
