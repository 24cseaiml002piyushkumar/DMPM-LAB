import numpy as np
n = int(input("Enter number of data points: "))
data = []
for i in range(n):
    data.append(float(input()))
print("Variance =", np.var(data))