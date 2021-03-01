import pandas as pd

q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])
q_df = q_df.fillna('others')
print(q_df)

pf = pd.get_dummies(q_df[['Profession']])
q_df = pd.concat([q_df, pf], axis=1)
print(q_df)