import numpy as np

study_hours = np.array([1,2,3,4,5])
scores = np.array([50,55,65,70,80])

avgStudyHours = np.mean(study_hours)
avgScores = np.mean(scores)

corr_matrix = np.corrcoef(study_hours,scores)
correlation = corr_matrix[0,1]

print(avgStudyHours)
print(avgScores)
print(corr_matrix)
print(correlation)