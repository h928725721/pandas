
import pandas as pd

# DataFrame类似于表 ，使用pd.DataFrame构造
# Series类似于表中的列，使用df['xxx]或者pd.Series[]构造
if __name__ == '__main__':
    df = pd.DataFrame({"Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth", ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"], })


    print(df)
    print()
    print(df['Age'])
    print()
    #进行数据分析的函数
    print(df['Age'].max())
    print()
    print(df.describe())