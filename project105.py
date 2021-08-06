import pandas as pd
import plotly.express as px
import statistics as stat
import math

df = pd.read_csv("class2.csv")
print(df)

mean = stat.mean(df["Marks"].tolist())
print(mean)

sum = 0
marks_list = df["Marks"].tolist()
for x in marks_list:
    s = (x - mean)*(x - mean)
    sum = sum + s

sd = sum/len(marks_list)
standarddeviation = math.sqrt(sd)
print(standarddeviation)