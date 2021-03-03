import datetime
import math
import time

# 1 фунт -- 12 дюйм,  1 дюйм -- 2,54 см

height = int(input("Введіть ваш зріст у см  "))

inch = int(height / 2.54)
print(inch)
ip = int(inch / 12)
inch -= ip*12 

print("Твій ріст ", ip,"футів i", inch, "дюймів")


def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')