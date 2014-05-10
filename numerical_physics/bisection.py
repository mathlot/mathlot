'''
Created on 2014.4.17

@author: YT
'''
def fun(x):
    return x**2-x-1

def bisection(error_bound=0.05):
    a = 1
    b = 2
    while abs(a-b) >= error_bound:
        c = (a+b)/2.
        if fun(c)*fun(a) < 0:
            b = c
        else:
            a = b
            b = c
    print "bisection method: x = %.3f"%b
    
bisection()