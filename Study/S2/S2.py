import pandas as pd

if __name__ == '__main__':
    df = pd.read_json('bond.json')
    df['日期'] = pd.to_datetime(df['日期'])

    # 日期筛选计算
    df1 = df[(df['日期'] > '2023-01-01') & (df['日期'] < '2023-01-21')]
    # 筛选指定日期数据
    df2 = df.set_index('日期').truncate(after=pd.Timestamp('2023-01-02'))
    print(df2)
