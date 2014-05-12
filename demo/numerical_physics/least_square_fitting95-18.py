import matplotlib.pyplot as plt
from math import exp

x = tuple(range(0,60,5))
y = (0.,1.27e-4,2.16e-4,2.86e-4,3.44e-4,3.87e-4,4.15e-4,4.37e-4,4.51e-4,4.58e-4,4.62e-4,4.64e-4)

x1_ = 0
x2_ = 0
x3_ = 0
x4_ = 0
x5_ = 0
x6_ = 0
y_ = 0
xy_ = 0
x2y_ = 0
x3y_ = 0

length = len(x)
for i in range(length):
    x1_ += x[i]*1./length
    x2_ += x[i]**2*1./length
    x3_ += x[i]**3*1./length
    x4_ += x[i]**4*1./length
    x5_ += x[i]**5*1./length
    x6_ += x[i]**6*1./length
    y_ += y[i]/length
    xy_ += y[i]*x[i]/length
    x2y_ += x[i]**2*y[i]/length
    x3y_ += x[i]**3*y[i]/length

A = [[x6_,x5_,x4_,x3_,x3y_],[x5_,x4_,x3_,x2_,x2y_],
     [x4_,x3_,x2_,x1_,xy_],[x3_,x2_,x1_,1.,y_]]
length = len(A)
for i in range(length):
    for j in range(i+1,length):
        factor = A[j][i]/A[i][i]
        for k in range(i,length+1):
            A[j][k] -= A[i][k]*factor

for i in range(length-1,-1,-1):
    for j in range(i-1,-1,-1):
        factor = A[j][i]/A[i][i]
        for k in range(i,length+1):
            A[j][k] -= A[i][k]*factor

a = A[0][-1]/A[0][0]
b = A[1][-1]/A[1][1]
c = A[2][-1]/A[2][2]
d = A[3][-1]/A[3][3]

def fun(x):
    return a*x**3+b*x**2+c*x+d

y_fitting = []
for i in x:
    y_fitting.append(fun(i))

variance = []
for i in x:
    variance.append(y[x.index(i)]-fun(i))

variances = sum(variance)

plt.plot(x,y,'r',label = "data")
plt.plot(x,y_fitting,'b',label = 'least square fitting')
plt.plot(x,variance,'g',label = "variance")
plt.xlabel('time:t/s')
plt.ylabel('density:y')
plt.legend()

print "leat square fitting method:a*x**3+b*x**2+c*x+d"
print "a = %.6f ; b = %.6f ; c = %.6f ; d = %.6f" % (a,b,c,d)
print "variances with this method: %.6f" % variances
plt.show()
