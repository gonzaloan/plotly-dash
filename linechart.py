import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(56)

# evenly spaces values, de 0 a 1, 100 valores
x_values = np.linspace(0, 1, 100)
y_values = np.random.rand(100)  # 100 random values

# line chart = trace
trace0 = go.Scatter(x=x_values, y=y_values + 5,  # add 5 to every value in random
                   mode='markers', name='markers')

trace1 = go.Scatter(x=x_values, y=y_values,
                   mode='lines', name='my lines')

trace2 = go.Scatter(x=x_values, y=y_values-5, #Se suma o resta para que no estén donde mismo los gráficos
                   mode='lines+markers', name='my markers+lines')
data = [trace0, trace1, trace2]

layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
