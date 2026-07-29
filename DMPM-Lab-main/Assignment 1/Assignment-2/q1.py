l=int(input("Enter the number of data points:"))
total=0
for i in range(l):
    num=float(input("enter the data point:"))
    total=total+num
mean=total/num
print("Mean=",mean)