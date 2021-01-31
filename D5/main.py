import numpy as np

english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

all = np.vstack((english_score, math_score, chinese_score))

print(np.nanmean(all, axis=0))
print(np.nanmax(all, axis=0))
print(np.nanmax(all, axis=0))
print(np.nanstd(all, axis=0))

all[1][4]=55

print(np.nanmean(all, axis=0))
print(np.nanmax(all, axis=0))
print(np.nanmax(all, axis=0))
print(np.nanstd(all, axis=0))
