import datetime
import math

a = int(input("Введіть число а \n"))
b = int(input("Введіть число b \n"))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

def printTimeStamp(name):
   print('Автор програми: ' + name)
   print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Artem')