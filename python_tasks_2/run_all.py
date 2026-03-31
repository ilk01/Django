import runpy
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent

    print("Выберите задание:")
    print("1 - Чистые функции")
    print("2 - Generators")
    print("3 - Closures")
    print("4 - Decorators")
    print("5 - Functions like first-class object")

    choice = input("Введите номер (1-5): ").strip()

    files = {
        "1": "task1_pure_functions.py",
        "2": "task2_generators.py",
        "3": "task3_closures.py",
        "4": "task4_decorators.py",
        "5": "task5_first_class_functions.py",
    }

    selected_file = files.get(choice)
    if not selected_file:
        print("Неверный ввод. Запустите снова и введите число от 1 до 5.")
        return

    runpy.run_path(str(base_dir / selected_file), run_name="__main__")


if __name__ == "__main__":
    main()
