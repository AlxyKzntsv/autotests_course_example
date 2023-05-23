# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    """
    Функция global_function с локальной переменной msg = 1, содержащая в себе функцию local_function
    :return msg: измененная локальная переменная
    """
    msg = 1

    def local_function():
        """
        Локальная функция, изменяющая значение переменной msg на значение 2
        :return:
        """
        nonlocal msg
        msg = 2
    local_function()
    return msg


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
