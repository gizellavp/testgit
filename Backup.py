import gspread
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cobaapi.json", scope)

gc = gspread.authorize(creds)

wk = gc.open('Contact').sheet1
wk1 = gc.open('Contact').worksheet('Sheet2')

data = wk.get_all_records()  # Get a list of all records
data1 = wk1.get_all_records()

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)


#df.loc[(df['Nama'] == 'maria')]
#df.loc[2, ['Nilai1']] = ['100']
#set_with_dataframe(wk, df)
print(df)



#print(df)
#print(df['Nama'])
#print(df.head(5))
#print(df.columns)
#print(df[['Nama', 'Nilai2']])
"""
df1 = df[['Nama', 'Nilai2']]
print(df1.loc[(df['Nilai2'] < 90)])
"""
#df1.update(['Nilai1'], '80')
#wk.update_cell(2,2, '67')
#df = pd.DataFrame(data)
#print(df.count())

#Sum = df['Nilai1'] + df['Nilai2']
#print(Sum)

#print(df.merge(df1, right_on='Nama', left_on='Nama'))

#print(df.iloc[2])

#concat = pd.concat([df, df1], ignore_index=True)
#print(concat)

#concat = pd.concat([df, df1], axis=0, join= 'inner')
#print(concat)

#inner = pd.merge(df, df1, on=['Nama'])
#print(inner)

#left = pd.merge(df, df1, on=['Nama'], how='left')
#print(left)

#outer = pd.merge(df, df1, on=['Nama'], how='outer')
#print(outer)

#right = pd.merge(df, df1, on=['Nama'], how='right')
#print(right)



