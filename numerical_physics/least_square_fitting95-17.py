import matplotlib.pyplot as plt

def fun(a,b,x):
    return a+b*x**2

x = (19,25,31,38,44)
y = (19.0,32.3,49.0,73.3,97.8)
x2_average = 0
x4_average = 0
x2y_average = 0
y_average = 0
length = len(x)
for i in range(length):
    x2_average += x[i]**2*1./length
    x4_average += x[i]**4*1./length
    x2y_average += x[i]**2*y[i]*1./length
    y_average += y[i]/length

b = (x2_average*y_average-x2y_average)/(x2_average**2-x4_average)
a = y_average-b*x2_average
variance = 0
for i in range(length):
    variance += (fun(a,b,x[i])-y[i])**2

list = []
for i in x:
    list.append(fun(a,b,i))
    
print "a = %.6f" % a
print "b = %.6f" % b
print "variance = %.6f" % variance

plt.plot(x,y,'*')
plt.plot(x,list,'b')
plt.show()