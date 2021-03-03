import datetime
import math
import time

num = int(input("Введіть десяткове число: "))
ten = num
a = []
while num != 0:
	g = num % 2
	num = num // 2
	a.insert(0,g)
	print(g)

print(a)

num_of_two = 0
for i in range(len(a)):
	num_of_two += a[len(a)-1-i] * (10 ** i)

print(ten,"[10]  =  ",num_of_two,"[2]" )
def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')