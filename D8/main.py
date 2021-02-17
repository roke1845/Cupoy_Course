import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

dt = np.dtype({'names':('name', 'sex', 'weight', 'rank', 'myopia'), 'formats':('U100', 'U100', float, int, '?')})

a = np.zeros(8,dt)

a['name'] = name_list
a['sex'] = sex_list
a['weight'] = weight_list
a['rank'] = rank_list
a['myopia'] = myopia_list
# print(a)
print('平均體重為:' + str(sum(a['weight'])/len(a['weight'])))
print('男生平均體重為:' + str(sum(a[a['sex'] == 'boy']['weight'])/len(a[a['sex'] == 'boy']['weight'])))
print('女生平均體重為:' + str(sum(a[a['sex'] == 'girl']['weight'])/len(a[a['sex'] == 'girl']['weight'])))