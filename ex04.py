import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)


plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0.0, np.pi, 100)
plt.subplot(2, 2, 1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(2, 2, 2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(2, 2, 3)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')
plt.show()

#################

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(211)
ax1.plot(x1, np.sin(2*np.pi*x1))
# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(212)
ax2.plot(x2, np.sin(4*np.pi*x2))
plt.show()

#############################

fig, ax = plt.subplots(2)               # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y, 'b')                    # 子圖索引 0
ax[1].plot(x, y, 'g')                    # 子圖索引 1
plt.tight_layout()                      # 緊縮佈局
plt.show()

###################################
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig = plt.figure()
gs = fig.add_gridspec(2, 2)          # 建立 2 x 2 網格

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
gs_ax1 = fig.add_subplot(gs[0, 0])   # 用網格物件索引0,0指定子圖
gs_ax1.plot(x, y, 'b')
gs_ax1.set_title('子圖[0, 0]')
gs_ax2 = fig.add_subplot(gs[0, 1])   # 用網格物件索引0,1指定子圖
gs_ax2.plot(x, y, 'g')
gs_ax2.set_title('子圖[0, 1]')
gs_ax3 = fig.add_subplot(gs[1, 0])   # 用網格物件索引1,0指定子圖
gs_ax3.plot(x, y, 'm')
gs_ax3.set_title('子圖[1, 0]')
gs_ax4 = fig.add_subplot(gs[1, 1])   # 用網格物件索引1,1指定子圖
gs_ax4.plot(x, y, 'r')
gs_ax4.set_title('子圖[1, 1]')

plt.tight_layout()                  # 緊縮佈局
plt.show()

######################################
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "lightyellow"
fig = plt.figure()
x = np.arange(1, 11)
plt.plot(x, x)
plt.title('外圖表')
# 新增子區域位置和大小
left, bottom, width, height = 0.2, 0.6, 0.2, 0.2
# 設定子座標物件
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, x, 'g')
ax2.set_title('內圖表')
plt.show()
