import datetime
import math

a = 5
b = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)
print(a**b)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Artem')
