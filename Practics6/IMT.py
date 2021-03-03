import datetime
import math
import time

print(f"Виберіть одниниці вимірювання маси та зросту:\n1  ---  (маса в фунтах, зріст у дюймах)\n2  ---  (маса в кілограмах, зріст у метрах)")
var = int(input("Виберіть цифру:  "))

if var == 1:
	height = float(input("Введіть ваш зріст в дюймах  "))
	weight = float(input("Введіть вашу вагу в футах "))
	imt = float(703 * (weight / (height ** 2)))
	print("IMT =", round(imt,2))
elif var == 2:
	height = float(input("Введіть ваш зріст в м "))
	weight = float(input("Введіть вашу вагу в кг "))
	imt = float(weight / (height ** 2))
	print("IMT =", round(imt,2))
else:
	print("Помилка!")

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')