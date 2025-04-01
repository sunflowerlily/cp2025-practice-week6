import numpy as np
from scipy.integrate import quad

# 最概然速率 (m/s)
vp = 1578  

# 麦克斯韦速率分布函数
def maxwell_distribution(v, vp):
    """
    计算麦克斯韦速率分布函数值
    
    参数：
    v : 分子速率 (m/s)
    vp : 最概然速率 (m/s)
    
    返回：
    分布函数f(v)的值
    """
    return (4/np.sqrt(np.pi)) * (v**2 / vp**3) * np.exp(-(v**2) / (vp**2))

# 任务1：计算0到vp的概率百分比
def percentage_0_to_vp(vp):
    # 你的代码在这里实现
    pass

# 任务2：计算0到3.3vp的概率百分比
def percentage_0_to_3_3vp(vp):
    # 你的代码在这里实现
    pass

# 任务3：计算3×10^4到3×10^8 m/s的概率百分比
def percentage_3e4_to_3e8(vp):
    # 你的代码在这里实现
    pass

if __name__ == "__main__":
    print("0 到 vp 间概率百分比:", percentage_0_to_vp(vp), "%")
    print("0 到 3.3vp 间概率百分比:", percentage_0_to_3_3vp(vp), "%")
    print("3×10^4 到 3×10^8 间概率百分比:", percentage_3e4_to_3e8(vp), "%")