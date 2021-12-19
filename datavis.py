import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
d = px.scatter(df, x="date", y="cases", title="graph", color="country")
d.show()