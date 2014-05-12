'''
Created on 2014.4.17

@author: YT
'''
import math

def fun(x):
    return x-math.tan(x)

def diff_fun(x):
    return 1 - 1/math.cos(x)**2

def bisection(error_bound=0.0001):
    a = math.pi
    b = math.pi*3/2
    while abs(a-b) >= error_bound:
        c = (a+b)/2
        if fun(c)*fun(a) < 0:
            b = c
        else:
            a = b
            b = c
    print "a = %.5f,b = %.5f"%(a,b)
    print "bisection method: x = %.5f"%b
    
def Newton(error_bound=0.0001):
    x = 4.7
    x_ = x - fun(x)/diff_fun(x)
    while abs(x_-x) >= error_bound:
        x = x_
        x_ = x-fun(x)/diff_fun(x)
    print "newton's method: x = %.5f"%x_

bisection()
print "\n"
Newton()