import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("pj_107.csv")
mean = df.groupby(["Marks In Percentage","Days Present"], as_index=False)["Roll No"].mean()
fig = px.scatter(mean, x="Marks In Percentage", y="Days Present", size ="Roll No", color ="Roll No")
fig.show()