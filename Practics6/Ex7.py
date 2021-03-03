import datetime
import math
import time

fee = int(input("Введіть початкову суму вкладення: "))
percent = float(input("Введіть річний відсоток: "))/100
year = int(input("Кількість років: "))

your_balance = fee * pow(1+percent,year)
print(round(your_balance,2))
def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')
