# write a program to find the factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("The factorial of the number is:", fact)
