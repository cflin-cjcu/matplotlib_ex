import numpy as np
import matplotlib.pyplot as plt

x = [x for x in range(1, 6)]
y = [(y * y) for y in x]
plt.scatter(x, y, color='lightgreen', edgecolor='b', s=60)
plt.show()

###############################
points = 30
x = np.random.randint(1, 11, points)          # 建立 x
y = np.random.randint(1, 11, points)          # 建立 y
colors = np.random.rand(points)             # 色彩數列
size = (30 * np.random.rand(points))**2    # 散點大小數列
plt.scatter(x, y, s=size, c=colors)
plt.xticks(np.arange(0, 12, step=1.0))
plt.yticks(np.arange(0, 12, step=1.0))
plt.show()

##################################

np.random.seed(10)                          # 固定隨機數
N = 50                                      # 散點的數量
r = 0.5                                     # 邊界線boundary半徑
x = np.random.rand(N)                       # 隨機的 x 座標點
y = np.random.rand(N)                       # 隨機的 y 座標點
area = []
for i in range(N):                          # 建立散點區域陣列
    area.append(30)
colorused = ['b', 'c', 'g', 'k', 'm', 'r', 'y']   # 定義顏色
colors = []
for i in range(N):                          # 隨機設定 N 個顏色
    colors.append(np.random.choice(colorused))

area1 = np.ma.masked_where(x < r, area)     # 邊界線 0.5 內區域遮罩
area2 = np.ma.masked_where(x >= r, area)    # 邊界線 0.5 (含)外區域遮罩
# 大於或等於 0.5 繪製星形, 小於 0.5 繪製圓形
plt.scatter(x, y, s=area1, marker='*', c=colors)
plt.scatter(x, y, s=area2, marker='o', c=colors)
# 繪製邊界線
plt.plot((0.5, 0.5), (0, 1.0))                 # 繪製邊界線
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.show()
########################
# ch9_16.py

trials = 2000
Hits = 0
radius = 50
for i in range(trials):
    x = np.random.randint(1, 100)               # x軸座標
    y = np.random.randint(1, 100)               # y軸座標
    if np.sqrt((x-50)**2 + (y-50)**2) < radius:  # 在圓內
        plt.scatter(x, y, marker='.', c='y')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')
plt.axis('equal')
PI = 4 * Hits / trials
print("PI = ", PI)
plt.show()

#################################################

fig = plt.figure()
np.random.seed(10)                      # 設定種子值
N = 100
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 150 * r**2
colors = theta
plt.subplot(projection='polar')
plt.scatter(theta, r, c=colors, s=area, cmap='rainbow', alpha=0.8)
plt.show()
