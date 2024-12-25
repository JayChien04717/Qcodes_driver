import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初始化 2D 陣列，假設有 100 筆資料，每筆資料長度為 50
num_measurements = 100
data_length = 50
data_2d = np.zeros((num_measurements, data_length))

# 設置即時繪圖
fig, ax = plt.subplots()
im = ax.imshow(data_2d, aspect='auto', cmap='viridis')

def update_data(new_data, i):
    # 更新 2D 陣列的第 i 行
    data_2d[i] = new_data
    
    # 更新圖像數據
    im.set_array(data_2d)
    plt.draw()
    return [im]

# 模擬資料到來，每隔 100 ms 加入新資料
def data_gen():
    for i in range(num_measurements):
        yield np.random.random(data_length), i

# 動畫函數
ani = animation.FuncAnimation(fig, lambda frame: update_data(*frame), data_gen, interval=100, blit=True)

plt.colorbar(im)
plt.show()
