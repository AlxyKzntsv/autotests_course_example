# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII
def to_roman_one_char(number, digit):
    """
    :param number: цифра, которую надо представить в виде римской 
    :param digit: разряд, позиция в числе (степень десяти: единицы - 0, десятки - 1 и тд )
    :return: строка в римском стиле, соответствующая цифре и разряду
    """
    roman_digits = (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M', 'V|', 'X|'))
    # для 5000 и 10000 условно взял значения, правильно их обозначить через Х и V c полосой сверху
    match number:
        case 0:
            return ''
        case 1:
            return roman_digits[digit][0]
        case 2:
            return roman_digits[digit][0]+roman_digits[digit][0]
        case 3:
            return roman_digits[digit][0]+roman_digits[digit][0]+roman_digits[digit][0]
        case 4:
            return roman_digits[digit][0]+roman_digits[digit][1]
        case 5:
            return roman_digits[digit][1]
        case 6:
            return roman_digits[digit][1]+roman_digits[digit][0]
        case 7:
            return roman_digits[digit][1]+roman_digits[digit][0]+roman_digits[digit][0]
        case 8:
            return roman_digits[digit][1]+roman_digits[digit][0]+roman_digits[digit][0]+roman_digits[digit][0]
        case 9:
            return roman_digits[digit][0]+roman_digits[digit][2]
        case _:
            return ''


def to_roman(val):
    """
    :param val: арабское число (int)
    :return: римское число (str)
    """
    roman_str = ''
    for i in enumerate(str(val)):
        roman_str += to_roman_one_char(int(i[1]), len(str(val)) - i[0] - 1)
    # print(val, ' = ', roman_str)
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
