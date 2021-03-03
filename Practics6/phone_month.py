import datetime
import math
import time

MI = 200
SE = 50
PEN = 1.44
STAND = 45
v = 0
minute = int(input("Введіть кількість витрачених хвилин за місяць:  "))
sms = int(input("Кількість повідомлень за місяць:  "))

if minute <= MI and sms <= SE:
	print(STAND, "грн базова плата за користування, без внесків та податків")
	all_price = STAND + PEN + 0.05 * STAND
	print(round(all_price,2),"грн - загальна сума")
else:
	if minute > MI:
		num = minute - MI
	if sms > SE:
		sms = int(sms - SE)
		v = sms
	print(STAND, "грн базова плата за користування, без внесків та податків")
	all_price = STAND + PEN + 0.05 * STAND + num*0.27 + v * 0.5
	print(round(all_price,2),"грн - загальна сума")
def printTimeStamp(name):
	print('Автор програми: ' + name)
	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Artem')