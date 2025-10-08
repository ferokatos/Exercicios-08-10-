import pandas as pd
pessoas = pd.read_csv("pessoas.csv")
gostos = pd.read_csv("gostos.csv")
Df_final = pd.merge(pessoas, gostos)
Df_final.to_csv("DataframeFinal.csv",index=False)