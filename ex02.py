import numpy as np
import matplotlib.pyplot as plt

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
plt.plot(squares)
plt.xlim(0, 9)
plt.ylim(0, 70)
plt.show()

######################
x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.xticks(np.arange(0, 7, step=0.5), color='b')
plt.yticks(np.arange(-1, 1.5, step=0.5), color='g')
plt.plot(x, y1, color='c')          # 設定青色cyan
plt.plot(x, y2, color='r')          # 設定紅色red
plt.show()

###########################
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2023, 2024, 2025]                # 年度
labels = ["2023年", "2024年", "2025年"]
plt.xticks(seq, labels)
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='center left')
plt.title("銷售報表", fontsize=24)
plt.xlabel("年度", fontsize=14)
plt.ylabel("數量", fontsize=14)
plt.show()
