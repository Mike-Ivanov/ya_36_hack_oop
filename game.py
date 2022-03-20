
# Создать класс Вещей
class Thing:
    def __init__(self, name, protect_health, attack, health):
        """Создаем класс вещей ими могут быть предметы одежды."""
        self.protect_health = protect_health
        self.attack = attack
        self.health = health


# Создать класс персонажей
class Person:
    def __init__(self, name, hp, baze_attack, baze_protect_health):
        """Класс персонажей, содержащий в себе следующие параметры"""
        """Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. """
        """Параметры передаются через конструктор"""
        self.name = name
        self.hp = hp
        self.baze_attack = baze_attack
        self.baze_protect_health = baze_protect_health

    # метод, принимающий на вход список вещей set_things(things)
    #
    # метод вычитания жизни на основе входной атаки,
    # а также методы для выполнения алгоритма, представленного ниже


# Создать Класс Паладина
class Paladin(Person):
    def __init__(self, name, hp, baze_attack, baze_protect_health):
        """Класс Паладина, наследуемый от персонажа количество присвоенных"""
        """жизней и процент защиты умножается на 2 в конструкторе"""
        self.hp = hp * 2
        self.baze_protect_health = baze_protect_health * 2


# Создать Класс Воина
class Warrior(Person):
    def __init__(self, name, hp, baze_attack, baze_protect_health):
        """Класс Воина наследуется от персонажа"""
        """атака умножается на 2 в конструкторе."""
        self.baze_attack = baze_attack * 2
        super().__init__(name, hp, baze_attack, baze_protect_health)
