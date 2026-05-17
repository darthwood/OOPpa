from model import Client, CreditCard  

class AnnualTaxStrategy:
    """Callable-объект: списывает налог (процент) от текущего баланса клиента."""
    # Призываем налогового инспектора и выдаем ему процентную ставку
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate  # Запоминаем ставку налога

    # Превращает объект класса в киллера балансов 
    def __call__(self, client: Client):
        # Грабим только тех, у кого баланс выше нуля. Минусовые балансы не трогаем
        if client.account.balance > 0:
            tax_amount = client.account.balance * self.tax_rate  # Считаем, сколько откусить
            client.account.change_balance(-tax_amount)  # Безжалостно отнимаем кровные шекели
        return client  # Возвращаем измученного клиента обратно в оборот

# Построить всех по алфавиту
def sort_by_name(client: Client):
    """Стратегия: сортировка по имени клиента."""
    return client.name  # Ключ для сортировки — строка с именем

# Построить всех по толщине кошелька
def sort_by_balance(client: Client):
    """Стратегия: сортировка по балансу счета."""
    return client.account.balance  # Ключ для сортировки — сумма денег

# Сортируем по числу кредитов, а если у них ничья — смотрим, у кого больше денег
def by_credits_and_balance(client: Client):
    """Стратегия сортировки по двум атрибутам: сначала по количеству активных кредитов, затем по балансу."""
    return (client.active_credits_count, client.account.balance)  # Возвращаем кортеж-матрешку для сравнения

# Завод по производству фильтров (Замыкание). Даем планку долга, он собирает кастомного проверяльщика
def make_debt_filter(min_debt: float):
    """Фабрика функций (Замыкание): создает фильтр под заданный порог долга."""
    # Внутренний агент-ищейка, который запомнил min_debt из внешнего мира
    def filter_fn(client: Client):
        # Проверяем, есть ли у клиента вообще кредитная карта, или он зашел погреться
        if isinstance(client.account, CreditCard):
            return client.account.debt >= min_debt  # Если карта есть, проверяем, достаточно ли глубоко он погряз в долгах
        return False  # Обычных работяг без кредитных карт сразу отшиваем
    return filter_fn  # Отдаем настроенного агента-ищейку наружу

# Дополнительный фильтр, чтоб фильтров побольше было
def filter_positive_balance(client: Client):
    """Фильтр: оставляет только клиентов с положительным балансом счета."""
    return client.account.balance > 0  # Пропускает дальше только тех, у кого баланс строго больше нуля
