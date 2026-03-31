def greet(name):
    return f"Привет, {name}!"


def loud(text):
    return text.upper()


def process_message(func, message):
    return func(message)


if __name__ == "__main__":
    # Функция как переменная
    say_hello = greet
    print(say_hello("Илькин"))

    # Функция как аргумент другой функции
    print(process_message(loud, "python это удобно"))

    # Функция в списке
    actions = [str.lower, str.upper, str.title]
    word = "pYtHoN"
    for action in actions:
        print(action(word))
