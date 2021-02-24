import datetime
import math

header = "{:^80}".format("Рахунок-фактура № __ від _____201_р.")
pay = "ПЛАТНИК:ЧП Iванов Iван Iванович"
body = f'''           Узгодження проектноi документацii                услуг             1,00          0,00          0,00
            нового будiвництва за адресою:
            м.Одеса,вул Iванова 986
                                                                                       Всього сума без ПДВ  0,00
                                                                                                      ПДВ   0,00
                                                                                             Всього с ПДВ   0,00
            '''
send = (f'''\n ПОСТАЧАЛЬНИК:Управлiння{pay.rjust(70)}
інженерного захисту територiI мiста та
розвитку узбережжя ОМР Код ЭДРПОУ
24760454 Р/рахунок №35420014002262
МФО 828011 в ГУДКУ в Одеськiй областi
\nПiдстава:\n  №                Найменування товару                       Од.вим            К-сть      Цiна             Сума\n
{body.rjust(100)}\n''')

print(header,send)

def printTimeStamp(name):
   print('Автор програми: ' + name)
   print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Artem')