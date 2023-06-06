# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.

# Здесь пишем код
import time
import datetime


def func_log(file_log="log.txt"):
    """
    Декоратор, выполняющий логирование времени выполнения функций
    :param file_log: файл, в котором ведется логирование
    :return:
    """
    def func_log_internal(func):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            return_value = func(*args, **kwargs)
            with open(f"{file_log}", 'a', encoding='utf-8') as file:
                file.write(f"{func.__name__} вызвана {start.strftime('%d.%m %H:%M:%S')}\n")
            return return_value
        return wrapper
    return func_log_internal


@func_log()
def func1():
    """
    Функция, которая отсчитывает 3 секунды
    :return:
    """
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    """
    Функция, которая отсчитывает 5 секунд
    :return:
    """
    time.sleep(5)


func1()
func2()
func1()
