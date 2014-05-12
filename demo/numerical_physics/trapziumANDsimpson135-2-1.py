from math import pi,sin



def fun1(x):
    return x/(4+x**2)

def fun2(x):
    return x**0.5

def fun3(x):
    return (4-sin(x)**2)**0.5

def integrate1():
    """
    the exact result is In(1.25)/2 = 0.11157177565710488
    """
    n = 8       #divide the domain into 8 parts
    a = 0       #the lower integral limit
    b = 1       #the upper integral limit
    h = (b-a)*1./n
    integral_trapzium = (fun1(a)+fun1(b))*h/2
    integral_simpson = (fun1(a)+fun1(b))*h/6+fun1(a+0.5*h)*2*h/3
    for i in range(1,n,1):
        integral_trapzium += h*fun1(a+i*h)
        integral_simpson += (fun1(a+(i+0.5)*h)*4+fun1(a+i*h)*2)*h/6
    print "\n"
    print "integrate x/(4+x**2) from 0 to 1 with trapzium method: %f" % integral_trapzium   
    print "integrate x/(4+x**2) from 0 to 1 with simpson method: %f" % integral_simpson

def integrate2():
    """
    the exact result is 52/3 = 17.333333333333332
    """
    n = 4       #divide the domain into 8 parts
    a = 1       #the lower integral limit
    b = 9       #the upper integral limit
    h = (b-a)*1./n
    integral_trapzium = (fun2(a)+fun2(b))*h/2
    integral_simpson = (fun2(a)+fun2(b))*h/6+fun2(a+0.5*h)*2*h/3
    for i in range(1,n,1):
        integral_trapzium += h*fun2(a+i*h)
        integral_simpson += (fun2(a+(i+0.5)*h)*4+fun2(a+i*h)*2)*h/6
    print "\n"
    print "integrate x**0.5 from 1 to 9 with trapzium method: %f" % integral_trapzium   
    print "integrate x**0.5 from 1 to 9 with simpson method: %f" % integral_simpson


def integrate3():
    """
    the exact result is 1.0357638697198759
    """
    n = 6       #divide the domain into 8 parts
    a = 0       #the lower integral limit
    b = pi/6       #the upper integral limit
    h = (b-a)*1./n
    integral_trapzium = (fun3(a)+fun3(b))*h/2
    integral_simpson = (fun3(a)+fun3(b))*h/6+fun3(a+0.5*h)*2*h/3
    for i in range(1,n,1):
        integral_trapzium += h*fun3(a+i*h)
        integral_simpson += (fun3(a+(i+0.5)*h)*4+fun3(a+i*h)*2)*h/6
    print "\n"
    print "integrate (4-sin(phi)**2)**0.5 from 0 to pi/6 with trapzium method: %f" % integral_trapzium   
    print "integrate (4-sin(phi)**2)**0.5 from 0 to pi with simpson method: %f" % integral_simpson
integrate1()
integrate2()
integrate3()