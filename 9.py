import plotly.express as px
df = px.data.iris()
fig = px.scatter_3d(df, x =
'sepal_width',
y = 'sepal_length',
z = 'petal_width', color = 'species')
fig.show()

import plotly.graph_objects as go
import numpy as np
# Helix equation
t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t
fig = go.Figure(data=[go.Scatter3d(x=x, y=y,
z=z, mode='markers')])
fig.show()