import random

def get_numbers_ticket(min_num, max_num, quantity):
    
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num+1):     # Перевірка вхідних параметрів
        return []
    
    numbers = set()                                                # Генерування унікальних чисел у заданому діапазоні
    while len(numbers) < quantity:
        num = random.randint(min_num, max_num)
        numbers.add(num)
    
    return sorted(list(numbers)) 
lottery_numbers = get_numbers_ticket(34, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)
