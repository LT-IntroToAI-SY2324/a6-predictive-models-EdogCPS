import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)

# Print out the linear equation and r squared value
print(f"Model's Linear Equation: y = {coef}x + {intercept}")
print(f"R Squared value: {r_squared}")

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction
x_predict = 43
prediction = model.predict([[x_predict]])
print(f"The predicted blood presure of somebody {x_predict} years old is {prediction} mmHg.")

# Create the model in matplotlib and include the line of best fit
plt.figure(figsize=(6,4))
plt.scatter(x,y, c="purple")
plt.scatter(x_predict, prediction, c="blue")

plt.xlabel("Age in years")
plt.ylabel("Blood Presure in mmHg")
plt.title("Blood Presuue in mmHg by Age in years")

plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()
