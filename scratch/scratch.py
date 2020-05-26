import pandas as pd
import numpy as np

df = pd.DataFrame([[1, np.nan, '3'], [4, 5, '6'], [7, 9, np.nan]],
                   columns=['a', 'b', 'c'])

print(df)