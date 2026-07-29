import numpy as np 
n=[int(x) for x in input("Enter the number:").split(",")]
mean=sum(n)/len(n)
sum_squared_diff=sum((x-mean)**2 for x in n)
sd=(sum_squared_diff/len(n))**0.5
print(f"standard deviation without function:{sd:4f}")
n2=np.array(n)
sd=np.std(n2)
print(f"Standard deviation with function:{sd:4f}")
