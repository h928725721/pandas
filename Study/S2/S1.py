import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('json_data.csv')
    # 各省销售额的平均薪资
    df1 = pd.pivot_table(df, values=['销售额'], index='省/自治区')
    df2 = df[['销售额', '省/自治区']].groupby('省/自治区').mean()

    # 各省销售总额的数据透视表
    df3 = pd.pivot_table(df, values=['销售额'], index='省/自治区', aggfunc=sum)
    df4 = df[['销售额', '省/自治区']].groupby('省/自治区').sum()

    # 计算各省销售总额和平均销售额
    df5 = pd.pivot_table(df, values=['销售额'], index='省/自治区', aggfunc=['mean', 'sum'])

    # 制作各省市「销售总额」与「利润总额」的数据透视表
    df6 = pd.pivot_table(df, values=['销售额', '利润', '数量'], index='省/自治区', aggfunc=sum)
    # 组合索引
    df7 = pd.pivot_table(df, values=['销售额'], index=['省/自治区', '类别'], aggfunc=sum)
    # 不同类别销售总额
    df8 = pd.pivot_table(df, values=['销售额'], index=['省/自治区'], columns='类别', aggfunc=sum)

    # 在最后追加一行合计数值
    df9 = pd.pivot_table(df, values=['销售额', '数量'], index=['省/自治区', '类别'], aggfunc=['mean', sum],
                         margins=True)
    # 按条件查询
    df9 = df9.query('类别 == ["手机"]')

    # 逆透视表，将宽的列转换为长的列
    df10 = pd.pivot_table(df, values=['销售额', '利润', '数量'], index='类别', aggfunc=sum)
    df10 = df10.melt(id_vars=['数量'], var_name='分类', value_name='金额')
    print(df10)
