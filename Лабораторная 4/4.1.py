# TODO решите задачу
import json

def task() -> float:
    """Сумма произведений двух значений в каждом словаре"""
    with open(r'.\input.json', 'r', encoding='utf-8') as file:
        file_ = json.load(file)
    sum_values = 0
    for i in file_:
        sum_values += i['score'] * i['weight']
    return round(sum_values, 3)


print(task())