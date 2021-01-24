import numpy as np

english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,55,60])

chinese_score = np.array([65,90,82,72,66,77])

print(np.greater(english_score, math_score))
