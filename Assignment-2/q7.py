n = int(input("Enter number of data points: "))
data = []
total = 0
for i in range(n):
    x = float(input())
    data.append(x)
    total += x
mean = total / n
var = 0
for x in data:
    var += (x - mean) ** 2
var = var / n
print("Variance =", var)