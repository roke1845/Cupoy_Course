import pandas as pd

iris_data = pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
iris_data.to_excel('homework.xlsx')
print(iris_data)

print(pd.read_excel('homework.xlsx',engine='openpyxl'))