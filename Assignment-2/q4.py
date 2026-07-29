import numpy as np
l=[int(x) for x in input("Enter the number:").split(",")]
median_with=np.median(l)
print(f"The median with using function:{median_with}")