import json 
import os  
from models import Client, BankAccount  

def save(clients: list[Client], filepath: str) -> None:
    """Превращает живых клиентов в бездушный текст и сохраняет в JSON."""
    data = []  # Заготовка под список словарей
    for client in clients:
        data.append({
            "name": client.name,  # Выковыриваем имя
            "acc_id": client.account.acc_id,  # Выковыриваем ID счета
            "balance": client.account.balance  # Выковыриваем баланс
        })
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # Записываем все это добро в файл с красивыми отступами

def load(filepath: str) -> list[Client]:
    """Воскрешает клиентов из текстового JSON-файла обратно в объекты."""
    if not os.path.exists(filepath):
        return []  # Если файла нет — возвращаем пустой список, начинаем с чистого листа
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)  # Парсим текст в питоновские словари
    clients = []  # Список для воскрешенных объектов
    for item in data:
        acc = BankAccount(item["acc_id"], item["balance"])  # Сначала собираем счет
        clients.append(Client(item["name"], acc))  # Потом упаковываем счет внутрь клиента
    return clients  # Возвращаем готовую банду клиентов наружу
