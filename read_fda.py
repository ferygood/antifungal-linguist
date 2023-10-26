import pandas as pd

file_path="FDA_data/Products.txt"

df=pd.read_csv(file_path, sep="\t", header=0)

print(df.iloc[0,:])