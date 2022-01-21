import numpy as np

#function that calculates the profit
def totalprofit(price, cost, k, b, x):
    A = [0, 0, 0, 0, 0 ,0 ,0]
    X = [0, 0, 0, 0, 0 ,0 ,0]
    X[0] = x[0]
    X[1] = X[0] * x[1]
    X[2] = X[1] * x[2]
    X[3] = X[2] * x[3]
    X[4] = X[3] * x[4]
    X[5] = X[4] * x[5]
    X[6] = X[5] * x[6]
    #profit on September relative to August
    A[0] = (k[0] * x[0] + b[0]) * (X[0] * price - (cost + X[0] * price * 0.15)) / ((X[0] / x[0]) * price - (cost + (X[0] / x[0]) * price * 0.15))
    #profit on October relative to August and so on
    A[1] = (k[1] * x[1] + b[1]) * (X[1] * price - (cost + X[1] * price * 0.15)) / ((X[1] / x[1]) * price - (cost + (X[1] / x[1]) * price * 0.15))
    A[2] = (k[2] * x[2] + b[2]) * (X[2] * price - (cost + X[2] * price * 0.15)) / ((X[2] / x[2]) * price - (cost + (X[2] / x[2]) * price * 0.15))
    A[3] = (k[3] * x[3] + b[3]) * (X[3] * price - (cost + X[3] * price * 0.15)) / ((X[3] / x[3]) * price - (cost + (X[3] / x[3]) * price * 0.15))
    A[4] = (k[4] * x[4] + b[4]) * (X[4] * price - (cost + X[4] * price * 0.15)) / ((X[4] / x[4]) * price - (cost + (X[4] / x[4]) * price * 0.15))
    A[5] = (k[5] * x[5] + b[5]) * (X[5] * price - (cost + X[5] * price * 0.15)) / ((X[5] / x[5]) * price - (cost + (X[5] / x[5]) * price * 0.15))
    #profit on March relative to August
    A[6] = (k[6] * x[6] + b[6]) * (X[6] * price - (cost + X[6] * price * 0.15)) / ((X[6] / x[6]) * price - (cost + (X[6] / x[6]) * price * 0.15))
    #print(A)
    #total profit from September till March relative to the profit in August
    prft = A[0] + A[0] * A[1] + A[0] * A[1] * A[2] + A[0] * A[1] * A[2] * A[3] + A[0] * A[1] * A[2] * A[3] * A[4] + A[0] * A[1] * A[2] * A[3] * A[4] * A[5] + A[0] * A[1] * A[2] * A[3] * A[4] * A[5] * A[6]
    #this loop excludes cases when there is no profit during one of the months
    for i in range (0, 7):
        if A[i] < 0:
            prft = 0
    return prft, A, x

#current price (September)
price = 200

#cost before amazon tax
cost = 95

#coefficients of the relation between the change of price and sale between months from September till March, where the relation is described as sales_change = k * price_change + b
k = [-2.72, -2.48, -5.61, -4.09, -2.03, -2.41, -2.58]
b = [3.65, 3.48, 6.72, 5.69, 2.71, 3.46, 3.59]

#array of the price change relative to the preceding month
x = [0, 0, 0, 0, 0, 0, 0]

#max total profit
maxtp = 0

#the best change of price from month to month 
bestx = [0, 0, 0, 0, 0, 0, 0]

#enumeration of all possible combinations of the price change from month to month
for i0 in range(5, 16):
    #the price change from August to September
    x[0] = 0.5 + i0 * 0.05
    print(i0)
    for i1 in range(5, 16):
        #the price change from September to October and so on
        x[1] = 0.5 + i1 * 0.05
        print(i1)
        for i2 in range(5, 16):
            x[2] = 0.5 + i2 * 0.05
            for i3 in range(5, 16):
                x[3] = 0.5 + i3 * 0.05
                for i4 in range(5, 16):
                    x[4] = 0.5 + i4 * 0.05
                    for i5 in range(5, 16):
                        x[5] = 0.5 + i5 * 0.05
                        for i6 in range(5, 16):
                            #the price change from February to March
                            x[6] = 0.5 + i6 * 0.05
                            #calculation of the profit for a particular combination
                            TP, A, _ = totalprofit(price, cost, k, b, x)
                            if maxtp <= TP:
                                maxtp = TP
                                Amax = A
                                bestx = x[:] 

#output of the results
print(Amax)
print(maxtp)
print(bestx) 