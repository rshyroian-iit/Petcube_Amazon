import numpy as np

price = 200
cost = 95

k = [-0.95, -2.72, -2.48, -5.61, -4.09, -2.03, -2.41, -2.58]
b = [1.74, 3.65, 3.48, 6.72, 5.69, 2.71, 3.46, 3.59]
x = [0, 0, 0, 0, 0, 0, 0, 0]
maxtp = 0

def totalprofit(price, cost, k, b, x):
    A = [0, 0, 0, 0, 0, 0 ,0 ,0]
    X = [0, 0, 0, 0, 0, 0 ,0 ,0]
    X[0] = x[0]
    X[1] = X[0] * x[1]
    X[2] = X[1] * x[2]
    X[3] = X[2] * x[3]
    X[4] = X[3] * x[4]
    X[5] = X[4] * x[5]
    X[6] = X[5] * x[6]
    X[7] = X[6] * x[7]
    A[0] = (k[0] * x[0] + b[0]) * (X[0] * price - (cost + X[0] * price * 0.15)) / ((X[0] / x[0]) * price - (cost + (X[0] / x[0]) * price * 0.15))
    A[1] = (k[1] * x[1] + b[1]) * (X[1] * price - (cost + X[1] * price * 0.15)) / ((X[1] / x[1]) * price - (cost + (X[1] / x[1]) * price * 0.15))
    A[2] = (k[2] * x[2] + b[2]) * (X[2] * price - (cost + X[2] * price * 0.15)) / ((X[2] / x[2]) * price - (cost + (X[2] / x[2]) * price * 0.15))
    A[3] = (k[3] * x[3] + b[3]) * (X[3] * price - (cost + X[3] * price * 0.15)) / ((X[3] / x[3]) * price - (cost + (X[3] / x[3]) * price * 0.15))
    A[4] = (k[4] * x[4] + b[4]) * (X[4] * price - (cost + X[4] * price * 0.15)) / ((X[4] / x[4]) * price - (cost + (X[4] / x[4]) * price * 0.15))
    A[5] = (k[5] * x[5] + b[5]) * (X[5] * price - (cost + X[5] * price * 0.15)) / ((X[5] / x[5]) * price - (cost + (X[5] / x[5]) * price * 0.15))
    A[6] = (k[6] * x[6] + b[6]) * (X[6] * price - (cost + X[6] * price * 0.15)) / ((X[6] / x[6]) * price - (cost + (X[6] / x[6]) * price * 0.15))
    A[7] = (k[7] * x[7] + b[7]) * (X[7] * price - (cost + X[7] * price * 0.15)) / ((X[7] / x[7]) * price - (cost + (X[7] / x[7]) * price * 0.15))
    #print(A)
    prft = A[0] + A[0] * A[1] + A[0] * A[1] * A[2] + A[0] * A[1] * A[2] * A[3] + A[0] * A[1] * A[2] * A[3] * A[4] + A[0] * A[1] * A[2] * A[3] * A[4] * A[5] + A[0] * A[1] * A[2] * A[3] * A[4] * A[5] * A[6] + A[0] * A[1] * A[2] * A[3] * A[4] * A[5] * A[6] * A[7]
    for i in range (0, 8):
        if A[i] < 0:
            prft = 0
    return prft, A, x
bestx = [0, 0, 0, 0, 0, 0, 0, 0]
for i0 in range(75, 85):
    x[0] = 0.5 + i0 * 0.01
    print(i0)
    for i1 in range(45, 55):
        x[1] = 0.5 + i1 * 0.01
        print(i1)
        for i2 in range(50, 55):
            x[2] = 0.5 + i2 * 0.01
            for i3 in range(37, 43):
                x[3] = 0.5 + i3 * 0.01
                for i4 in range(47, 53):
                    x[4] = 0.5 + i4 * 0.01
                    for i5 in range(46, 52):
                        x[5] = 0.5 + i5 * 0.01
                        for i6 in range(52, 57):
                            x[6] = 0.5 + i6 * 0.01
                            for i7 in range(48, 53):
                                x[7] = 0.5 + i7 * 0.01
                                TP, A, _ = totalprofit(price, cost, k, b, x)
                                if maxtp <= TP:
                                    maxtp = TP
                                    Amax = A
                                    bestx = x[:] 
print(Amax)
print(maxtp)
print(bestx) 