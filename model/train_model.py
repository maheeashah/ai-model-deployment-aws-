import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Generate dummy data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')

print("Model trained and saved as model.pkl")
