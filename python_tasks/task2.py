# Ввод списка целых чисел через пробел
numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
border = int(input("Введите число: "))

# Оставляем только элементы, которые не меньше border
result = []
for value in numbers:
    if value >= border:
        result.append(value)

print("Результат:", result)
