import runpy
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent

    print("Выберите задание:")
    print("1 - Задание 1")
    print("2 - Задание 2")

    choice = input("Введите номер (1 или 2): ").strip()

    if choice == "1":
        runpy.run_path(str(base_dir / "task1.py"), run_name="__main__")
    elif choice == "2":
        runpy.run_path(str(base_dir / "task2.py"), run_name="__main__")
    else:
        print("Неверный ввод. Запустите снова и введите 1 или 2.")


if __name__ == "__main__":
    main()
