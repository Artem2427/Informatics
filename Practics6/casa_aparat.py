import datetime
import math
import time

while True:
	print("Введіть решту")
	num = int(input())
	if num >= 0:
		break
		
FIFTY = 0.5
ONE = 1
TWO = 2
FIVE = 5

n = num // FIVE
m = (num - (n * FIVE)) // TWO
c = ((num - (n * FIVE)) - m * TWO) // ONE

print(f"Мінімальна кількість монет\n{n} по 5 грн\n{m} по 2 грн\n{c} по 1 грн\n","Найменша кількість монет", n+m+c)

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')