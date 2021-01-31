import numpy as np

english_score = np.array([55, 89, 76, 65, 48, 70])

chinese_score = np.array([65, 90, 82, 72, 66, 77])
math_score = np.array([60, 85, 60, 68, 55, 60])


en_greater_ma = np.greater(english_score, math_score)
print(en_greater_ma)
print(np.sum(en_greater_ma))

ch_greater_ma = np.greater(chinese_score, math_score)
print(ch_greater_ma)
ch_greater_en = np.greater(chinese_score, english_score)
print(ch_greater_en)

print(np.logical_and(ch_greater_ma, ch_greater_en).all())
