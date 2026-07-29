import numpy as np
n = int(input("Enter number of data points: "))
data = []
for i in range(n):
    data.append(float(input(f"Enter data point {i+1}: ")))
print("Variance =", np.var(data))
print("Standard Deviation =", np.std(data))