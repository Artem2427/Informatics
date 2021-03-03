import datetime
import math
import time

home = str(input("Введіть ваше місце проживання: "))

while True:
	hours = int(input("Введіть кількість годин, які ви перебуваєте вдома: "))
	if hours > 0:
		if home == "Будинок":
			if hours >= 18:
				print("В’єтнамське порося")
				break
			elif hours >=17 and hours <=10:
				print("Собака")
				break
			else: 
				print("Змія")
				break
		elif home == "Квартира":
			if hours >= 10:
				print("Кішка")
				break
			else:
				print("Хом’як")
				break
		elif home == "Гуртожиток":
			if hours >= 6:
				print("Рибки")
				break
			else:
				print("Мурашник")
				break
		else:
			print("Ви бездомний)))))")
			break
	else:
		print("Введіть коректний час перебування вдома!")

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')