import datetime
import math
import time

R = 8.314
P = 20 * 10**6
t = 20
T = t + 273.15
V = 12 * 10**(-3)

n = int((P * V) / (R * T))

print(n)

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')






