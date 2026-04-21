class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} получает {damage} урона. Осталось здоровья: {self.health}")

    def info(self):
        print(self)

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}) | HP: {self.health}, ATK: {self.attack_power}"

    def __add__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return Team(self, other)

    def __lt__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return len(self) < len(other)

    def __eq__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return (
            self.name == other.name
            and self.health == other.health
            and self.attack_power == other.attack_power
            and self.__class__ == other.__class__
        )

    def __len__(self):
        # Боевая сила: здоровье + сила атаки
        return self.health + self.attack_power

    def __bool__(self):
        return self.health > 0


class Warrior(Character):
    def __init__(self, name, health, attack_power, armor=3):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self, other):
        damage = self.attack_power + 2
        print(f"{self.name} (Воин) наносит мощный удар на {damage} урона.")
        other.take_damage(damage)

    def take_damage(self, damage):
        reduced = max(0, damage - self.armor)
        self.health -= reduced
        if self.health < 0:
            self.health = 0
        print(
            f"{self.name} блокирует {self.armor} урона и получает {reduced}. "
            f"Осталось здоровья: {self.health}"
        )


class Mage(Character):
    def __init__(self, name, health, attack_power, mana=50):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, other):
        if self.mana >= 10:
            damage = self.attack_power + 6
            self.mana -= 10
            print(
                f"{self.name} (Маг) использует огненный шар и наносит {damage} урона. "
                f"Мана: {self.mana}"
            )
        else:
            damage = self.attack_power
            print(f"{self.name} (Маг) бьет обычной атакой на {damage} урона. Маны мало.")
        other.take_damage(damage)


class Archer(Character):
    def __init__(self, name, health, attack_power, crit_chance=0.3):
        super().__init__(name, health, attack_power)
        self.crit_chance = crit_chance
        self._crit_toggle = False

    def attack(self, other):
        # Чтобы поведение было предсказуемым: каждый второй выстрел критический
        self._crit_toggle = not self._crit_toggle
        if self._crit_toggle:
            damage = self.attack_power * 2
            print(f"{self.name} (Лучник) попадает в голову! Крит на {damage} урона.")
        else:
            damage = self.attack_power
            print(f"{self.name} (Лучник) стреляет на {damage} урона.")
        other.take_damage(damage)


class Team:
    def __init__(self, *members):
        self.members = list(members)

    def __str__(self):
        names = ", ".join(member.name for member in self.members)
        return f"Команда: {names}"


def create_character():
    print("\n--- Создание персонажа ---")
    print("Классы: 1-Warrior, 2-Mage, 3-Archer")
    choice = input("Выберите класс (1-3): ").strip()
    name = input("Введите имя: ").strip()

    try:
        health = int(input("Здоровье (по умолчанию 50): ") or 50)
        attack = int(input("Сила атаки (по умолчанию 10): ") or 10)
    except ValueError:
        health, attack = 50, 10

    if choice == "1":
        armor = int(input("Броня (по умолчанию 3): ") or 3)
        return Warrior(name, health, attack, armor)
    elif choice == "2":
        mana = int(input("Мана (по умолчанию 50): ") or 50)
        return Mage(name, health, attack, mana)
    elif choice == "3":
        return Archer(name, health, attack)
    else:
        return Character(name, health, attack)


def show_all(characters):
    print("\n--- Вс персонажи ---")
    for i, ch in enumerate(characters, 1):
        status = "жив" if bool(ch) else "мёртв"
        print(f"{i}. {ch} | Статус: {status}")


def battle(characters):
    alive = [ch for ch in characters if bool(ch)]
    if len(alive) < 2:
        print("Нужно минимум 2 живых персонажа!")
        return

    print("\n--- Атака ---")
    for i, ch in enumerate(alive, 1):
        print(f"{i}. {ch.name} ({ch.__class__.__name__})")

    try:
        attacker_idx = int(input("Кто атакует (номер): ")) - 1
        target_idx = int(input("Ког атаковать (номер): ")) - 1
        attacker = alive[attacker_idx]
        target = alive[target_idx]
        attacker.attack(target)
    except (ValueError, IndexError):
        print("Неверный выбор!")


def compare_chars(characters):
    if len(characters) < 2:
        print("Нужно минимум 2 персонажа!")
        return
    show_all(characters)
    try:
        i1 = int(input("Первый персонаж (номер): ")) - 1
        i2 = int(input("Второй персонаж (номер): ")) - 1
        c1, c2 = characters[i1], characters[i2]
        print(f"\n{c1.name} < {c2.name}: {c1 < c2}")
        print(f"{c1.name} == {c2.name}: {c1 == c2}")
        print(f"Боевая сила {c1.name}: {len(c1)}, {c2.name}: {len(c2)}")
    except (ValueError, IndexError):
        print("Неверный выбор!")


def team_up(characters):
    alive = [ch for ch in characters if bool(ch)]
    if len(alive) < 2:
        print("Нужно минимум 2 живых персонажа!")
        return
    show_all(characters)
    try:
        i1 = int(input("Первый для команды (номер): ")) - 1
        i2 = int(input("Второй для команды (номер): ")) - 1
        team = alive[i1] + alive[i2]
        print(team)
    except (ValueError, IndexError):
        print("Неверный выбор!")


def main():
    characters = []
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Создать персонажа")
        print("2. Показать всех")
        print("3. Атаковать")
        print("4. Сравнить персонажей")
        print("5. Создать команду")
        print("0. Выход")

        choice = input("Выбор: ").strip()

        if choice == "1":
            characters.append(create_character())
        elif choice == "2":
            show_all(characters)
        elif choice == "3":
            battle(characters)
        elif choice == "4":
            compare_chars(characters)
        elif choice == "5":
            team_up(characters)
        elif choice == "0":
            break
        else:
            print("Неверный выбор!")

    print("Пока!")


if __name__ == "__main__":
    main()
