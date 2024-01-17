import os
import pandas as pd

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
filename = "Historico disponibilidad y km.xlsx"


df = pd.read_excel(path+"\\"+filename, '2019')
"""
for x in df.index:
  if df.loc[x, "b"] == 0:
    df.drop(x, inplace = True)"""

print(df.to_string()) 