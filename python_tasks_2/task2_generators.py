def even_numbers(limit):
    current = 0
    while current <= limit:
        if current % 2 == 0:
            yield current
        current += 1


if __name__ == "__main__":
    n = int(input("Введите верхнюю границу: "))
    print("Чётные числа:")
    for value in even_numbers(n):
        print(value, end=" ")
    print()
