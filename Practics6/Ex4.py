import datetime
import math
import time

while True:
    dish = input("Введіть назву страви: ")
    if dish == "картошка":
        num = int(input("Введіть кількість порцій: "))
        price = 45 * num
        tips = price * 0.14
        fees = price * 0.18
        fprice = price + tips + fees
        print(
            f"Податок: {round(fees,2)}\nЧайові: {round(tips,2)}\nЗаг. сума: {round(fprice,2)} ")
        break
    else:
        print("Такої страни не існує!")
        continue


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Artem')
