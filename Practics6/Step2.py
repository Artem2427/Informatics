import datetime
import math

name = "Мене звати Данько Артем Русланович."
age = "Мені 17 років"
print(name + age)


def printTimeStamp(name):
   print('Автор програми: ' + name)
   print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Artem')