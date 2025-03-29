import numpy as np
import math

def lagrange_interp(x_data, y_data, x_target):
    """
    Lagrange插值計算
    參數:
        x_data: 已知x值陣列
        y_data: 已知y值陣列
        x_target: 需要插值的x點
    返回:
        插值結果
    """
    n = len(x_data)
    result = 0.0
    
    # Lagrange插值公式實現
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x_target - x_data[j])/(x_data[i] - x_data[j])
        result += term
    return result

# 已知數據點
x_points = np.array([0.698, 0.733, 0.768, 0.803])
y_points = np.array([0.7661, 0.7432, 0.7193, 0.6946])
target_x = 0.750
true_value = 0.7317

# 計算不同階數的插值
print("Q1：Lagrange插值近似cos(0.750)")
for degree in range(1, 4):
    # 取前degree+1個點進行插值
    approx = lagrange_interp(x_points[:degree+1], y_points[:degree+1], target_x)
    error = abs(approx - true_value)
    print(f"{degree}次插值結果: {approx:.8f}, 誤差: {error:.8f}")

# 誤差界限計算
def error_bound(x_points, x_target, n, max_deriv):
    """
    計算Lagrange插值誤差上界
    參數:
        x_points: 插值節點
        x_target: 目標x值
        n: 插值多項式次數
        max_deriv: n+1階導數的最大值
    返回:
        誤差上界
    """
    product = 1.0
    for i in range(n+1):
        product *= abs(x_target - x_points[i])
    return (max_deriv/math.factorial(n+1)) * product

# 對cos(x)函數，n+1階導數的最大值為1
print("\n誤差界限分析:")
for degree in range(1, 4):
    bound = error_bound(x_points[:degree+1], target_x, degree, 1.0)
    print(f"{degree}次插值誤差界限: {bound:.8e}")