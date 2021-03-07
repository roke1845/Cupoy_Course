import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
data = np.round(np.random.randn(4, 6), 1)
df = pd.DataFrame(data, index=index, columns=columns)

# print(df)
# 直接將column轉成index (從第一個column開始轉換)
# print(df.stack().stack())

# 將index轉乘column (最外面的index)
# print(df.unstack())

df = pd.DataFrame({'Name':{0:'John', 1:'Bob', 2:'Shiela'},
                   'Course':{0:'Masters', 1:'Graduate', 2:'Graduate'},
                   'Age':{0:27, 1:23, 2:21}})

# print(df)

# print(df.melt())

#保留某column, 其餘column轉換成value
# print(df.melt(id_vars='Name'))

#只將某column轉換成value, 其餘column不轉換
# print(df.melt(value_vars='Name'))

df = pd.DataFrame({'fff': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bbb': ['P', 'Q', 'R', 'P', 'Q', 'R'],
                   'baa': [2, 3, 4, 5, 6, 7],
                   'zzz': ['h', 'i', 'j', 'k', 'l', 'm']})

# print(df)

#重新定義dataframe(重組資料) => 指定index與column與value
# print(df.pivot(index='fff', columns='bbb', values='zzz'))


def homework():
    score_df = pd.DataFrame(
        [[1, 50, 80, 70, 'boy', 1], [2, 60, 45, 50, 'boy', 2], [3, 98, 43, 55, 'boy', 1], [4, 70, 69, 89, 'boy', 2],
         [5, 56, 79, 60, 'girl', 1], [6, 60, 68, 55, 'girl', 2], [7, 45, 70, 77, 'girl', 1], [8, 55, 77, 76, 'girl', 2],
         [9, 25, 57, 60, 'girl', 1], [10, 88, 40, 43, 'girl', 3], [11, 25, 60, 45, 'boy', 3],
         [12, 80, 60, 23, 'boy', 3], [13, 20, 90, 66, 'girl', 3], [14, 50, 50, 50, 'girl', 3],
         [15, 89, 67, 77, 'girl', 3]],
        columns=['student_id', 'math_score', 'english_score', 'chinese_score', 'sex', 'class'])
    df = score_df.melt(id_vars=['sex','class', 'student_id'])
    print(score_df)
    print(df)
    # print(score_df)
    print(df.pivot(index=['sex','class', 'student_id'],columns='variable',values='value'))
homework()