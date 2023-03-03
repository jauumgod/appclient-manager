import pandas as pd
import openpyxl
import numpy as np


df = pd.read_excel(".//static//tab_client.xlsx")


def read_data(arquivo):
    data = []
    for i in range(arquivo.shape[0]):
        linha=[]
        for j in range(arquivo.shape[1]):
            linha.append(arquivo.iloc[i,j])
        data.append(linha)

    arr = np.array(data)
    lista = arr.tolist()
    sorted_data = dict(enumerate(lista[0]))

    return sorted_data

read_data(df)

