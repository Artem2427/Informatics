import datetime
import math
import time

a = [[1, 2, 3], [5, 6,9], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print("{:4d}".format(a[i][j]), end='')
    print("")

def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')