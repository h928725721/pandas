import pandas as pd
import numpy as np


def myfun(x):
    return x.max() - x.mean()


def group_data():
    global data1, data2, data13
    # mean()均值
    data1 = data[['district', 'salary']].groupby(by='district').mean()
    # 分组不以district作为索引
    data2 = data.groupby('district', as_index=False)['salary'].mean()
    # 排序
    data3 = data[['district', 'salary']].groupby(by='district').mean().sort_values('salary', ascending=False).head(1)
    # 计算不同区，不同人数公司的数量
    data4 = pd.DataFrame(data.groupby('district')['companySize'].value_counts())
    # 修改索引名
    data4.rename_axis(['行政区', '公司规模'], inplace=True)
    # 按照上面的逻辑，查看区域的数量
    data5 = data4.groupby('行政区')['count'].count()
    # 将所有数据按地区和薪资分组展示
    data6 = data.groupby(['district', 'salary']).groups
    # 按照条件查看数据
    data7 = data.groupby(['district', 'salary']).get_group(('商业区', 15000))
    # apply(lambda x: x.day) 将每个日期的天数提取出来，以便按照天数进行分组
    data8 = pd.DataFrame(data.groupby([data.createTime.apply(lambda x: x.day)])['district'].value_counts()).rename_axis(
        ['发布日', '行政区'])
    # 按区域分组，并计算行业包含科技的数量
    data9 = data.groupby('district', sort=False)['industryField'].apply(lambda x: x.str.contains('科技').sum())
    # 根据positionName的长度进行分组，并计算平均薪资
    data10 = data.set_index('positionName').groupby(len)['salary'].mean()
    # 将 score 和 matchScore 的和记为总分，与 salary 列同时进行分组，并查看结果
    data11 = data.groupby({'salary': '薪资', 'score': '总分', 'matchScore': '总分'}, axis=1).sum()
    # 计算不同 工作年限（workYear）和 学历（education）之间的薪资均值
    data12 = pd.DataFrame(data['salary'].groupby([data['workYear'], data['education']]).mean())
    # 新增一列，为该地区平均薪资
    data['该区平均薪资'] = data[['district', 'salary']].groupby(by='district').transform('mean')
    data13 = data.groupby('district').filter(lambda x: x.salary.mean() < 30000)


if __name__ == '__main__':
    data = pd.read_csv('json_data.csv', parse_dates=['createTime'])
    group_data()
    # 胡同地区的薪资最大值，最小值，平均值
    data1 = data.groupby('district')['salary'].agg([max, min, np.mean])
    # 修改列名
    data2 = data.groupby('district').agg(最低工资=('salary', 'min'), 最高工资=('salary', 'max'),
                                         平均工资=('salary', 'mean')).rename_axis(['平均值'])

    # 计算中位数和均值
    data3 = data.groupby('positionName').agg({'salary': np.median, 'score': np.mean})
    # 对不同行政区进行分组，并统计薪水的均值、中位数、方差，以及得分的均值
    data4 = data.groupby('district').agg({'salary': [np.mean, np.median, np.std], 'score': np.mean})

    data5 = data.groupby('district').agg(最低工资=('salary', 'min'), 最高工资=('salary', 'max'),
                                         平均工资=('salary', 'mean'), 最大值与均值插值=('salary', myfun)).rename_axis(
        ['行政区'])

    print(data5)
