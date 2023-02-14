import pandas as pd
import openpyxl

df = pd.read_excel(".//static//tab_client.xlsx")

data =[]
for i in range(df.shape[0]):
    linha=[]
    for j in range(df.shape[1]):
        linha.append(df.iloc[i,j])
    data.append(linha)


sorted_data = data
#print(data)