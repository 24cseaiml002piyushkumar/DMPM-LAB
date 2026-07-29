n=[int(x) for x in input("Enter the number:").split(",")]
dict={}
for x in n:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
mode_without=max(dict,key=dict.get)
print(f"The mode without function:{mode_without}")
