import pandas as pd
import numpy as np

score_df = pd.DataFrame([[1,50,80,70,'boy'],
              [2,60,45,50,'boy'],
              [3,98,43,55,'boy'],
              [4,70,69,89,'boy'],
              [5,56,79,60,'girl'],
              [6,60,68,55,'girl'],
              [7,45,70,77,'girl'],
              [8,55,77,76,'girl'],
              [9,25,57,60,'girl'],
              [10,88,40,43,'girl']],columns=['student_id','math_score','english_score','chinese_score','sex'])
score_df = score_df.set_index('student_id')
# print(score_df)
#
#
# boy_score_df = score_df.loc[score_df.sex=='boy']
# print(boy_score_df.mean())
#
# print(score_df.groupby('sex').mean())
#
# score_df['class'] = [1,2,1,2,1,2,1,2,1,2]
# print(score_df)
#
# print(score_df.groupby(['sex','class']).mean())
#
# print(score_df.groupby(['sex']).agg(['mean','std']))
#
# print(score_df.groupby(['sex','class']).agg(['mean','max']))
#
# print(score_df.groupby(['sex','class']).describe())


def homework():
    score_df = pd.DataFrame([[1, 50, 80, 70, 'boy', 1],
                             [2, 60, 45, 50, 'boy', 2],
                             [3, 98, 43, 55, 'boy', 1],
                             [4, 70, 69, 89, 'boy', 2],
                             [5, 56, 79, 60, 'girl', 1],
                             [6, 60, 68, 55, 'girl', 2],
                             [7, 45, 70, 77, 'girl', 1],
                             [8, 55, 77, 76, 'girl', 2],
                             [9, 25, 57, 60, 'girl', 1],
                             [10, 88, 40, 43, 'girl', 3],
                             [11, 25, 60, 45, 'boy', 3],
                             [12, 80, 60, 23, 'boy', 3],
                             [13, 20, 90, 66, 'girl', 3],
                             [14, 50, 50, 50, 'girl', 3],
                             [15, 89, 67, 77, 'girl', 3]],
                            columns=['student_id', 'math_score', 'english_score', 'chinese_score', 'sex', 'class'])
    score_df = score_df.set_index('student_id')

    # Q1
    # print(score_df.agg(['max','min']))
    # print(score_group_df.agg(['max','min']))

    # Q2
    score_group_df = score_df.groupby(['class'])
    print(score_group_df['math_score'].mean()) #2
    new = score_df.groupby(['class']).mean()
    print(new[new['math_score'] == new.max()['math_score']].index)
    print(score_df.groupby('class').mean()['math_score'].idxmax())

    # Q3
    diff = score_df[['chinese_score', 'sex']].groupby('sex').mean()
    print(diff.iloc[0])
    print(diff.iloc[0] - diff.iloc[1])
    # print(score_df.groupby('sex').mean())
    # a = score_df.groupby('sex').mean()
    # a['new'] = a['chinese_score'].shift(-1)
    #
    # print(a)
    # print(a['new'] - a['chinese_score'])

homework()