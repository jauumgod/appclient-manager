import pandas as pd
import openpyxl
import seaborn as sns

dados = pd.read_excel(".//static//tab_client.xlsx")



print(dados.mean(0))

cliente = []
cnpj =[]

for chaves in dados.values:
    cliente.append(chaves[1][1])

print(cliente)