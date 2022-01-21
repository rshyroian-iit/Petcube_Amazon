import numpy as np
import pandas as pd
from statistics import mean

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m, b

read_data = pd.read_csv('petcube_sales_numbers.csv', encoding="ISO-8859-1")
frame = [read_data]
df = pd.concat(frame)

names = list(df.ASIN)
#mydata = [list(df.July), list(df.August), list(df.September), list(df.October), list(df.November), list(df.December), list(df.January), list(df.February), list(df.March)]
#mydatam = [list(df.Julym), list(df.Augustm), list(df.Septemberm), list(df.Octoberm), list(df.Novemberm), list(df.Decemberm), list(df.Januarym), list(df.Februarym), list(df.Marchm)]
mydata = [list(df.August), list(df.September), list(df.October), list(df.January), list(df.February), list(df.March)]
mydatam = [list(df.Augustm), list(df.Septemberm), list(df.Octoberm), list(df.Januarym), list(df.Februarym), list(df.Marchm)]
#mydata = [list(df.September), list(df.October)]
#mydatam = [list(df.Septemberm), list(df.Octoberm)]
coordinatessale = []
coordinatesprice = []
comp = 0
for i in range(2, len(mydata[0])):
    a = False
    for j in range(1,len(mydata)):
        if float(mydata[j-1][i]) > 49 and float(mydata[j][i]) > 0:
            price = (float(mydatam[j][i])/float(mydata[j][i]))/(float(mydatam[j-1][i])/float(mydata[j-1][i]))
            prices_value = float(mydatam[j][i])/float(mydata[j][i])
            print(type(prices_value))
            sale = float(mydata[j][i])/float(mydata[j-1][i])
            if abs(price - 1) > 0.05 and (sale > 0.8 and sale < 2):
#                if price > 1 and sale < 1.1:
#                    a = True
#                    coordinatesprice.append(price)
#                    coordinatessale.append(sale)
#                if price < 1 and (sale > 0.9):
#                    a = True
#                    coordinatesprice.append(price)
                    coordinatessale.append(sale)
    if a == True:
        comp +=1              

#for i in range (0, len(coordinatesprice)): print(coordinatesprice[i])
xprice = np.array(coordinatesprice)
ysale = np.array(coordinatessale)
m, b = best_fit_slope_and_intercept(xprice, ysale)

dif = 0
for i in range (0, len(coordinatesprice)): 
    dif += abs(coordinatessale[i] - (m * coordinatesprice[i] + b))
dif = dif / len(coordinatesprice)

print("Number of companies: " + str(comp))                
print("Number of data points: " + str(len(coordinatesprice)))
print("The line of best fit: " + str(m) + " * x + " + str(b))
print("Avarage error: " + str(dif))

#current_price = 200
#company_price = 100
#after_discount = 0.9
#sales_cof = after_discount * m + b
#print(sales_cof)
#profit = sales_cof * (after_discount * current_price - company_price) / (current_price - company_price)
#print(profit)