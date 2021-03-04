import pandas as pd
score_df = pd.DataFrame([[1,56,66,70],
              [2,90,45,34],
              [3,45,32,55],
              [4,70,77,89],
              [5,56,80,70],
              [6,60,54,55],
              [7,45,70,79],
              [8,34,77,76],
              [9,25,87,60],
              [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
score_df = score_df.set_index('student_id')

print(score_df.mean(axis=1)[5:6])
score_df_mean = score_df.mean(axis=1)
print(score_df_mean.median())

new_score_df = score_df.apply(lambda x : x**(0.5)*10)
print(new_score_df)

print(new_score_df.mean())
