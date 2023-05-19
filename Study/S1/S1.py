import pandas as pd


def excel_read():
    pass
    # data = pd.read_csv('../S0/foo.csv')
    # data = pd.read_csv('../S0/foo.csv',nrows=20)
    # 跳过前20行
    # data = pd.read_csv('../S0/foo.csv', skiprows=[i for i in range(1, 21)])
    # 指定偶数行读取
    # data = pd.read_csv('../S0/foo.csv', skiprows=lambda x: (x != 0) and not x % 2)
    # 指定列号读取
    # data = pd.read_csv('../S0/foo.csv',usecols=[0,2,4])
    # 指定列名读取
    # data = pd.read_csv('../S0/foo.csv', usecols=['A', 'B', 'C'])
    # 指定列匹配就读取
    # usecols = ['A', 'C', 'E', 'sdfa']
    # data = pd.read_csv('../S0/foo.csv', usecols=lambda c : c in set(usecols))
    # 读取时将A列值设置为索引
    # data = pd.read_csv('../S0/foo.csv',index_col=['A'])
    # 读取并设置标题
    # data = pd.read_csv('../S0/foo.csv',usecols=[1,2,3],names=['测试A','测试B','测试C'])
    # 分别是，不将缺失值标识为NA；将[]标识为缺失值；不处理缺失值
    # data = pd.read_csv('../S0/foo.csv',keep_default_na=False,na_values=['[]'],na_filter=False)
    # 指定格式，日期可以用parse_dates[]
    # data = pd.read_csv('../S0/foo.csv', dtype={'A': str, 'B': float})


def txt_read():
    pass
    # pd.read_table('xxx.txt')
    # 读取时设置编码
    # pd.read_table('xxx.txt',encoding='gb18030')


if __name__ == '__main__':
    # excel_read()

    # txt_read()

    data = pd.read_html(
        "https://baike.baidu.com/item/2020%E5%B9%B4%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A/10188878?fromtitle"
        "=%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A&fromid=3250130&fr=aladdin")[6]
    data.to_excel('test.xlsx')



    print(data)
