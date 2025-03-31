import numpy as np
import matplotlib.pyplot as plt

def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    模拟并可视化两个正弦波叠加产生的拍频现象
    
    参数:
        f1 (float): 第一个波的频率，默认440Hz
        f2 (float): 第二个波的频率，默认444Hz
        A1 (float): 第一个波的振幅，默认1.0
        A2 (float): 第二个波的振幅，默认1.0
        t_start (float): 时间起始点，默认0秒
        t_end (float): 时间结束点，默认1秒
        num_points (int): 采样点数，默认5000
    
    返回:
        tuple: 包含三个元素的元组
            - t (ndarray): 时间数组
            - superposed_wave (ndarray): 叠加后的波形数据
            - beat_frequency (float): 计算得到的拍频
    
    示例:
        >>> t, wave, beat = simulate_beat_frequency(f1=440, f2=444)
        >>> print(f"拍频频率: {beat}Hz")
    """
    # 生成时间范围
    t = np.linspace(t_start, t_end, num_points)

    # 生成两个正弦波
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)

    # 叠加两个波
    superposed_wave = wave1 + wave2

    # 计算拍频
    beat_frequency = np.abs(f1 - f2)

    # 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 6))
        plt.subplot(3, 1, 1)
        plt.plot(t, wave1, label=f'Wave 1 (f={f1} Hz, A={A1})')
        plt.title('Wave 1')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
    
        plt.subplot(3, 1, 2)
        plt.plot(t, wave2, label=f'Wave 2 (f={f2} Hz, A={A2})')
        plt.title('Wave 2')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
    
        plt.subplot(3, 1, 3)
        plt.plot(t, superposed_wave, label=f'Superposed Wave (Beat f={beat_frequency} Hz)')
        plt.title('Superposed Wave')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
    
        plt.tight_layout()
        plt.show()
    return t, superposed_wave, beat_frequency

def parameter_sensitivity_analysis():
    """
    分析频率差和振幅比例对拍频现象的影响
    
    该函数会生成两套子图:
    1. 展示不同频率差(1Hz, 2Hz, 5Hz, 10Hz)对拍频波形的影响
    2. 展示不同振幅比例(0.5, 1.0, 2.0, 5.0)对拍频波形的影响
    
    注意:
        每次调用会显示两个独立的图形窗口，分别对应频率差和振幅比例的分析
    
    示例:
        >>> parameter_sensitivity_analysis()
    """
    # 不同频率差的影响
    base_freq = 440
    freq_diffs = [1, 2, 5, 10]
    
    plt.figure(1,figsize=(12, 8))
    for i, diff in enumerate(freq_diffs):
        t, wave, _ = simulate_beat_frequency(f1=base_freq, f2=base_freq+diff,show_plot=False)
        plt.subplot(2, 2, i+1)
        plt.plot(t, wave)
        plt.title(f'Frequency diff = {diff} Hz')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


    # 不同振幅比例的影响
    amplitude_ratios = [0.5, 1.0, 2.0, 5.0]
    plt.figure(2,figsize=(12, 8))
    for i, ratio in enumerate(amplitude_ratios):
        t, wave, _ = simulate_beat_frequency(A2=ratio,show_plot=False)
        plt.subplot(2, 2, i+1)
        plt.plot(t, wave)
        plt.title(f'Amplitude ratio = {ratio}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    # 示例调用
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency()
    print(f"计算得到的拍频为: {beat_freq} Hz")
    
    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
    
    
