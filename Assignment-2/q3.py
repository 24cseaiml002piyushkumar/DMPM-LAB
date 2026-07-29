n = int(input("Enter number of data points: "))
data = []
for i in range(n):
    data.append(float(input()))
data.sort()
if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]
print("Median =", median)
