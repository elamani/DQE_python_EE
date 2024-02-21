import numpy as np
import pandas as pd
# generating random numbers till 1000 of size 100
num = np.random.randint(1000,size = 100)
res = pd.Series(num)
print(list(res))