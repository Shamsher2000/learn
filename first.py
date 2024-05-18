import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\shamsher\Desktop\headbrain.csv')
print(data.shape)
data.head()
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)
print(mean_x)
print(mean_y)
# Total number of values
n = len(X)
print(n)
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)
# Printing coefficients
print("Coefficients")
print(b1, b0)
max_x = np.max(X) + 100
min_x = np.min(X) - 100
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x
# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()