from scipy import integrate

def fun(x):
    return 1./x

def romberg(err = 1e-5):
    a = 1
    b = 3
    k = 1
    n = 1
    h = b-a
    T = [[h*(fun(a)+fun(b))/2]]
    while True:
        T.append([])
        sum = 0
        for i in range(n):
            sum += h*fun(a+(i+0.5)*h)/2
        T[-1].append(sum+T[-2][0]/2)
        
        for i in range(1,k+1):
            T1 = T[-1][-1]
            T0 = T[-2][i-1]
            T[-1].append(4**i*T1/(4**i-1)-T0/(4**i-1))
        
        if abs(T[-1][-1]-T[-2][-1]) < err:
            break
        else:
            n *= 2
            h /= 2.
            k += 1
    value, err = integrate.quad(fun,a,b)
    print "romberg method: %.6f" % T[-1][-1]
    print "exact value: %.6f" % value
    
def gauss(a=1,b=3):
    def fun1(a,b,t):
        return (b-a)*t/2.+(a+b)/2.
    coefficient = (b-a)/2.
    gauss_3 = coefficient*(5*fun(fun1(a,b,-15**0.5/5))/9+8*fun(fun1(a,b,0))/9+5*fun(fun1(a,b,15**0.5/5))/9)
    gauss_5 = coefficient*(0.2369269*(fun(fun1(a,b,-0.9061798))+fun(fun1(a,b,0.9061798)))
                           +0.4786287*(fun(fun1(a,b,-0.5384693))+fun(fun1(a,b,0.5384693)))+
                           0.5688889*fun(fun1(a,b,0)))
    print "gauss method with 3 points: %.6f" % gauss_3
    print "gauss method with 5 points: %.6f" % gauss_5
    
def Gauss_2(a=1,b=3,n=4):
    def gauss_2(a,b):
        def fun1(a,b,t):
            return (b-a)*t/2.+(a+b)/2.
        coefficient = (b-a)/2.
        gauss2 = coefficient * (fun(fun1(a,b,-0.5773503))+fun(fun1(a,b,0.5773503)))
        return gauss2
    h = (b-a)*1./n
    list = [a+i*h for i in range(n+1)]
    sum = 0
    for i in range(n):
        sum += gauss_2(list[i],list[i+1])
    print "gauss method with 2 points after dividing domain into 4 homogeneous parts: %.6f" % sum
    
romberg()
gauss()
Gauss_2()