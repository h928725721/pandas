import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_data():
    global s
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    df = base_data()
    # 通过字典创建DataFrame对象
    df2 = pd.DataFrame({'A': (1, 2, 3, 4),
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print('****************')
    print(df2)
    print('****************')
    print(df2.dtypes)
    print('****************')
    print(dir(df2))


def base_data():
    # 通过numpy的arry数据来创建DataFrame对象
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print('****************')
    return df


def data_view():
    global df
    df = base_data()
    print("查看头、尾信息")
    print(df.head(2))
    print(df.tail(3))
    print('查看df的索引、列名、数据信息')
    print(df.index)
    print(df.columns)
    print(df.values)
    print('描述统计信息')
    print(df.describe())
    print('数据转置')
    print(df.T)
    print('根据列名排序')
    print(df.sort_index(axis=1, ascending=False))
    print('根据B列数值排序')
    print(df.sort_values(by='B'))


def data_choose():
    global dates, df
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print('选取单列数据')
    print(df.A)
    # print(df['A'])
    print('按行选数据')
    print(df[0:3])
    print('************')
    print(df['20130102':'20130104'])
    print('通过标签选取数据')
    print(df.loc[dates[0]])
    print('************')
    print(df.loc[:, ['A', 'B']])
    print('************')
    print(df.loc['20130102':'20130103', ['A', 'B']])
    print('************')
    print(df.loc['20130102', ['A', 'B']])
    print('************')
    print(df.loc[dates[0], 'A'])
    print('************')
    print(df.at[dates[0], 'A'])


def data_choose_by_position():
    global dates, df
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print('通过位置选取数据')
    print("************")
    print(df.iloc[3:5, 0:2])
    print("************")
    print(df.iloc[[1, 2, 4], [0, 3]])
    print("************")
    print(df.iloc[1:3])
    print("************")
    print(df.iloc[:, 1:3])
    print("************")
    print(df.iloc[1, 1])
    print(df.iat[1, 1])


def data_use_bool_index():
    global dates, df
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print("************")
    print(df[df.A > 0])
    print("************")
    print(df[df > 0])
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
    print(df2)
    print("************")
    print(df2[df2['E'].isin(['two', 'four'])])


def data_deletion_deal():
    global df1
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
    df1.loc[dates[0]:dates[1], 'E'] = 1
    print(df1)
    print('删除缺失值')
    print(df1.dropna(how='any'))
    print('补充缺失值')
    print(df1.fillna(value=5))
    print(pd.isnull(df1))


def statistics():
    print('纵向求均值')
    print(df.mean())
    print('横向求均值')
    print(df.mean(1))
    print("创建一个Series,dates作为索引，shift(2)表示将元素向下平移两个单位，并用NaN填充前两个单位")
    print(pd.Series([1, 3, 5, np.nan, 6, 8], index=dates))
    print(pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2))
    print('apply方法会遍历DateFrame中的每一列,注意是列')
    print("np.cumsum用于计算数组中元素的累计和，apply将每一列作为参数传递给np.cumsum函数，对df中的每一列执行求和的操作")
    print('原始值')
    print(df)
    print('对每一列求和，每往下一行，就是与上一行加起来的值')
    print(df.apply(np.cumsum))
    print('最后一行算出来的才是总的合计')
    print("************")
    print(df.apply(lambda x: x.max() - x.min()))

    print('value_counts()')
    s = pd.Series(np.random.randint(0, 7, size=10))
    print(s)
    print("统计每个元素出现的次数")
    print(s.value_counts())

    print('字符串方法')
    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print(s.str.lower())


def data_concat():
    global left, right, s
    print('*************')
    dd = pd.DataFrame(np.random.randn(10, 4))
    print(dd)
    print('从刚才创建的DataFrame取出，前三行，4-6行，8到最后一行，并创建一个数组容纳他们')
    pieces = [dd[:3], dd[3:6], dd[7:]]
    print('将三个DataFrame组成一个新的DataFrame.concat: 用于将多个DataFrame拼接到一起')
    print(pd.concat(pieces))
    print('join')
    left = pd.DataFrame({'key': ['foo', 'foo'], 'ival': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'foo'], 'ival': [4, 5]})
    print()
    print(left)
    print(right)
    print(pd.merge(left, right, on='key'))
    print('append')
    dc = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    print(dc)
    s = dc.iloc[3]
    print(s)
    dl = dc._append(s, ignore_index=True)
    print(dl)


if __name__ == '__main__':
    dates = pd.date_range('20130101', periods=6)
    # np.random.randn(6, 4) 表示生成6行4列的随机数数组，填充DataFrame值 index=dates, columns=list('ABCD') 表示分别使用dates和ABCD 作为行索引和列索引
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print("************")

    # create_data()

    # data_view()
    # data_choose()
    # data_choose_by_position()
    # data_use_bool_index()

    # data_deletion_deal()

    # statistics()
    # data_concat()
