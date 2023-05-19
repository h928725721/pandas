import pandas as pd
import numpy as np


def update():
    global data, data1, data2
    print('修改列名')
    data.rename(columns={'Unnamed: 0': '序号',
                         '金牌': '金牌数',
                         '银牌': '银牌数',
                         '铜牌': '铜牌数'}, inplace=True)
    print('修改索引名')
    data.set_index('排名', inplace=True)
    data.rename_axis('金牌排名', inplace=True)
    print('指定索引修改值')
    data.iloc[4, 1] = '俄罗斯'
    data['金牌数'].replace(0, '无', inplace=True)
    # 将‘无’或nan的值替换成0，inplace的作用是直接在原始值中修改
    data.replace(['无', np.nan], [0, 0], inplace=True)
    # fillna作用是将nan的值替换成0
    data['金牌数'] = data['金牌数'].fillna('0').astype(int)
    data['银牌数'] = data['银牌数'].fillna('0').astype(int)
    data['铜牌数'] = data['铜牌数'].fillna('0').astype(int)
    data['比赛地点'] = '东京'
    data.replace('None', 0, inplace=True)
    data['金银总数'] = data['金牌数'] + data['银牌数']
    # 从金银铜中找出最多的那个
    data['最多奖牌数'] = data.bfill()[['金牌数', '银牌数', '铜牌数']].max(1)
    # 按条件新增一列
    data['金牌大于30'] = np.where(data['金牌数'] > 30, '是', '否')
    # 增加多列
    data = data.assign(金铜牌总数=data.金牌数 + data.铜牌数,
                       银铜牌总数=data.银牌数 + data.铜牌数)
    # 新增列（引用变量）
    gold_sum = data['金牌数'].sum()
    data.eval(f'金牌占比 = 金牌数/{gold_sum}', inplace=True)
    # 删除第一行
    data1 = data.drop(1)
    # 删除条件行
    data2 = data.drop(data[data['金牌数'] < 20].index)
    print(data2)
    data.drop(columns=['比赛地点'], inplace=True)
    print(data)


if __name__ == '__main__':
    data = pd.read_excel('test.xlsx')
    # update()
    # 筛选第1,2,3,4列   : 代表所有行
    data1 = data.iloc[:, [0, 1, 2, 3]]

    # 根据列名提取
    data2 = data[['金牌', '银牌']]

    # 筛选全部奇数列
    data3 = data.iloc[:, [i % 2 == 1 for i in range(len(data.columns))]]

    # 条件（列名）
    data4 = data.loc[:, data.columns.str.endswith('牌')]

    # 组合（行号+列名）
    data5 = data.loc[10:20, '排名':]
    data5 = data.at[4, '金牌']
    # 固定间隔(第1到50行，间隔为3)
    data6 = data[0:50:3]

    # 筛选金牌> 10的
    data7 = data[data['金牌'] > 10]
    data7 = data.loc[data['金牌'] > 10]
    data7 = data.query('金牌+银牌 > 50')
    # 小于10的
    data8 = data.loc[~(data['金牌'] > 10)]

    # 条件指定值
    data9 = data.loc[data['代表团'].isin(['中国', '法国'])]

    # 条件（包含值）
    data0 = data[data.代表团.str.contains('中')]

    # 条件
    data11 = data.loc[data['代表团'] == '中国'].loc[1].at['金牌']
    print(data11)
