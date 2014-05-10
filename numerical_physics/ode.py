'''
Created on 2014.4.18.

@author: YT
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D
from scipy.integrate import odeint
import numpy as np

def fun1(x,y1=0,y2=0,y3=0):
    return -0.013*y1-1000*y1*y2

def fun2(x,y1=0,y2=0,y3=0):
    return -2500*y2*y3

def fun3(x,y1=0,y2=0,y3=0):
    return -0.013*y1-1000*y1*y2-2500*y2*y3

def fun(y1=0.,y2=0.,y3=0.):
    return np.array([-0.013*y1-1000*y1*y2,
                     -2500*y2*y3,
                     -0.013*y1-1000*y1*y2-2500*y2*y3])
    

    

def ode_runge_kutta_order4():
    h = 0.0001
    x = [0]
    y1 = [1]
    y2 = [1]
    y3 = [0]
    while x[-1] <= 0.01:
        k1 = fun1(x[-1],y1[-1],y2[-1],y3[-1])
        l1 = fun2(x[-1],y1[-1],y2[-1],y3[-1])
        m1 = fun3(x[-1],y1[-1],y2[-1],y3[-1])
        k2 = fun1(x[-1]+h/2,y1[-1]+h*k1/2,y2[-1]+h*l1/2,y3[-1]+m1*h/2)
        l2 = fun2(x[-1]+h/2,y1[-1]+h*k1/2,y2[-1]+h*l1/2,y3[-1]+m1*h/2)
        m2 = fun3(x[-1]+h/2,y1[-1]+h*k1/2,y2[-1]+h*l1/2,y3[-1]+m1*h/2)
        k3 = fun1(x[-1]+h/2,y1[-1]+h*k2/2,y2[-1]+h*l2/2,y3[-1]+m2*h/2)
        l3 = fun2(x[-1]+h/2,y1[-1]+h*k2/2,y2[-1]+h*l2/2,y3[-1]+m2*h/2)
        m3 = fun3(x[-1]+h/2,y1[-1]+h*k2/2,y2[-1]+h*l2/2,y3[-1]+m2*h/2)
        k4 = fun1(x[-1]+h,y1[-1]+h*k3,y2[-1]+h*l3,y3[-1]+h*m3)
        l4 = fun2(x[-1]+h,y1[-1]+h*k3,y2[-1]+h*l3,y3[-1]+h*m3)
        m4 = fun3(x[-1]+h,y1[-1]+h*k3,y2[-1]+h*l3,y3[-1]+h*m3)
        y1.append(y1[-1]+h*(k1+2*k2+2*k3+k4)/6)
        y2.append(y2[-1]+h*(l1+2*l2+2*l3+l4)/6)
        y3.append(y3[-1]+h*(m1+2*m2+2*m3+m4)/6)
        x.append(x[-1]+h)
    return x,y1,y2,y3
    

def trapzium():
    h = 0.0001
    x = [0]
    y1 = [1]
    y2 = [1]
    y3 = [0]
    first_time = True
    while x[-1] <= 0.01:
        y1_predictor = y1[-1] + h*fun1(x[-1],y1[-1],y2[-1],y3[-1])
        y2_predictor = y2[-1] + h*fun2(x[-1],y1[-1],y2[-1],y3[-1])
        y3_predictor = y3[-1] + h*fun3(x[-1],y1[-1],y2[-1],y3[-1])
        fun1_evaluation = fun1(x[-1]+h,y1_predictor,y2_predictor,y3_predictor)
        fun2_evaluation = fun2(x[-1]+h,y1_predictor,y2_predictor,y3_predictor)
        fun3_evaluation = fun3(x[-1]+h,y1_predictor,y2_predictor,y3_predictor)
        y1_evaluation = y1[-1] + h*(fun1_evaluation + fun1(x[-1],y1[-1],y2[-1],y3[-1]))/2
        y2_evaluation = y2[-1] + h*(fun2_evaluation + fun2(x[-1],y1[-1],y2[-1],y3[-1]))/2
        y3_evaluation = y3[-1] + h*(fun3_evaluation + fun3(x[-1],y1[-1],y2[-1],y3[-1]))/2

        for i in range(10):
            y1_evaluation = y1[-1] + h*(fun1(x[-1],y1[-1],y2[-1],y3[-1])+
                                        fun1(x[-1]+h,y1_evaluation,y2_evaluation,y3_evaluation))/2
            y2_evaluation = y2[-1] + h*(fun2(x[-1],y1[-1],y2[-1],y3[-1])+
                                        fun2(x[-1]+h,y1_evaluation,y2_evaluation,y3_evaluation))/2
            y3_evaluation = y3[-1] + h*(fun3(x[-1],y1[-1],y2[-1],y3[-1])+
                                        fun3(x[-1]+h,y1_evaluation,y2_evaluation,y3_evaluation))/2

        y1.append(y1_evaluation)
        y2.append(y2_evaluation)
        y3.append(y3_evaluation)
        x.append(x[-1]+h)
    return x,y1,y2,y3
    
    
def plot():
    x,y1,y2,y3 = ode_runge_kutta_order4()
    X,Y1,Y2,Y3 = trapzium()
    fig= plt.figure()
    ax = Axes3D(fig)
    ax.plot(y1,y2,y3,color = "red")
    ax.plot(Y1,Y2,Y3,"b.")
    ax.set_xlabel("y1:red--runge-kutta;blue--trapzium")
    ax.set_ylabel("y2")
    ax.set_zlabel("y3")
    ax.set_title("dy1/dx=-0.013y1-1000y1y2    dy2/dx=-2500y2y3\ndy3/dx=-0.013y1-1000y1y2-2500y2y3")
    plt.show()
    plt.plot(x,y1,'b',label = "y1:runge-kutta")
    plt.plot(X,Y1,'g.',label = "y1:trapzium")
    plt.plot(x,y2,'r',label = "y2:runge-kutta")
    plt.plot(X,Y2,'c.',label = "y2:trapzium")
    plt.plot(x,y3,'y',label = "y3:runge-kutta")
    plt.plot(X,Y3,'k.',label = "y3:trapzium")
    plt.ylim(-0.5,2.8)
    plt.xlim(0,0.011)
    plt.title("dy1/dx=-0.013y1-1000y1y2    dy2/dx=-2500y2y3\ndy3/dx=-0.013y1-1000y1y2-2500y2y3")
    plt.legend()
    plt.show()

plot()
