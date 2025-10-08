import pandas as pd
pessoas = pd.read_csv("pessoas.csv")
gostos = pd.read_csv("gostos.csv")
Df_final = pd.merge(pessoas, gostos)
print(Df_final.head())