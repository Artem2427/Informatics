import datetime
import math
import time

TH = 75
THS = 112
thing = int(input("Введіть кількість штук: "))
things = int(input("Введіть кількість штукенцій: "))

result = thing * TH + things * THS
print(result)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Artem')
