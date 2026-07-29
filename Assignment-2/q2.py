import numpy as np
n = int(input("Enter the number of data points: "))
data = []
for i in range(n):
    num = float(input("Enter data point: "))
    data.append(num)
average = np.mean(data)
print("Average (Mean):", average)