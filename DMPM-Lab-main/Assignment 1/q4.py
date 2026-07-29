#write a program to check whether a string is a palindrome

string = input("Enter a string: ")
flag = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        flag = False
        break
if flag:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")