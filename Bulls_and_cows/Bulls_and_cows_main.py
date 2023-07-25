import random as r
import sys


def printmeaning(word: str) -> None:
    """ Выводит на экран значение слова из файла со словарем значений. """
    with open('russian_nouns_with_definition.txt', encoding='utf-8') as znach:
        for i in znach.readlines():
            if i.startswith(word):
                print(i.strip())
                break


dlina = int(input('''Из скольки букв мне загадать слово? 
Введи цифру от 3 до 10 и нажми 'Enter': '''))

with open('russian_nouns.txt', encoding='utf-8') as d:
    l = [i.strip().lower() for i in d.readlines() if len(i.strip()) == dlina]

x = r.choice(l)
hod = 0

print(f'''\n\nПривет, Друг!!! Я готов сыграть с тобой в игру "Быки и коровы".
Я загадал слово из {dlina} букв. Чтобы попробовать отгадать мое слово, введи существующее слово из {dlina}
букв и нажми "Enter", а я скажу: сколько в нем "Быков" и "Коров".(Бык = буква есть в моем слове на том же месте.
Корова = буква есть в слове, но на другом месте.\nВ игре доступны команды: "сдаюсь" и "покажи словарь")\n''')

while (move := input('Введи слово:  ').lower()) != x:
    if move == 'сдаюсь':
        print(f'Ладно,ладно! Это было слово: "{x}"')
        printmeaning(x)
        sys.exit()
    if move == 'покажи словарь':
        print(l)
        continue
    if hod == 7:
        print('Может попросишь кого-то помочь тебе?!')
    b = 0
    k = 0
    tm = x
    hod += 1
    prp = set()
    if len(move) != dlina:
        print(f'В твоем слове неверное количество букв! Введи слово из {dlina} букв)))')
        continue
    elif move not in l:
        print(f"Такого слова: '{move}' нет в моем словаре! Я его не загадывал. Попробуй другое слово.")
        continue
    else:
        for i in range(dlina):
            if move[i] == tm[i]:
                b += 1
                tm = tm.replace(move[i], '*', 1)
                prp.add(i)
        for i in range(dlina):
            if i in prp:
                continue
            if move[i] != tm[i] and move[i] in tm:
                k += 1
                tm = tm.replace(move[i], '*', 1)
        print(f"В слове '{move}' быков: {b} шт., коров: {k} шт. ")
print(f'Вау!Это, действительно, слово "{x}". Поздравляю!\n')
printmeaning(x)
