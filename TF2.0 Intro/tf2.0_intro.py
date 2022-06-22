import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0, 10*np.pi, 1000)
y = np.sin(x)


plt.plot(x, y)