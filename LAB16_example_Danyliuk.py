import matplotlib.pyplot as plt
import numpy as np

import pylab
def A():
    x = np.linspace(0 , 10 , 51)
    y = 3*x**3-8

    plt.plot(x , y , 'r-' , label='y = 3x^3-8')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True) #сітка

    plt.title('Function graphic')
    plt.legend()

    plt.show()
    plt.savefig('img-12.png' , dpi= 400)


def B():
    x = np.array([1,2,3,4,5])
    y = np.array([122,181,129,95,366])
    pylab.bar(x,y)
    pylab.show()

a = input("A or B ?\n")
if a == 'A' or a == 'a':
    A()
elif a == 'B' or a == 'b':
    B()