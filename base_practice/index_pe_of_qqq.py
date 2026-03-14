import requests
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from scipy import stats


def get_nasdaq100_components():
    """获取纳指100成分股列表"""
    url = "https://en.wikipedia.org/wiki/Nasdaq-100"
    tables = pd.read_html(url)
    components = tables[3]  # 纳指100成分股表格
    return components['Ticker'].tolist()


def calculate_index_pe(tickers):
    """计算纳指100的加权PE比率"""
    pe_ratios = []
    market_caps = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            if 'trailingPE' in info and 'marketCap' in info:
                pe_ratios.append(info['trailingPE'])
                market_caps.append(info['marketCap'])
        except:
            continue

    if not pe_ratios:
        return None

    # 计算市值加权PE
    pe_array = np.array(pe_ratios)
    mc_array = np.array(market_caps)
    weighted_pe = np.sum(pe_array * mc_array) / np.sum(mc_array)
    return weighted_pe


def get_historical_pe_data():
    """获取历史PE数据（这里使用模拟数据，实际应用中应从数据库或API获取）"""
    # 模拟数据：日期和对应的纳指100 PE
    dates = pd.date_range(start='2010-01-01', end=datetime.today(), freq='M')
    pe_values = np.random.normal(loc=25, scale=5, size=len(dates)).cumsum() / 10 + 20
    pe_values = np.clip(pe_values, 15, 40)  # 限制在15-40之间

    # 添加一些异常值模拟真实市场
    pe_values[10] = 45
    pe_values[30] = 15
    pe_values[80] = 50

    return pd.DataFrame({'Date': dates, 'PE': pe_values})


def analyze_pe_percentile(current_pe, historical_data):
    """分析当前PE的历史百分位"""
    historical_pe = historical_data['PE'].values

    # 计算百分位
    percentile = stats.percentileofscore(historical_pe, current_pe)

    # 计算统计指标
    mean_pe = np.mean(historical_pe)
    median_pe = np.median(historical_pe)
    min_pe = np.min(historical_pe)
    max_pe = np.max(historical_pe)
    std_pe = np.std(historical_pe)

    return {
        'current_pe': current_pe,
        'percentile': percentile,
        'mean_pe': mean_pe,
        'median_pe': median_pe,
        'min_pe': min_pe,
        'max_pe': max_pe,
        'std_pe': std_pe
    }


def plot_pe_history(historical_data, current_pe):
    """绘制PE历史走势图"""
    plt.figure(figsize=(12, 6))
    plt.plot(historical_data['Date'], historical_data['PE'], label='Historical PE')
    plt.axhline(y=current_pe, color='r', linestyle='--', label=f'Current PE: {current_pe:.2f}')

    # 添加统计线
    mean_pe = np.mean(historical_data['PE'])
    plt.axhline(y=mean_pe, color='g', linestyle=':', label=f'Mean PE: {mean_pe:.2f}')

    plt.title('Nasdaq-100 Historical PE Ratio')
    plt.xlabel('Date')
    plt.ylabel('PE Ratio')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    print("纳指100实时估值分析程序")
    print("正在获取数据...")

    # 1. 获取纳指100成分股
    tickers = get_nasdaq100_components()
    print(f"获取到{len(tickers)}只成分股")

    # 2. 计算当前PE
    current_pe = calculate_index_pe(tickers)
    if current_pe is None:
        print("无法获取当前PE数据")
        return

    print(f"当前纳指100加权PE: {current_pe:.2f}")

    # 3. 获取历史PE数据
    historical_data = get_historical_pe_data()

    # 4. 分析历史百分位
    analysis = analyze_pe_percentile(current_pe, historical_data)

    print("\n估值分析结果:")
    print(f"当前PE: {analysis['current_pe']:.2f}")
    print(f"历史百分位: {analysis['percentile']:.1f}%")
    print(f"历史平均PE: {analysis['mean_pe']:.2f}")
    print(f"历史中位数PE: {analysis['median_pe']:.2f}")
    print(f"历史最低PE: {analysis['min_pe']:.2f}")
    print(f"历史最高PE: {analysis['max_pe']:.2f}")
    print(f"PE标准差: {analysis['std_pe']:.2f}")

    # 5. 绘制图表
    plot_pe_history(historical_data, current_pe)

    # 估值判断
    if analysis['percentile'] > 75:
        print("\n估值警告: 纳指100当前处于高估值区域(高于75%历史时期)")
    elif analysis['percentile'] < 25:
        print("\n估值机会: 纳指100当前处于低估值区域(低于25%历史时期)")
    else:
        print("\n估值提示: 纳指100当前估值处于合理区间")


if __name__ == "__main__":
    main()