from datetime import *

import spreadsheet_reader as sr

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
filename = "test.ods"

"""
time.fromisoformat('04:23:01')
print(date.fromisoformat('20191204'))
print(date.fromisoformat('01/09/2019'.replace("/", "-")))
"""


t = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(t)


dt = sr.read_page(page="a")
dt = sr.remove_empty_rows(dt, "motif")
print(dt.to_string())
dt = dt[dt["motif"].notnull()]
print(dt.to_string())

row = dt.loc[0]
print(row)

t = datetime.combine(row["date"], dt.loc[0]["time"])
print(t)


