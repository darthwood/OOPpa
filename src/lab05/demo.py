from model import Client, BankAccount, SavingsAccount, CreditCard  
from collections import ClientCollection

from strategies import (
    sort_by_name, 
    sort_by_balance, 
    by_credits_and_balance, 
    make_debt_filter, 
    filter_positive_balance,
    AnnualTaxStrategy
)


if __name__ == "__main__":
    
    c1 = Client("Анна", BankAccount("ACC-01", 500.0))  
    c2 = Client("Борис", SavingsAccount("DEP-02", 1500.0, 10.0, 12))  
    c3 = Client("Владимир", CreditCard("CRD-03", 0.0, 5000.0, 55))  
    c4 = Client("Дмитрий", BankAccount("ACC-04", 1200.0))  
    c5 = Client("Елена", BankAccount("ACC-05", 300.0))  

    # Экшен: Владимир кутит на кредитные бабки, Борис лезет в долги при живом вкладе
    c3.account.take_loan(2000.0)  # Владимир загнал карту в долг на 2000$
    c2.take_loan(500.0, 12.0)  # Борис зачем-то взял еще один кредит сверху

    
    collection = ClientCollection()  # Рождаем контейнер
    collection.add(c1).add(c2).add(c3).add(c4).add(c5)  # Нанизываем клиентов на цепочку вызовов
    collection.show("СВЕЖЕПОЙМАННЫЕ КЛИЕНТЫ БАНКА (ПОКА ЕЩЕ СЧАСТЛИВЫЕ)")  # Выводим этот балаган

    print("\n================== СЦЕНАРИЙ 1: КОНВЕЙЕР ЖАДНОСТИ (Filter -> Sort -> Apply) ==================")
    # Запускаем конвейер: фильтруем нищих, сортируем выживших богачей
    chain_result = (
        collection
        .filter_by(filter_positive_balance)  # Шаг 1: Оставляем только тех, у кого баланс > 0 (Владимир с долгами вылетает нахрен)
        .sort_by(sort_by_balance)  # Шаг 2: Сортируем выживших по увеличению их капитала
    )
    chain_result.show("ОТФИЛЬТРОВАЛИ НИЩИХ И ПОСТРОИЛИ БОГАЧЕЙ ПО РОСТУ ИХ НАГЛОСТИ") 
    
    # Шаг 3: Раздаем каждому выжившему по 50 баксов премии через лямбда-микрофункцию
    print("\n[АТТРАКЦИОН ЩЕДРОСТИ]: Банк по ошибке начислил выжившим по +50$... Бежим, пока не отобрали!")
    chain_result.apply(lambda client: client.account.change_balance(50.0))  # Сбросываем вертолетные деньги
    chain_result.show("КОЛЛЕКЦИЯ ПОСЛЕ ТОГО, КАК КЛИЕНТЫ УСПЕЛИ СХВАТИТЬ ПО ХАЛЯВНОЙ ПЯТИДЕСЯТКЕ") 

    print("\n================== СЦЕНАРИЙ 2: КРУЧУ-ВЕРЧУ, ЗАПУТАТЬ ХОЧУ (ВЗАИМОЗАМЕНЯЕМОСТЬ СТРАТЕГИЙ) ==================")
    collection.sort_by(sort_by_name) 
    collection.show("СТРОИМ КЛИЕНТОВ ПО АЛФАВИТУ, КАК НА ШКОЛЬНОЙ ФИЗКУЛЬТУРЕ (sort_by_name)")
    
    collection.sort_by(sort_by_balance, reverse=True)  # Баланс наеборот
    collection.show("ОТ ВИП-МАЖОРОВ К ОБЫЧНЫМ СМЕРТНЫМ (sort_by_balance + reverse)") 
    
    collection.sort_by(by_credits_and_balance)
    collection.show("СОРТИРОВКА ДЛЯ КОЛЛЕКТОРОВ: СНАЧАЛА ПО КОЛИЧЕСТВУ ГРЕХОВ (КРЕДИТОВ), ПОТОМ ПО БАБЛУ")

    print("\n================== СЦЕНАРИЙ 3: ОПЕРАЦИЯ 'ОБДИРАЛОВО' (CALLABLE-ОБЪЕКТ И ЗАМЫКАНИЕ) ==================")
    # Часть А: Проверяем работу нашего фабричного замыкания
    debt_filter_200 = make_debt_filter(200.0)  # Заказываем на фабрике фильтр «ищи долги от 200 баксов»
    debtors_collection = collection.filter_by(debt_filter_200)  # Натравливаем полученный фильтр на коллекцию
    debtors_collection.show("СПИСОК ЖЕРТВ ДЛЯ ОБЗВОНА В 3 ЧАСА НОЧИ (Долг по кредитке >= 200$)")  # В капкане должен быть один Владимир

    # Часть Б: Проверяем работу класса-функции
    tax_processor = AnnualTaxStrategy(tax_rate=0.10)  # Создаем налоговика, готового откусить 10% от баланса
    print("\n[ВНИМАНИЕ]: Налоговая инспекция зашла в чат. Списываем 10% за воздух со всех плюсовых балансов...")  # Православный лог
    collection.apply(tax_processor)  # Засовываем объект вместо обычной функции в метод .apply()
    collection.show("РЕЗУЛЬТАТ ВИЗИТА НАЛОГОВОЙ (У КРИЗИС-МЕНЕДЖЕРА БАНКА НОВАЯ ЯХТА)")

    print("\n================== ДОПОЛНИТЕЛЬНО: ПРОВЕРКА MAP И REDUCE ==================")
    # Демонстрируем метод map_to_list: выковыриваем из клиентов только их имена
    client_names = collection.map_to_list(lambda client: client.name)  # Потрошим коллекцию через лямбду
    print(f"🕵️‍♂️ Выкрали чистый список имен кожаных мешков (через map_to_list): {client_names}")

    # Демонстрируем метод reduce_to_value: схлопываем всю коллекцию в одно число
    total_bank_cash = collection.reduce_to_value(
        lambda acc, client: acc + (client.account.balance if client.account.balance > 0 else 0), 
        initial=0.0
    )  # Считаем бабло. Если у клиента на балансе минус, то плюсуем 0, чтобы не портить общую кассу
    print(f"💰 Сколько реального бабла лежит в нашем сейфе (сумма всех плюсовых балансов через reduce_to_value): {total_bank_cash}$")  # Куш
