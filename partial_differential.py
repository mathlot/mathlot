
import numpy as np
import copy
import matplotlib.pyplot as plt

def fun():
    M = 10 #space
    N = 10 #time
    h = 0.1
    v = 1
    tao = 0.1
    t = [0]
    x = [0]
    for i in range(M):
        x.append(x[-1]+h)
    sigma = v*tao/(4*h)
    A = [[1]+[0]*(M-1)]
    for i in range(M-1):
        a = [0]*M
        a[i-1] = -sigma
        a[i] = 1
        a[i+1] = sigma
        A.append(a)
        A.append([0]*(M-1)+[1])

    u = [[1]+[0]*(M-1)]
    while True:
        B = [u[-1][0]]
        for i in range(1,M-1):
            B.append(sigma*u[-1][i-1]+u[-1][i]-sigma*u[-1][i+1])
        B.append(u[-1][-1])
        
        result = fun1(A,B)
        u.append(result)
        t.append(t[-1]+tao)
        if t[-1] > 1:
            break

    plt.plot(x,u[-1])
    plt.show()

def fun1(A,B):
    for i in range(len(A)):
        a = A[i]+B[i]
    row_changed = []
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if abs(a[i][i]) < abs(a[j][i]):
                row = (i,j)
        a[row(0)],a[row(1)] = a[row(1)],a[row(0)]
        row_changed.append(row)
        for j in range(i+1,len(A)):
            factor = a[j][i]/a[i][i]
            for k in range(i+1,len(A)+1):
                a[j][k] = a[j][k] - factor*a[i][k]
    for i in range(len(A)-1,-1,-1):
        for j in range(i-1,-1,-1):
            factor = a[j][i]/a[i][i]
            for k in range(i,len(A)+1):
                a[j][k] = a[j][k] - factor*a[i][k]
    result = []
    for i in range(len(A)):
        result.append(A[i][-1])
    return result