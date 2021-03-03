import datetime
import math
import time
BM = 130 # Відбійний молоток
BZ = 106 # Бензинова газонокосарка
BY = 70 # Будильник
TR = 40 # Тиха кімната

num = int(input("Введіть кількість Дб  "))

if num > BM:
	print("Шум перевищує найгучніше значення в таблиці")
elif num == BM:
	print("Відбійний молоток ")
elif num < BM and num > BZ:
	print("Шум розташовується між Відбійним молотком та Бензиновою газонокосаркою")
elif num == BZ:
	print("Бензинова газонокосарка")
elif num < BZ and num > BY:
	print("Шум розташовується між Бензинова газонокосарка та  Будильник")
elif num == BY:
	print("Будильник")
elif num < BY and num >TR:
	print("Шум розташовується між Будильник та Тихою кімнатою")
elif num == BY:
	print("Тиха кімната")

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')