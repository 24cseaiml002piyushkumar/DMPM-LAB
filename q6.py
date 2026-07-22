# write a program to count vowels in a string
string = input("Enter a string: ")
vowels = [l for l in string if l in 'aeiouAEIOU']
print("The number of vowels in the string is:", len(vowels))