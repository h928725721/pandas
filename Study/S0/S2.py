import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def data_group():
    global df
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)})
    print(df)
    print('数据分组')
    print(df.groupby('A').sum())
    print(df.groupby(['A', 'B']).sum())


def data_remodeling():
    # zip()函数，将两个数组中的元素一一对应组合成元组，*操作符，将元组中的元素解压缩成单独的参数
    tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                         'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two',
                         'one', 'two', 'one', 'two']]))
    print("tuples")
    print(tuples)
    # pd.MultiIndex.from_tuples 将元组列表转换为多级索引对象，并将指定新的索引，names 为多级索引每两个层级指定新的索引
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    print(df)
    df2 = df[:4]
    print(df2)
    print('df2的列索引有两层，stack可以将最内层的列索引转换为新的行索引的最内层')
    print('stack')
    stack = df2.stack()
    print(stack)
    print('unstack()操作与stack操作相反，将最内层的列索引转换为新的行索引的最内层。')
    print(stack.unstack())
    print(stack.unstack(0))
    print(stack.unstack(1))

    stack2 = df2.unstack()
    print(stack2)


def data_perspective_table():
    global df
    df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                       'B': ['A', 'B', 'C'] * 4,
                       'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D': np.random.randn(12),
                       'E': np.random.randn(12)})

    print(df)
    # 以D的值填充，A,B的值组合为索引，C的值作为新的列
    dd = df.pivot_table(values='D', index=['A', 'B'], columns='C')
    print(dd)


def date_sequence():
    global ts
    print('100个时间点，频率为每秒一次（即freq=\'S\') T表示分钟，H小时，D每天  ')
    rng = pd.date_range('1/1/2012', periods=100, freq='S')
    print(rng)
    print('每个元素都是一个随机整数（randint方法，len表示随机数的数量）')
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    print(ts)
    print('对结果重采样，将数据的时间精度下降到了分钟级别，每隔5分钟为一个时间段，sum对每个时间段的数据求和统计')
    rs = ts.resample('5Min').sum()
    print(rs)
    print('***********')
    rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
    ts = pd.Series(np.random.randn(len(rng)), rng)
    print(ts)
    print('指定时间区域')
    ts_utc = ts.tz_localize('UTC')
    print(ts_utc)
    print('时区转换')
    ts_utc = ts_utc.tz_convert('US/Eastern')
    print(ts_utc)
    print('在时间跨度表示之间进行转换')
    rng = pd.date_range('1/1/2012', periods=5, freq='M')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    print(ts)
    print('将时间映射为周期结果，此例子中为每个月一个周期')
    ts = ts.to_period()
    print(ts)
    print('转换为时间戳')
    ts = ts.to_timestamp()
    print(ts)
    print('将以11月结束的年度的季度频率转换为季度结束后的月末的上午9点')
    prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
    ts = pd.Series(np.random.randn(len(prng)), prng)
    print(ts)
    print(
        '将其转换为M频率，并加1，就可以获得每个季度的最后一个月的时间戳，然后将其转化为H频率，并与9相加，以获得每个季度末尾的第9个小时的时间戳')
    ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
    print(ts.head(2))


def data_type_use():
    global df
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
    print(df)
    # category 存储离散值的一种数据结构
    df['grade'] = df['raw_grade'].astype("category")
    print(df['grade'])


def data_visualization():
    global ts, df
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    print(ts.head())
    print('累加')
    ts = ts.cumsum()
    print(ts)
    ts.plot()
    plt.show()
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                      columns=['A', 'B', 'C', 'D'])
    df = df.cumsum()
    # 创建一个新的图形窗口
    plt.figure()
    df.plot()
    # 为每一列添加图例
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    # data_group()

    # data_remodeling()

    # data_perspective_table()

    # date_sequence()

    # data_type_use()

    # data_visualization()
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                      columns=['A', 'B', 'C', 'D'])
    # df.to_csv('foo.csv')
    # pd.read_csv('foo.csv').head()
    # df.to_hdf('foo.h5','df')
    # pd.read_hdf('foo.h5','df').head()
    # df.to_excel('foo.xlsx', sheet_name='Sheet1')
    # pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']).head()