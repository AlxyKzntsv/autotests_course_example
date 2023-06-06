# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    list_sales = file.readlines()
list_purchases = []
purchase = 0
for sale in list_sales:
    if sale != '\n':
        purchase += int(sale.replace('\n', ''))
    else:
        list_purchases.append(purchase)
        purchase = 0
list_purchases.sort(reverse=True)
three_most_expensive_purchases = list_purchases[0] + list_purchases[1] + list_purchases[2]

assert three_most_expensive_purchases == 202346
