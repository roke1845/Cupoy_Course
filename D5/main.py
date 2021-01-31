import numpy as np

english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

print("數學分數 ","平均",np.nanmean(math_score),"最大值",np.nanmax(math_score),"最小值",np.nanmin(math_score),"標準差",np.nanstd(math_score))
print("國文分數 ","平均",np.nanmean(chinese_score),"最大值",np.nanmax(chinese_score),"最小值",np.nanmin(chinese_score),"標準差",np.nanstd(chinese_score))
print("英文分數 ","平均",np.nanmean(english_score),"最大值",np.nanmax(english_score),"最小值",np.nanmin(english_score),"標準差",np.nanstd(english_score))

math_score[4]=55
print("補考數學後")
print("數學分數 ","平均",np.nanmean(math_score),"最大值",np.nanmax(math_score),"最小值",np.nanmin(math_score),"標準差",np.nanstd(math_score))

print("國文與數學相關係數",np.corrcoef(chinese_score,math_score))
print("國文與英文相關係數",np.corrcoef(chinese_score,english_score))