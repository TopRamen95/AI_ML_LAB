#!/usr/bin/env python
# coding: utf-8

# # Edited

# In[5]:


import matplotlib.pyplot as plt
import numpy as np


# In[7]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
num_friends_good = [1, 2, 3, 4, 5]
daily_minutes_good = [2, 4, 5, 4, 5]

# Calculate the least squares fit (slope and intercept)
x_mean = np.mean(num_friends_good)
y_mean = np.mean(daily_minutes_good)
numerator = sum((x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(num_friends_good, daily_minutes_good))
denominator = sum((x_i - x_mean) ** 2 for x_i in num_friends_good)
beta = numerator / denominator
alpha = y_mean - beta * x_mean

# Create the best-fitting line
x_values = np.linspace(min(num_friends_good), max(num_friends_good), 100)
y_values = alpha + beta * x_values

# Scatter plot
plt.scatter(num_friends_good, daily_minutes_good, label="Data points")
plt.plot(x_values, y_values, color='red', label="Best-fitting line")

plt.xlabel("Number of Friends")
plt.ylabel("Daily Minutes Spent")
plt.title("Linear Regression: Friends vs. Daily Minutes")
plt.legend()
plt.grid(True)
plt.show()


# # Original 

# In[9]:


def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))

def least_squares_fit(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    numerator = sum((x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y))
    denominator = sum((x_i - x_mean) ** 2 for x_i in x)
    beta = numerator / denominator
    alpha = y_mean - beta * x_mean
    return alpha, beta

# Sample data (replace with your actual data)
num_friends_good = [1, 2, 3, 4, 5]
daily_minutes_good = [2, 4, 5, 4, 5]

alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)
print("Slope (beta):", beta)
print("Intercept (alpha):", alpha)

# Predictions for a new data point
new_x = 6
predicted_y = predict(alpha, beta, new_x)
print(f"Predicted value for x = {new_x}: {predicted_y:.2f}")


# In[ ]:




