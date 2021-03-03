import datetime
import math
import time

while True:
	n = int(input("Кількість цифр карти: "))
	if n == 13:
		break
	else: 
		print("Error!")

print("Введіть номер вашої карти:")
a = []
for i in range(n):
	new_element = int(input(""))			# считываем очередной элемент
	a.append(new_element)					# добавляем его в список                 

sum = 0
for i in range(n-1):
	if i % 2 == 0:
		a[i] *= 1
	else:
		a[i] *= 3
	sum += a[i]

check_digit = 10 - (sum % 10)
if check_digit == a[n-1]:
	print("Your card Good!")
else:
	print("Error, Game over!!!")

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')