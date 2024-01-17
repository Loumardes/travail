import pandas as pd
import numpy as np

data = {'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan]}
df = pd.DataFrame(data)

check_for_nan = df['set_of_numbers'].isnull()
print (check_for_nan)