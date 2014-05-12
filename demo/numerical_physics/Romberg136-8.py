
from math import pi, sin, exp
from scipy import integrate
def fun(x,l):
    if l not in [0,1,2]:
        print "l must be 0,1 or 2!"
    elif l == 0:
        return 2*exp(-x)/pi**0.5
    elif l == 1:
        return x*sin(x)
    elif l == 2:
        return x**(1+x**2)**0.5

def romberg(err = 1e-5,a=0,b=1,l=0):
    n = 1
    h = b - a
    k = 1
    T = [[h*(fun(a,l)+fun(b,l))/2]]
    while True:
        T.append([])
        sum = 0
        for i in range(n):
            sum += h*fun(a+(i+0.5)*h,l)/2
        T[-1].append((sum+T[-2][0]/2))    #solve the first element at the kth row
        
        for i in range(k):  #find other elements at the kth tow
            j = i+1
            T1 = T[-1][-1]
            T0 = T[-2][i]
            T[-1].append((4**j)*T1/(4**j-1)-T0/(4**j-1))
        if abs(T[-1][-1]-T[-2][-1]) < err and len(T) > 2:
            break
        else:
            k += 1
            h /= 2.
            n *= 2
    result,err = integrate.quad(fun,a,b,args=(l,))
    if l == 0:
        print "integrate 2*exp(-x)/pi**0.5 from 0 to 1"
        print "romberg method: %.6f" % T[-1][-1]
        print "exact value: %.6f" % result
    elif l == 1:
        print "integrate x*sin(x) from 0 to 2*pi"
        print "romberg method: %.6f" % T[-1][-1]
        print "exact value: %.6f" % result
    elif l == 2:
        print  "integrate x*(1+x**2)**0.5 from 0 to 3"
        print "romberg method: %.6f" % T[-1][-1]
        print "exact value: %.6f" % result
    print "\n"
    
        
romberg(a=0,b=1,l=0)
romberg(a=0,b=2*pi,l=1)
romberg(a=0,b=3,l=2)
        

        
