import pandas as pd
import openpyxl
import numpy as np


df = pd.read_excel(".//static//tab_client.xlsx")

data =[]
for i in range(df.shape[0]):
    linha=[]
    for j in range(df.shape[1]):
        linha.append(df.iloc[i,j])
    data.append(linha)


arr = np.array(data)
lista = arr.tolist()
sorted_data = dict(enumerate(lista[0]))



print(sorted_data)