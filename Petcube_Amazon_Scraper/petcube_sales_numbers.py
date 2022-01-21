import numpy as np
import pandas as pd

def takeSecond(elem):
    return elem[1]

read_data = pd.read_csv('petcube_sales_numbers.csv', encoding="ISO-8859-1")
frame = [read_data]
df = pd.concat(frame)

names = list(df.ASIN)
price = list(df.price)
mydata = [list(df.July),list(df.August),list(df.September),list(df.October),list(df.November),list(df.December),list(df.January),list(df.February),list(df.March)]
coeficients = []

for i in range(2, len(mydata[0])):
    maximum = 0
    change = [0,0,0]
    for j in range(1,len(mydata)):
        change[0] = change[1]
        change[1] = change[2]
        if int(mydata[j-1][i]) > 49  and len(price[i]) == 8:
            change[2] = float(mydata[j][i])/float(mydata[j-1][i])
        else:
            change[2] = 0
        summa = change[0] + change[1] + change[2]
        if summa > maximum:
            maximum = summa
    coeficients.append([names[i], maximum, price[i], i])

coef_sort = coeficients
coef_sort.sort(key=takeSecond, reverse = True)
for i in range(10): print(coef_sort[i][2])
result =  []
for i in range(10): 
    result.append([])
    for j in range(0, len(mydata)):
        result[i].append(mydata[j][coef_sort[i][3]])
#for products in result:
    #for sell in products: print(sell)
    #print("   ")




# План
# 1. Определить последний коэфициент всех компаний
# 2. Выбрать топ 10 компаний с найвысшим коэфициентом
# 3. Вывести график этих компаний




