import datetime
import math
import time

FRESH_BREAD = 8.5

num = int(input("Скільки вам буханок вчорашнього хліба? "))

discount = float(FRESH_BREAD *0.6)
total_cost = float(discount * num)

print(f"Початкова вартість: {round(FRESH_BREAD,2)}\nСкидка: {round(discount,2)}\nЗагальна вартість {round(total_cost,2)} ")


def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')
