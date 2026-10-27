# TASK -> DATA -> MODELING ->Error Measurement -> Training & Optimization -> Performance Measurement -> Validating and Testing -> Corrective Measures
import tensorflow as tf #Model creating
import pandas as pd     #Reading data, Processing it, Manipulting data
import numpy as np  #COMPLEX MATHS
import seaborn as sb   #Vizualization

data=pd.read_csv("train.csv",",")
print(data)
print(data.head())
print(data.shape)
