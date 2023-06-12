# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name(start, end=None):
    """
    Генератор, который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    :param start:
    :param end:
    :return:
    """
    if end is None:
        start, end = 0, start
    while start < end:
        a = ''
        for i in range(random.randint(1, 16)):
            a += random.choice(string.ascii_letters)
        a += ' '
        for i in range(random.randint(1, 16)):
            a += random.choice(string.ascii_letters)
        yield a.lower()
        start += 1


gen = generate_random_name(1, 10)
for i in gen:
    print(i)
