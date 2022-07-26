import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x, squares)
plt.show()

x = [x for x in range(9)]
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares)
plt.show()

####################
x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1, color=('#00ffff'))  # 設定青色cyan
plt.plot(x, y2, color=('#ff0000'))  # 設定紅色red
plt.show()

######################
d1 = [1, 2, 3, 4, 5, 6, 7, 8]           # data1線條之y值
d2 = [1, 3, 6, 10, 15, 21, 28, 36]      # data2線條之y值
d3 = [1, 4, 9, 16, 25, 36, 49, 64]      # data3線條之y值
d4 = [1, 7, 15, 26, 40, 57, 77, 100]    # data4線條之y值

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(seq, d1, '-', marker='x')
plt.plot(seq, d2, '-', marker='o')
plt.plot(seq, d3, '-', marker='^')
plt.plot(seq, d4, '-', marker='s')
plt.show()

#########################
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

temperature = [23, 22, 20, 24, 22, 22, 23, 20, 17, 18,
               20, 20, 16, 14, 14, 20, 20, 20, 15, 14,
               14, 14, 14, 16, 16, 16, 18, 21, 21, 20,
               16]
x = [x for x in range(1, len(temperature)+1)]
plt.plot(x, temperature)
plt.title("天氣報表", fontsize=24)
plt.xlabel('日期')
plt.ylabel('溫度')
plt.show()

####################
print("以下是matplotlibrc檔案內容")
print(plt.rcParams)
plt.show()
