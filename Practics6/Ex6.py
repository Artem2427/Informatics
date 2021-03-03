import datetime
import math
import time

days = int(input("Введіть кількість днів: "))
hours = int(input("Введіть кількість годин: "))
minute = int(input("Введіть кількість хвилин: "))
seconds = int(input("Введіть кількість секунд: "))



all_time = days * 86400 + hours * 3600 + minute * 60 + seconds
print(all_time)

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')