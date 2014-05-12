'''
Created on 2014.4.17.

@author: YT
'''
#find the solution near x0 = 1.5 of function x^3-x^2-1=0 with the iteration method



def iteration1(error_bounds = 0.0001):
    x = 1.5
    y = 1 + 1/x**2
    change = y - x
    x = y
    while abs(change) >= error_bounds:
        y = 1 + 1/x**2
        change = y - x
        x = y
        if abs(change) > 10:
            print "oops,invalid!"
            change = error_bounds/10
    if change != error_bounds/10:
        print "iteration equation:x(k+1)=1+1/x(k)**2"
        print "x = %.4f"%y
    
def iteration2(error_bounds=0.0001):
    x = 1.5
    y = (1+x**2)**(1./3)
    change = y - x
    x = y
    while abs(change) >= error_bounds:
        y = (1+x**2)**(1./3)
        change = y - x
        x = y
        if abs(change) > 10:
            print "oops,invalid!"
            change = error_bounds/10
    if change != error_bounds/10:
        print "iteration equation:x(k+1)=(1+x**2)**(1./3)"
        print "x = %.4f"%y
    

def iteration3(error_bounds=0.0001):
    x = 1.5
    y = 1./(x-1)**(1./2)
    change = y - x
    x = y
    while abs(change) >= error_bounds:
        y = ((x-1)**(1./2))**(-1)
        change = y - x
        x = y
        if abs(change) > 1:
            print "iteration equation:x(k+1)=1./(x(k)-1)**0.5"
            print "oops,invalid!"
            change = error_bounds/10
    if change != error_bounds/10:
        print "iteration equation:x(k+1)=1./(x(k)-1)**0.5"
        print "x = %.4f"%y
        
iteration1()
iteration2()
iteration3()