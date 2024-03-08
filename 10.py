# Using plotly.express
import plotly.express as
px
df = px.data.stocks()
fig = px.line(df,
x='date', y="GOOG")
fig.show(

import plotly.express as
px
df =
px.data.stocks(indexed=T
rue)-1
fig = px.bar(df,
x=df.index, y="GOOG")
fig.show()