from matplotlib.font_manager import fontManager
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

from io import StringIO,BytesIO

def Generate_Table(data_str):

    fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
    mpl.rc('font', family='Taipei Sans TC Beta')
    colors = ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color', 'axes.edgecolor']

    for set in colors:
        plt.rcParams[set] = 'white'

    data_file = StringIO(data_str)
    
    df = pd.read_csv(data_file)
    plt.figure(facecolor="#1e2124", figsize=(12,7))
    x = list(range(1,25))

    # 步數子圖
    plt.subplot(2, 2, 1)
    plt.title("步數")
    step_num = df['步數']/100
    plt.plot(x, step_num, 'r')  # red line without marker
    plt.yticks(range(20, 110, 20))  # 手動設置 y 軸範圍
    plt.gca().set_facecolor('#1e2124')
    plt.xlabel('每小時')
    plt.ylabel('每100步')

    # 平均心律子圖
    plt.subplot(2, 2, 2)
    plt.title("平均心律")
    ahr = df['平均心律']
    plt.plot(x, ahr, 'r')  # red line without marker
    plt.yticks(range(60, 110, 10))  # 手動設置 y 軸範圍
    plt.gca().set_facecolor('#1e2124')
    plt.xlabel('每小時')
    plt.ylabel('心跳平均值')


    # 心跳子圖
    plt.subplot(2, 2, 3)
    plt.title("心跳")
    heart_bit = df['心跳']
    plt.plot(x, heart_bit, 'r')  # red line without marker
    plt.yticks(range(60, 130, 10))  # 手動設置 y 軸範圍
    plt.gca().set_facecolor('#1e2124')
    plt.xlabel('每小時')
    plt.ylabel('每分鐘心跳次數')

    # 血氧濃度子圖
    plt.subplot(2, 2, 4)
    plt.title("血氧濃度")
    spox = df['血氧濃度']
    plt.plot(x, spox, 'r')  # red line without marker
    plt.yticks(range(90, 101, 2))  # 手動設置 y 軸範圍
    plt.gca().set_facecolor('#1e2124')
    plt.xlabel('每小時')
    plt.ylabel('百分比')

    plt.tight_layout()

    # 儲存圖片
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    png = buffer.read()
    plt.close()
    return png