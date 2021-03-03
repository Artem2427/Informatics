import datetime
import math
import time

vowel = ["a", "e", "i", "o", "u"]

letter = str(input("Введіть букву: "))

if letter in vowel:
	print("Голосна")
elif letter == "y":
	print("Інколи y – голосна, а інколи – приголосна")
else:
	print("Приголосна")

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')