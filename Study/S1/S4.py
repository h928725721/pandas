import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 当前时间
    df = pd.Timestamp('now')
    # 指定时间范围
    df = pd.date_range('2020-01-01', '2021-01-01')
    df = pd.date_range('2020-01-01', periods=10)

    # 生成6周的日期
    df = pd.date_range('2020-01-01', periods=6, freq='W')
    # 生成指定区间内的工作日日期
    df = pd.bdate_range(start='2020-01-01', end='2021-01-01')

    # 计算间隔天数
    df = (pd.Timestamp('now') - pd.to_datetime('2021-01-01')).days
    # 计算指定时间间隔多少小时
    df = (pd.Timestamp('now') - pd.to_datetime('2021-01-01 09:01:01')) / np.timedelta64(1, 'h')
    # 日期格式化
    df = pd.Timestamp('now').strftime('%Y年%m月%d日-%H时%M分%S秒')
    print(df)
