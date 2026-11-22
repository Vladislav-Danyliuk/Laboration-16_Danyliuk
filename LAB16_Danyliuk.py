import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10 , 10)
y = np.sin(0.4*x) + 0.1*x

plt.plot(x , y , 'r-' , label='y=sin0.4x + 0.1x')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
plt.savefig('x.png')