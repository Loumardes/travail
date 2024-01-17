import os
import pandas as pd

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
filename = "test.ods"

df = pd.read_excel(path+"\\"+filename)




check_for_nan = df['motif'].isnull()
print (check_for_nan)

for x in df.index:
  if check_for_nan.loc[x]:
    df.drop(x, inplace = True)

"""
df.loc[df['motif'].isnull(),'value_is_NaN'] = 'Yes'
df.loc[df['motif'].notnull(), 'value_is_NaN'] = 'No'
"""


# export to an ods spreadsheet
data = pd.ExcelWriter(path+"\\"+"export.ods")
print(os.getcwd())
df.to_excel(data)
data.close()

print(df.to_string()) 