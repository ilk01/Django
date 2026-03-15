# Lambda expressions

# def add(a:int, b:int)-> int:
#     return a + b
#
# print(add(5, 6))
#
# func_add = lambda a, b: a + b
# func = add
#
# print(func(68, 78))


def filter_negative(lst: list) -> list:
    negative = []
    for item in lst:
        if item < 0:
            negative.append(item)
    return negative


def my_filter(lst: list, predicate) -> list:
    filtered = []
    for item in lst:
        if predicate(item):
            filtered.append(item)
    return filtered


def isNegative(value):
    return value < 0

def isPositive(value):
    return value > 0

my_list = [1, -2, 3, -4, 5, 6, -7, 8, 9, -10]

# print(filter_negative(my_list))
# print(my_filter(my_list, isNegative))
# print(my_filter(my_list, isPositive))
# print(my_filter(my_list, lambda x: x > 0))

print(list(filter(lambda x: x % 2 == 0, my_list)))

