import datetime
import math
import time
import string

a = []
while True:
	age = int(input("Введіть свій вік: "))
	
	if age == -1 or age <= 0:
		break
	a.append(age)

print(a)
sum = 0
for i in range(len(a)):
	if a[i] < 3:
		sum += 0
	elif a[i] >= 3 and a[i] <= 12:
		sum += 16 
	elif a[i] >= 60: 
		sum += 18
	else:
		sum += 25 

if len(a) >= 10:
	sum *= 0.9
print(round(sum,2))

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')