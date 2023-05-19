import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('json_data.csv', parse_dates='订单日期')
