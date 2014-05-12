'''
Created on 2014.4.17

@author: YT
'''

#find the solution near x = 2 of function x^3-3*x-1=0 with methods shown below


def fun(x):
    return x**3-3*x-1

def diff_fun(x):
    return 3*x**2-3

def difference_quotient_order2(x,y):
    return (fun(y)-fun(x))/(y-x)

def difference_quotient_order3(x,y,z):
    return ((fun(x)-fun(z)/(x-z))-(fun(y)-fun(z))/(y-z))/(x-y)   

def Newton(error_bounds=0.0001):
    x = 2.
    x_acc = 1.87938524
    while abs(x-x_acc) >= error_bounds:
        x -= fun(x)/diff_fun(x)
    print "newton's method:x = %.5f"%x
    
def Secant_method(error_bounds=0.0001):
    a = 2.
    b = 1.9
    x_acc = 1.87938524
    while abs(b-x_acc) >= error_bounds:
        c = b - fun(b)*(b-a)/(fun(b)-fun(a))
        if abs(c-a) >= abs(c-b):
            a = b
            b = c
        else:
            b = c
    print "secant method:x = %.5f"%b
    
def Parabolic_method(error_bounds=0.0001):
    x_acc = 1.87938524
    x0 = 1
    x1 = 3
    x2 = 2
    while True:
        omiga= difference_quotient_order2(x2,x1)+difference_quotient_order3(x0,x1,x2)*(x2-x1)
        root1 = x2-2*fun(x2)/(omiga+(omiga**2-4*fun(x2)*difference_quotient_order3(x2, x1, x0))**0.5) 
        root2 = x2-2*fun(x2)/(omiga-(omiga**2-4*fun(x2)*difference_quotient_order3(x2, x1, x0))**0.5)
        if abs(root1-x2) >= abs(root2-x2):
            x0 = x1
            x1 = x2
            x2 = root2
        else:
            x0 = x1
            x1 = x2
            x2 = root1
        if abs(x_acc-x2) < error_bounds:
            print "parabolic method:x = %.5f"%x2
            break
    

Newton()
Secant_method()
Parabolic_method()
