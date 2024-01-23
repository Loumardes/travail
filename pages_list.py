import os
import pandas as pd

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
#filename = "Historico disponibilidad y km.xlsx"
filename = "failure_grouping_test.ods"

xls = pd.ExcelFile(path+"\\"+filename)
print(xls.sheet_names)
