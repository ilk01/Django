import runpy
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    runpy.run_path(str(base_dir / "oop_practice.py"), run_name="__main__")


if __name__ == "__main__":
    main()
