from sklearn.linear_model import LinearRegression
import numpy as np

study_hours = np.array([[1],[2],[3],[4],[5]])
scores = np.array([50,55,65,70,80])

model = LinearRegression()
model.fit(study_hours, scores)

X_test = np.array([[6]])
prediction = model.predict(X_test)
print(prediction)