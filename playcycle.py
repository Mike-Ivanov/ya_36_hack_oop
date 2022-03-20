
import random
from game import Thing


# Шаг 1 - создаем произвольное количество вещей с различными параметрами,
# #  процент защиты не должен превышать 10%(0.1). Сортируем по проценту защиты,
#  по возрастанию;
def create_items():
    """Функция создающая вещи"""
    thing_list = []  # Пустой список вещей
    # quantity_of_items = 20
    # Список имен вещей
    thing_names = ['Вещь 1', 'Вещь 2', 'Вещь 3', 'Вещь 4', 'Вещь 5',
        'Вещь 6', 'Вещь 7', 'Вещь 8', 'Вещь 9', 'Вещь 10']

    for i in range(10):
        thing_list.append(Thing(thing_names[i], random.randrange(0, 10, 1), 0, 0))
        i = i + 1

    # thing_list = sorted(thing_list)
    print(thing_list)
    # return items


create_items()


# Шаг 2 - создаем произвольно 10 персонажей,
#  кол-во воинов и паладинов произвольно.
# Имена персонажам тоже рандомные из созданного списка 20 имен.
#  Придумайте своих уникальных персонажей
#  или заставьте сражаться знаменитостей,
#  посмотрим кто сильнее =)
# def create_characters():
#    characters = []
#    names = ['Frodo Baggins','Gandalf the Grey', 'Samwise Gamgee',
#  'Meriadoc Brandybuck', 'Peregrin Took', 'Aragorn',
#            'Legolas', 'Gimli', 'Boromir', 'Sauron', 'Gollum',
#  'Bilbo Baggins', 'Tom Bombadil', 'Elrond',
#             'Arwen Evenstar', 'Galadriel', 'Saruman the White', 'Eomer',
#  'Theoden', 'Eowyn']
#
#    i = 0
#    while i <= 9:
#        choice = random.choice([1, 2])
#        if choice == 1:
#            characters.append(Paladin(names[i], 100, 10, 5))
#       else:
#            characters.append(Warrior(names[i], 100, 10, 5))
#        i += 1
#
#    return characters


# Шаг 3 - одеваем персонажей рандомными вещами.
#  Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;
# def main():
#    characters = create_characters()
#    items = create_items()
#
#    for character in characters:
#        quantity_of_items = random.randrange(1, 4, 1)
#        items_set = []
#        i = 0
#        while i <= (quantity_of_items-1):
#            item_number = random.randrange(0, 20, 1)
#            items_set.append(items[item_number])
#            i += 1
#
#        character.set_things(items_set)


# Шаг 4 - отправляем персонажей на арену,
#  и в цикле в произвольном порядке выбирается пара Нападающий и Защищающийся.

# У Защищающегося вызывается метод
# вычитания жизни на основе атаки (attack_damage) Нападающего.

# Количество получаемого урона рассчитывается
#  по формуле: (attack_damage - attack_damage*finalProtection)

# Общий процент защиты (finalProtection)
# вычисляется по формуле (базовый процент защиты
# + процент защиты от всех надетых вещей)

# Жизнь вычитается по формуле
#  (HitPoints - (attack_damage - attack_damage*finalProtection)),
#  где finalProtection - коэффициент защиты в десятичном виде;

# Цикл идет до тех пор,
# пока не останется последнего выжившего.
# Как только кол-во жизней меньше или равно 0,
#  персонаж удаляется из арены (списка).
#  Для отслеживания процесса битвы выведите информацию
# в таком виде: {атакующий персонаж} наносит удар по
# {защищающийся персонаж} на {кол-во урона} урона
