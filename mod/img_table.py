import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import fontManager

from io import StringIO,BytesIO
import base64

def Generate_Table(data_str):
    fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
    mpl.rc('font', family='Taipei Sans TC Beta')
    
    # 使用StringIO将字符串转换为文件对象
    data_file = StringIO(data_str)

    # 读取csv文件并将其转换为DataFrame
    data = pd.read_csv(data_file)
    # 将日期的年份去除，只保留月份和日期
    data["日期"] = pd.to_datetime(data["日期"]).dt.strftime('%m-%d')

    plt.figure(figsize=(15, 6)) # 設定圖形大小和背景顏色為深灰色

    # 第一張圖：卡路里
    plt.subplot(2, 2, 1)
    plt.plot(data["日期"], data["卡路里 (大卡)"], label="卡路里")
    plt.legend()
    plt.title("卡路里")

    # 第二張圖：距離
    plt.subplot(2, 2, 2)
    plt.plot(data["日期"], data["距離 (公尺)"], label="距離")
    plt.legend()
    plt.title("距離")

    # 第三張圖：平均心率
    plt.subplot(2, 2, 3)
    plt.plot(data["日期"], data["平均心率 (每分鐘心跳數)"], label="平均心率")
    plt.legend()
    plt.title("平均心率")

    # 第四張圖：平均速度
    plt.subplot(2, 2, 4)
    plt.plot(data["日期"], data["平均速度 (公尺/秒)"], label="平均速度")
    plt.legend()
    plt.title("平均速度")

    plt.tight_layout() # 自動調整子圖間的間距

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # 關閉圖形
    plt.close()
    return image_base64