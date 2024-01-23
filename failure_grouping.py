# -*- coding: utf-8 -*-

# groups failures :
# guideways if less than 24h between them
# trains if same number and less than 24h between them

# 1h delay for other types
# do not log aena errors (client induced errors)

import numpy as np
import pandas as pd
from datetime import * 
import json

import spreadsheet_reader as sr


path = "C:\\Users\\Louis GLANDIERES\\Documents\\stages\\Alstom\\travail"
#filename = "failure_grouping_test.ods"
filename = "Historico disponibilidad y km.xlsx"

parsed_pages = ['2019', '2020']#, '2021', '2022', '2023']

with open('config.json') as configFile:
    configData = json.load(configFile)

column_name = configData["columns"]

print(column_name["event_start"])


# todo delay for error types

class TrainError:
    def __init__(self, type, start, end, train=np.nan):
        self.type = type
        self.start = start 
        self.end = end
        self.train = train

trainErrors = []
activeTrainErrors = []


def find_matching_TrainError(row):
    

    #print("cycle errors")
    event_time = datetime.combine(row[column_name["date"]], row[column_name["event_start"]])
    for x in range(len(activeTrainErrors)-1, -1, -1) :
        #print(row["Hora Inicio"], row["Clasificación BT"], row["Convoy"])
              

        if ((event_time - activeTrainErrors[x].end) < timedelta(hours=1) and 
            activeTrainErrors[x].type == row[column_name["error_type"]] and
            (row["TrainNull"] or activeTrainErrors[x].train == row[column_name["train"]])):
            return activeTrainErrors[x]
        
        elif (activeTrainErrors[x].end - event_time) > timedelta(hours=1):
            del activeTrainErrors[x]
    return False

"""
df_list = []
print("opening spreadsheet")
for x in parsed_pages:
    df_list.append(sr.read_page(path+"\\"+filename, page=x))
    sr.remove_empty_rows(df_list[-1], "Clasificación BT")
    print("read page "+x)

print("concatenating")
df = pd.concat(df_list, ignore_index=True)

print("exporting")
#print(df.to_string())
sr.export(df, "page_group_test.ods")
"""

df = sr.read_page(path+"\\"+filename, page='2023')
df = sr.remove_empty_rows(df, column_name["error_type"])

# add a column for wether or not the error contains a train
df["TrainNull"] = df[column_name["train"]].isnull()

for x in df.index:
    row = df.loc[x]
    #print(df.loc[x])
    #print(row["Fecha"], row["Hora Final"])


    start_time = datetime.combine(row[column_name["date"]], row[column_name["event_start"]])
    end_time = datetime.combine(row[column_name["date"]], row[column_name["event_end"]])

    matching_TrainError = find_matching_TrainError(row)
    if matching_TrainError:
        matching_TrainError.end = end_time
    else :    
        activeTrainErrors.append(TrainError(row[column_name["error_type"]], start_time, end_time, train=row[column_name["train"]]))
        trainErrors.append(activeTrainErrors[-1])


dataframeTemplate = {"Start Time" : [], "End Time" : [], "Error Type" : [], "Train" : []}
for x in trainErrors:
    dataframeTemplate["Start Time"].append(x.start.ctime())
    dataframeTemplate["End Time"].append(x.end.ctime())
    dataframeTemplate["Error Type"].append(x.type)
    dataframeTemplate["Train"].append(x.train)

OutputDataFrame = pd.DataFrame(dataframeTemplate)

sr.export(OutputDataFrame, "failure_grouping.ods")

print(trainErrors)
