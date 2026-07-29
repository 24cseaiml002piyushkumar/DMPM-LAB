n=[int(x) for x in input("Enter the number:").split(",")]
import numpy as np
mode_with=np.bincount(n).argmax()
print(f"The mode with using function:{mode_with}")