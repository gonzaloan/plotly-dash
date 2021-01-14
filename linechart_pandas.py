import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/nst-est2017-alldata.csv')


#Extract some data, where division is equals to 1
df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True) #Seteamos el index como la columna name
#print(df2)
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]
#print(df2.index)

for name in df2.index:
    print('columns',df2.columns)
    print('dfloc', df2.loc[name])
    print('name', name)
    print('*'*24)

data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode='lines',
                   name=name) for name in df2.index] #Index are connecticut, Maine, etc

pyo.plot(data)