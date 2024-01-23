# -*- coding: utf-8 -*-

import pandas as pd

path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
filename = "test.ods"


def read_page(file=path+"\\"+filename, page=""):
  df = pd.read_excel(file, page)
  return df

def remove_empty_rows(df, column):
    return df[df[column].notnull()]

def remove_empty_rows_Old(df, column):
    check_for_nan = df[column].isnull()
    for x in df.index:
      if check_for_nan.loc[x]:
        df.drop(x, inplace = True)
    return df

def export(df, filename):
    # export to an ods spreadsheet
    data = pd.ExcelWriter(path+"\\"+filename)
    df.to_excel(data)
    data.close()
