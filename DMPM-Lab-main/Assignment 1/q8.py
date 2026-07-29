# write a program to find th sum of digits of a number
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print("The sum of digits of the number is:", sum_of_digits)