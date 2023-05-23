import pandas as pd

if __name__ == '__main__':
    df = pd.read_json('bond.json')
    df['日期'] = pd.to_datetime(df['日期'])

    # 日期筛选计算
    df = df[(df['日期'] > '2023-01-01') & (df['日期'] < '2023-01-21')]
    print(df)
