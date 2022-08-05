import sqlite3
import telebot
import datetime
from telebot import types
import matplotlib.pyplot as plt
import numpy as np
import math


def test_user(message):
    if message == '25':
        userid = 1111
    else:
        userid = message
    return userid

print(test_user(str(25)))
x = [1,2,3,4,5,6,7,8,9]
lst = [(1, '🏠Дом', 10354), (2, '🚙 Автомобиль', 33000), (3, 'Проживание', 1900), (2, '🚙 Автомобиль', 33000), (2, '🚙 Автомобиль', 33000), (3, 'Проживание', 1900), (3, 'Проживание', 1900)]
stronic = math.ceil(len(x) / 2)
y = zip(*[iter(x)]*stronic)
print(len(x), 'всего элементов')
print(stronic, 'страниц')
print(list(y))

list = range(0, len(x))
print(list)
chunk = 5
# Разбиваем список на блоки
[list[i:i + chunk] for i in range(0, len(list), chunk)]





# labels = 'Дом', 'Автомобиль', 'Продукты', 'Прочее', 'Фрукты'
# sizes = [45, 30, 15, 50, 5]
# explode = (0.02, 0.02, 0.02, 0.02)
# print(labels,sizes)
# fig1, ax1 = plt.subplots()
# ax1.barh(labels, sizes)
# # ax1.pie(sizes, labels=labels, explode=explode, shadow=False, startangle=90, counterclock= False, autopct='%.0f%%', wedgeprops=dict(width=0.3))
# #  #      значения, подписи,       отступы,        тень,         поворот,      по часовой стрелке,      проценты,      дырка внутри
# # ax1.axis('equal')
# # ax1.text(0, -0.08, 'Всего:\n100 руб.', horizontalalignment= 'center')
# ax1.text(0,0, f'Создано @YouMoney25\nТвой персональный финансовый бот', fontsize = 6, color = 'red', alpha=0.9, horizontalalignment= 'right')
# #  #                                  текст                                         размер         цвет         прозрачность          выравнивание
# ax1.set_title('Расходы за текущий месяц', fontweight='bold')
# # ax1.legend(loc='upper right', bbox_to_anchor=(1, 1))
# # ax1.set_title('Всего:\n100 руб.', x=0.5, y=0.45)
# plt.show()
 # показать на экране
# plt.savefig('png')
 # сохранить в файл



# attr = dir(datetime)




