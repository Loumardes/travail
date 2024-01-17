import os
import pandas as pd

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
filename = "Historico disponibilidad y km.xlsx"

xls = pd.ExcelFile(path+"\\"+filename)
print(xls.sheet_names)
