import pandas as pd
data={"age":["25","30","45","23"]}
df=pd.DataFrame(data)
print(df)
# to convert it into int
df["age"]=df["age"].astype(int)
print(df)