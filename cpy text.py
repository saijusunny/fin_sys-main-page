import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

dt = 0.100
t = np.arange(dt, 20.0, dt)

ax.semilogx(t, np.exp(-t / 5.0))
ax.grid()

plt.show()