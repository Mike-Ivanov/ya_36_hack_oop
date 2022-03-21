
# Создать класс Вещей
class Thing:
    def __init__(self, name, protect_health, attack, health):
        """Создаем класс вещей ими могут быть предметы одежды."""
        self.protect_health = protect_health
        self.attack = attack
        self.health = health
        print(f'Создаем новую вещь {name}')


# Создать класс персонажей
class Person:
    def __init__(self, name, baze_hp, baze_attack, baze_protect_health):
        """Класс персонажей, содержащий в себе следующие параметры"""
        """Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. """
        """Параметры передаются через конструктор"""
        self.name = name
        self.hp = baze_hp
        self.baze_attack = baze_attack
        self.baze_protect_health = baze_protect_health
        print(f'Создаем нового персонажа {name}')

    # метод, принимающий на вход список вещей set_things(things)
    def set_things(self, things):
        raise NotImplementedError

    # метод вычитания жизни на основе входной атаки,
    def get_damage(self, damge):
        raise NotImplementedError

    # а также методы для выполнения алгоритма, представленного ниже


# Создать Класс Паладина
class Paladin(Person):
    def __init__(self, name, baze_hp, baze_attack, baze_protect_health):
        """Класс Паладина, наследуемый от персонажа количество присвоенных"""
        """жизней и процент защиты умножается на 2 в конструкторе"""
        super().__init__(name, baze_hp, baze_attack, baze_protect_health)
        self.hp = baze_hp * 2
        self.baze_protect_health = baze_protect_health * 2
        print(f'Создаем нового Паладина {name}')


# Создать Класс Воина
class Warrior(Person):
    def __init__(self, name, baze_hp, baze_attack, baze_protect_health):
        """Класс Воина наследуется от персонажа"""
        """атака умножается на 2 в конструкторе."""
        super().__init__(name, baze_hp, baze_attack, baze_protect_health)
        self.baze_attack = baze_attack * 2
        print(f'Создаем нового Воина {name}')
