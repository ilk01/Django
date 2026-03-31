import random

# Случайный список из 20 целых чисел
numbers = [random.randint(-20, 20) for _ in range(20)]
print("Список:", numbers)

min_positive = None
max_negative = None
count_positive = 0
count_negative = 0
count_zero = 0

for value in numbers:
    if value > 0:
        count_positive += 1
        if min_positive is None or value < min_positive:
            min_positive = value
    elif value < 0:
        count_negative += 1
        if max_negative is None or value > max_negative:
            max_negative = value
    else:
        count_zero += 1

if min_positive is not None:
    print("Минимальный положительный элемент:", min_positive)
else:
    print("Положительных элементов нет")

if max_negative is not None:
    print("Максимальный отрицательный элемент:", max_negative)
else:
    print("Отрицательных элементов нет")

print("Количество отрицательных элементов:", count_negative)
print("Количество положительных элементов:", count_positive)
print("Количество нулей:", count_zero)
