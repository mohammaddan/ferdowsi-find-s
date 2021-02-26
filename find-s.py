import numpy as np
import pandas as pd

data=pd.read_csv('data.csv')
print(data)

h={"sky":'',"airtemp":'',"humidity":'',"wind":'',"water":'',"forcast":''}

for row in data.iterrows():
    if row[1].enjoysport=='yes':
        for d in row[1].to_dict():
            if d=='enjoysport':
                continue
            if h[d]=='':
                h[d]=row[1][d]
            elif h[d]!=row[1][d]:
                h[d]='?'

print(h.values())