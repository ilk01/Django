from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(10, 15)
