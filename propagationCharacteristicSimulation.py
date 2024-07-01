import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

def plot_electric_field():
    # 参数设置
    x = np.arange(0, 6*np.pi, 0.01)
    
    # 初始化图形
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(30, 30)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # 设置初始的电场和磁场数据
    line1, = ax.plot([], [], [], 'r.', label='Electric Field')
    line2, = ax.plot([], [], [], 'b.', label='Magnetic Field')

    # 动画初始化函数
    def init():
        ax.set_xlim(0, 6*np.pi)
        ax.set_ylim(-1.5, 1.5)
        ax.set_zlim(-1, 1)
        line1.set_data([], [])
        line1.set_3d_properties([])
        line2.set_data([], [])
        line2.set_3d_properties([])
        return line1, line2

    # 动画更新函数
    def update(frame):
        phase_shift = frame / 10.0
        data = np.cos(x + phase_shift)
        data_mag = data / 2
        line1.set_data(x, data)
        line1.set_3d_properties(np.zeros_like(x))
        line2.set_data(x, np.zeros_like(x))
        line2.set_3d_properties(data_mag)

        return line1, line2

    # 创建动画
    ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), init_func=init, blit=True)

    # 显示动画
    plt.legend()
    plt.show()
    ani.save("1.gif")



def polarizationShape(Exm, Eym, faix, faiy, w=4*10**6, t=1, z_start=1, z_end=300, z_points=300, k=0.1):
    """
    绘制线极化波的3D图。
    
    参数：
    Exm: float - x方向上的场强
    Eym: float - y方向上的场强
    faix: float - x方向上的相位
    faiy: float - y方向上的相位
    w: float - 角频率 (默认值为4MHz)
    t: float - 时间 (默认值为1)
    z_start: float - z坐标起始值 (默认值为1)
    z_end: float - z坐标结束值 (默认值为300)
    z_points: int - z坐标的点数 (默认值为300)
    k: float - 波数 (默认值为0.1)
    
    输出：
    None
    """

    # 定义z坐标
    z = np.linspace(z_start, z_end, z_points)
    # 初始化电场分量
    Ex = np.zeros(len(z))
    Ey = np.zeros(len(z))
    # 计算电场分量
    for ii in range(len(z)):
        Ex[ii] = Exm * np.cos(w * t - k * z[ii] + faix)
        Ey[ii] = Eym * np.cos(w * t - k * z[ii] + faiy)
    #绘图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=45, azim=-40)
    ax.plot3D(Ex, Ey, z, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

#调用
plot_electric_field()

#调用
polarizationShape(Exm=1, Eym=1, faix=-np.pi/2, faiy=0)
polarizationShape(Exm=1, Eym=1, faix=-np.pi/4, faiy=-np.pi/4)
polarizationShape(Exm=1, Eym=2, faix=-np.pi/4, faiy=0)





