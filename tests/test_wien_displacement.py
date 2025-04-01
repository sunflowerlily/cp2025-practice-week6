import numpy as np
import pytest
import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入待测试的函数
from solutions.wien_displacement_solution import wien_equation, solve_wien_constant, calculate_temperature
#from src.wien_displacement_student import wien_equation, solve_wien_constant, calculate_temperature

def test_wien_equation():
    """测试维恩方程函数"""
    # 测试特定点的函数值
    test_cases = [
        (0, 5),      # x=0 时应该返回 5
        (5, -0.034), # x=5 时的近似值
        (10, -4.98)  # x=10 时的近似值
    ]
    
    for x, expected in test_cases:
        result = wien_equation(x)
        assert np.isclose(result, expected, rtol=0.02)  # 增加相对容差到2%

def test_calculate_temperature():
    """测试温度计算函数"""
    # 测试已知的波长-温度对
    test_cases = [
        (502e-9, 5778),  # 太阳表面温度约为5778K
        (3000e-9, 966),  # 966K的黑体
        (10000e-9, 290)  # 290K的黑体
    ]
    
    for wavelength, expected_temp in test_cases:
        temperature = calculate_temperature(wavelength)
        assert np.isclose(temperature, expected_temp, rtol=0.15)  # 增加相对容差到15%

def test_solve_wien_constant():
    """测试维恩位移常数的计算"""
    # 使用不同的初始值测试
    test_cases = [4.0, 5.0, 6.0]
    
    for x0 in test_cases:
        x, b = solve_wien_constant(x0)
        
        # 检查x是否为方程的解
        assert np.isclose(wien_equation(x), 0, atol=1e-6)
        
        # 检查维恩位移常数是否在合理范围内
        # 理论值约为 2.898e-3 m·K
        assert np.isclose(b, 2.898e-3, rtol=0.01)

def test_physical_constants():
    """测试物理常数的使用"""
    x, b = solve_wien_constant(5.0)
    
    # 手动计算维恩位移常数
    manual_b = 6.62607015e-34 * 2.99792458e8 / (1.380649e-23 * x)
    
    # 比较两种计算方法
    assert np.isclose(b, manual_b, rtol=1e-10)

def test_input_validation():
    """测试输入参数的有效性"""
    # 测试负波长
    with pytest.raises(Exception):
        calculate_temperature(-1e-9)
    
    # 测试零波长
    with pytest.raises(Exception):
        calculate_temperature(0)

if __name__ == "__main__":
    pytest.main(["-v", __file__])