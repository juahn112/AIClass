import matplotlib.pyplot as plt
import numpy as np

study_hours = np.array([1,2,3,4,5])
scores = np.array([50,55,65,70,80])

plt.scatter(study_hours, scores)
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.title('Study vs Score')
plt.show()