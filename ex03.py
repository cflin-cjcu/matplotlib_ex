import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = 1 / (1 + np.exp(-x))

plt.axhline(y=0, c="blue", ls="--")
plt.axhline(y=0.5, c="red", ls=":")
plt.axhline(y=1.0, c="green", ls="--")
plt.axvline(c="gray", ls="-.")              # 垂直的灰色線條
plt.axline((-2, 0), (2, 1), c='cyan', lw=3)    # 兩個點的連線
plt.axline((-1, 0), slope=0.5, c='y', lw=2)   # 點和斜率的線條
plt.plot(x, y, linewidth=2, c='gray')
plt.xlim(-2*np.pi, 2*np.pi)
plt.show()

################
left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)                  # sin(3*x)函數

plt.plot(x, y)
plt.fill_between(x, 0, y, color='green', alpha=0.1)
plt.show()

########################

x = np.arange(0, 13.3, 0.01)
y = 3 - x
y1 = 17.5 - 2.5 * x
y2 = 8 - 0.6 * x
y3 = np.minimum(y1, y2)  # 取較低值

plt.plot(x, y, color="r", label="3 - x")
plt.plot(x, y1, color="blue", label="17.5 - 2.5x")
plt.plot(x, y2, color="green", label="8 - 0.6x")
plt.ylim(0, 10)
plt.fill_between(x, y, y3, color='yellow')
plt.legend()
plt.show()
################################
# 函數f(x)的係數
a1 = 1
c1 = -2
x = np.linspace(-2, 3, 1000)
y1 = a1*x**2 + c1
plt.plot(x, y1, color='b')      # 藍色是 f(x)

# 函數g(x)的係數
a2 = -1
b2 = 2
c2 = 2
x = np.linspace(-2, 3, 1000)
y2 = a2*x**2 + b2*x + c2
plt.plot(x, y2, color='g')      # 綠色是 g(x)

# 繪製區間
plt.fill_between(x, y1=y1, y2=y2, where=(x >= -1) & (x <= 2),
                 facecolor='yellow')

plt.grid()
plt.show()
