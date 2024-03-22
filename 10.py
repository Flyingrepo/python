
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

import plotly  
figures at once 
import plotly.express as px  
fig = px.choropleth(locationmode="USA
states", color=[1], scope="usa") 
fig.show()



import pandas as pd 
import plotly.express as px 
data = 
pd.read_csv('2011_us_ag_exports.csv') 
fig = px.choropleth(data, locations='code',
 locationmode="USA-states", 
color='total exports', scope="usa") 
fig.show()
