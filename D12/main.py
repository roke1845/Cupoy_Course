import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('boston.csv')
data.boxplot()
# print(data.median().between(300,400))

data.plot.scatter(x='RM', y='LSTAT')
plt.show()