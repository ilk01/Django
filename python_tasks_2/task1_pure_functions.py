def square_list(numbers):
    # Чистая функция: не меняет внешний список, зависит только от аргумента
    return [x * x for x in numbers]


def sum_even(numbers):
    # Чистая функция: всегда один и тот же результат для одного и того же входа
    return sum(x for x in numbers if x % 2 == 0)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    print("Исходный список:", data)
    print("Квадраты:", square_list(data))
    print("Сумма чётных:", sum_even(data))
