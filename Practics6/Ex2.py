import datetime
import math
import time

deg = int(input("Введіть кількість градусів у Цельсія  "))

far = 9/5 * deg + 32
kel = deg + 273

print("\nКельвіна = ", kel)
print("\nФаренгейта = ", far)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Artem')
