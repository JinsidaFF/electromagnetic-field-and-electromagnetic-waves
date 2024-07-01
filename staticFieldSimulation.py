import numpy as np
import sympy as sp
import sympy.vector as sv
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False 

#第一题
A = np.array([1, 5, 3])
B = np.array([1, 6, 7])
C = np.array([3, 2, -8])
print("A(B×C) =",np.dot(A, np.cross(B, C)))
print("A×(B×C) =",np.cross(A, np.cross(B, C)))

#第二题
C = sv.CoordSys3D('C')
A_2 = -C.y*C.i + C.x*C.j + C.z*C.k
B_2 = -2 *C.x *C.y *C.i + C.x *C.y**2 *C.j + C.z**3 *C.k
print("AB点积的梯度:",sv.gradient(sv.dot(A_2, B_2)))

#第三题
k = 8.99e9  
q = 2e-9    
#电荷位置
charge1_pos = np.array([0, 0])   # 原点
charge2_pos = np.array([1, 1])   # 任意位置，可以改变

#建立坐标系
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

#函数
def electric_field(q, pos, X, Y):
    r = np.sqrt((X - pos[0])**2 + (Y - pos[1])**2)
    Ex = k * q * (X - pos[0]) / r**3
    Ey = k * q * (Y - pos[1]) / r**3
    return Ex, Ey
#电势函数
def electric_potential(q, pos, X, Y):
    r = np.sqrt((X - pos[0])**2 + (Y - pos[1])**2)
    V = k * q / r
    return V

#电场
Ex1, Ey1 = electric_field(q, charge1_pos, X, Y)
Ex2, Ey2 = electric_field(q, charge2_pos, X, Y)
Ex = Ex1 + Ex2
Ey = Ey1 + Ey2
#电势
V1 = electric_potential(q, charge1_pos, X, Y)
V2 = electric_potential(q, charge2_pos, X, Y)
V = V1 + V2

plt.figure(figsize=(12, 6))

#电场线
plt.subplot(1, 2, 1)
plt.streamplot(X, Y, Ex, Ey, color='b', linewidth=0.5, density=1.5)
plt.scatter([charge1_pos[0], charge2_pos[0]], [charge1_pos[1], charge2_pos[1]], color='r', s=50)
plt.title('电场分布')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')
#等势面
plt.subplot(1, 2, 2)
plt.contour(X, Y, V, levels=100, cmap='viridis')
plt.scatter([charge1_pos[0], charge2_pos[0]], [charge1_pos[1], charge2_pos[1]], color='r', s=50)
plt.title('电荷等势面')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')

plt.tight_layout()
plt.show()

#第四问
z = sp.symbols('z')

mu0 = 4 * np.pi * 10**-7
I = 1.0
R = 0.1

B_expr = (mu0 * I * R**2) / (2 * (R**2 + z**2)**(3/2))
B_func = sp.lambdify(z, B_expr, 'numpy')

z_vals = np.linspace(-0.5, 0.5, 400)
B_vals = B_func(z_vals)

#制图
plt.figure(figsize=(8, 6))
plt.plot(z_vals, B_vals, label='Magnetic Field B')
plt.title('轴线磁感应强度分布')
plt.xlabel('z (m)')
plt.ylabel('B (T)')
plt.legend()
plt.grid(True)
plt.show()

