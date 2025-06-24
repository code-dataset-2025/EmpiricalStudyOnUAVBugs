import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 请修改以下参数为你的实际数据
file_path = r'.\RQ5.xlsx'
category_col = 'Hardware Related?'  # 分类列名称
measure_cols = ['Assignees', 'Participants', 'Comments(Include report)','Closed Time']  # 四个度量列名称

# 读取数据
df = pd.read_excel(file_path)

# 准备画布
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(wspace=0.3, hspace=0.3)
axes = axes.flatten()

# 为每个度量绘制箱线图
for idx, measure in enumerate(measure_cols):
    ax = axes[idx]

    # 按分类列分割数据
    class0 = df[df[category_col] == 0][measure].dropna()
    class1 = df[df[category_col] == 1][measure].dropna()

    # 绘制箱线图
    box0 = ax.boxplot(class0, positions=[1], patch_artist=True,
                      whis=(0, 100),  # 须从最小值到最大值
                      widths=0.6,
                      boxprops=dict(facecolor='skyblue'),
                      medianprops=dict(color='black', linewidth=2),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'))

    box1 = ax.boxplot(class1, positions=[2], patch_artist=True,
                      whis=(0, 100),
                      widths=0.6,
                      boxprops=dict(facecolor='lightgreen'),
                      medianprops=dict(color='black', linewidth=2),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'))

    # 添加平均值标记
    ax.scatter(1, np.mean(class0), color='white', edgecolor='black', s=60, zorder=3)
    ax.scatter(2, np.mean(class1), color='white', edgecolor='black', s=60, zorder=3)
    print(measure)
    print("左边的平均值",np.mean(class0))
    print("右边的平均值",np.mean(class1))
    print("左边的中位数",np.median(class0))
    print("右边的中位数",np.median(class1))
    print()
    # 设置坐标轴
    ax.set_title(measure, fontsize=10)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Non Hardware-Related', 'Hardware-Related'])
    ax.grid(True, linestyle='--', alpha=0.7)

plt.savefig(r'.\RQ5.png', dpi=1000)
# 显示图形
plt.show()
