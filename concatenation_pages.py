import pandas as pd

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
#filename = "test.ods"
#filename = "Historico disponibilidad y km.xlsx"
filename = "Madrid Analysed Test.ods"

parsed_pages = ['2019']#, '2020', '2021', '2022', '2023']
filtered_column = "responsible entity"

def read_page(file=path+"\\"+filename, page=""):
  df = pd.read_excel(file, page)
  return df

def remove_empty_rows(df, column):
    # remove the empty lines in the column
    check_for_nan = df[column].isnull()

    for x in df.index:
        if check_for_nan.loc[x]:
            df.drop(x, inplace = True)

def export(df, filename):
    # export to an ods spreadsheet
    data = pd.ExcelWriter(path+"\\"+filename)
    df.to_excel(data)
    data.close()

df_list = []
print("opening spreadsheet")
for x in parsed_pages:
    df_list.append(read_page(page=x))
    remove_empty_rows(df_list[-1], filtered_column)
    print("read page "+x)

print("concatenating")
df = pd.concat(df_list)
print("exporting")
export(df, "madrid_concaténé.ods")


#print(df.to_string()) 
