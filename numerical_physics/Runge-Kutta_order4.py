'''
Created on 2014.4.18

@author: YT
'''

import matplotlib.pyplot as plt
import math


def diff_fun1(x,y):
    return x+y

def diff_fun2(x,y):
    return 3*y/(1+x)

def runge_kutta1():
    h = 0.2
    x = [0]
    y = [1]
    y_real = []
    while x[-1] <= 1:
        k1 = diff_fun1(x[-1],y[-1])
        k2 = diff_fun1(x[-1]+h/2,y[-1]+h*k1/2)
        k3 = diff_fun1(x[-1]+h/2,y[-1]+h*k2/2)
        k4 = diff_fun1(x[-1]+h,y[-1]+h*k3)
        y.append(y[-1]+h*(k1+2*k2+2*k3+k4)/6)
        x.append(x[-1]+h)
    for i in x:
        y_real.append(2*math.exp(i)-1-i)
    plt.plot(x,y,"r*",linewidth=4)
    plt.plot(x,y_real,color = "blue",linewidth=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y'=x+y,y(0)=1,0<x<1")
    plt.xlim(0,1)
    plt.ylim(1,4)
    plt.show()
    
def runge_kutta2():
    h = 0.2
    x = [0]
    y = [1]
    y_real = []
    while x[-1] <= 1:
        k1 = diff_fun2(x[-1],y[-1])
        k2 = diff_fun2(x[-1]+h/2,y[-1]+h*k1/2)
        k3 = diff_fun2(x[-1]+h/2,y[-1]+h*k2/2)
        k4 = diff_fun2(x[-1]+h,y[-1]+h*k3)
        y.append(y[-1]+h*(k1+2*k2+2*k3+k4)/6)
        x.append(x[-1]+h)
    for i in x:
        y_real.append((1+i)**3)
    plt.plot(x,y,"r*",linewidth=4)
    plt.plot(x,y_real,color = "blue",linewidth=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y'=3y/(1+x),y(0)=1,0<x<1")
    plt.xlim(0,1)
    plt.ylim(1,9)
    plt.show()


runge_kutta1()
runge_kutta2()