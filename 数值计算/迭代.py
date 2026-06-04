import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 1. 定义方程组系数矩阵 A 和右侧常数项 b
# 2x - 1y = 2
# -1x + 3y = 3
a11, a12, b1 = 2.0, -1.0, 2.0
a21, a22, b2 = -1.0, 3.0, 3.0
A = np.array([[a11, a12], 
              [a21, a22]])
b = np.array([b1, b2])

# 初始猜测值和迭代步数
x_init = np.array([0.0, 0.0])
max_iter = 7  # 降低步数，防止同一个图里标注太拥挤


# 2. 雅可比迭代过程记录
def jacobi_trace(A, b, x0, steps):
    history = [x0.copy()]
    x = x0.copy()
    for _ in range(steps):
        x_new = np.zeros_like(x)
        x_new[0] = (b[0] - A[0, 1] * x[1]) / A[0, 0]
        x_new[1] = (b[1] - A[1, 0] * x[0]) / A[1, 1]
        x = x_new
        history.append(x.copy())
    return np.array(history)

# 3. 高斯-赛德尔迭代过程记录
def gauss_seidel_trace(A, b, x0, steps):
    history = [x0.copy()]
    x = x0.copy()
    for _ in range(steps):
        x[0] = (b[0] - A[0, 1] * x[1]) / A[0, 0]
        history.append(x.copy())
        x[1] = (b[1] - A[1, 0] * x[0]) / A[1, 1]
        history.append(x.copy())
    return np.array(history)


def sor_trace(A, b, x0, steps, omega=1.0):
    """Successive Over-Relaxation (SOR) 跟踪，每次更新单个分量后记录中间状态。"""
    history = [x0.copy()]
    x = x0.copy()
    n = x.size
    for _ in range(steps):
        for j in range(n):
            # 计算不含 x_j 的矩阵乘积
            sigma = 0.0
            for k in range(n):
                if k != j:
                    sigma += A[j, k] * x[k]
            x_j_gs = (b[j] - sigma) / A[j, j]
            x[j] = (1 - omega) * x[j] + omega * x_j_gs
            history.append(x.copy())
    return np.array(history)

# 获取轨迹数据
jacobi_history = jacobi_trace(A, b, x_init, max_iter)
gs_history = gauss_seidel_trace(A, b, x_init, max_iter)
# 超松弛参数（可调整）
sor_omega = 1.1
sor_history = sor_trace(A, b, x_init, max_iter, omega=sor_omega)


def add_path_arrows(points, color):
    for i in range(len(points) - 1):
        plt.annotate(
            '',
            xy=points[i + 1],
            xytext=points[i],
            arrowprops=dict(arrowstyle='->', color=color, lw=1.5, shrinkA=0, shrinkB=0),
            zorder=4,
        )


def add_step_boxes(points, color):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        rect = Rectangle(
            (min(x0, x1), min(y0, y1)),
            abs(x1 - x0),
            abs(y1 - y0),
            fill=False,
            linestyle='--',
            linewidth=1.3,
            edgecolor=color,
            alpha=0.75,
            zorder=3,
        )
        plt.gca().add_patch(rect)

# 4. 开始绘图（单图模式）
plt.figure(figsize=(10, 8))

# 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 绘制几何背景：方程组对应的两条直线
x_range = np.linspace(-0.5, 3.0, 100)
y1 = (b1 - a11 * x_range) / a12
y2 = (b2 - a21 * x_range) / a22

plt.plot(x_range, y1, 'g--', alpha=0.7, label='方程①: 2x - y = 2')
plt.plot(x_range, y2, 'b--', alpha=0.7, label='方程②: -x + 3y = 3')

# 绘制精确解交点 (1.8, 1.6)
plt.plot(1.8, 1.6, 'o', markersize=5, zorder=5, label='精确解 (1.8,1.6)')

# 5. 绘制两条迭代轨迹进行对比
# 雅可比轨迹 (橙色)
plt.plot(jacobi_history[:, 0], jacobi_history[:, 1], 
         color='darkorange', marker='o', linewidth=2, markersize=2, label='雅可比迭代 (Jacobi)')
add_step_boxes(jacobi_history, 'darkorange')
add_path_arrows(jacobi_history, 'darkorange')

# 高斯-赛德尔轨迹（每次单个变量更新都记录一个点）
plt.plot(gs_history[:, 0], gs_history[:, 1], 
         color='purple', marker='s', linewidth=2, markersize=2, label='高斯-赛德尔迭代 (Gauss-Seidel)')
add_path_arrows(gs_history, 'purple')

# SOR 轨迹（超松弛）
plt.plot(sor_history[:, 0], sor_history[:, 1], 
         color='teal', marker='^', linewidth=2, markersize=3, label=f'SOR (ω={sor_omega})')
add_path_arrows(sor_history, 'teal')

# 6. 为前几步加上数字序号标签，方便对比速度
for i in range(4):  # 只标注前4个记录点，避免重叠
    # 雅可比文本标注
    plt.text(jacobi_history[i, 0] + 0.05, jacobi_history[i, 1] - 0.08, 
             f'J{i}', fontsize=10, color='darkorange', weight='bold')
    # 高斯-赛德尔文本标注
    plt.text(gs_history[i, 0] - 0.12, gs_history[i, 1] + 0.08, 
             f'GS{i}', fontsize=10, color='purple', weight='bold')
    # SOR 文本标注
    plt.text(sor_history[i, 0] + 0.05, sor_history[i, 1] - 0.08, 
             f'SOR{i}', fontsize=10, color='teal', weight='bold')

plt.title('二维平面上各种迭代法轨迹对比', fontsize=14)
plt.xlabel('X 轴', fontsize=12)
plt.ylabel('Y 轴', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
# 去重图例，防止重复标签（例如重复运行同一脚本时出现）
handles, labels = plt.gca().get_legend_handles_labels()
unique = {}
unique_handles = []
unique_labels = []
for h, l in zip(handles, labels):
    if l not in unique:
        unique[l] = True
        unique_handles.append(h)
        unique_labels.append(l)
plt.legend(unique_handles, unique_labels, loc='upper left', fontsize=11)

# 设置合理的轴范围
plt.xlim(-0.3, 2.6)
plt.ylim(-0.3, 2.8)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()