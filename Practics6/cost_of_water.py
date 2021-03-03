import datetime
import math
import time
CONST = 20

while True:
	num = int(input("Скільки кубометрів ви витратили: "))
	if num > 0:
		break

if num >= 60:
	num -= 60
	cost = CONST + 30 * 9.86 + 20 * 11.22 + 10 * 13.06 + num * 17.89
elif num < 60 and num >= 50:
	num -= 50
	cost = CONST + 30 * 9.86 + 20 * 11.22 + num * 13.06
elif num < 50 and num >= 30:
	num -= 30
	cost = CONST + 30 * 9.86 + num * 11.22
else:
	cost = CONST + num * 9.86

print(round(cost,2), "грн --  ціна за воду ")
def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')