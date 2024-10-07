import plotly.express as px
import pandas as pd

# Exemplo de dados de estados e valores (use os seus dados aqui)
data = {
    'state': ['CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI', 'NJ', 'VA', 'WA', 'AZ', 'MA'],
    'value': [39538223, 29145505, 21538187, 20201249, 12812508, 13002700, 11799448, 10711908, 10439388, 10077331, 9288994, 8631393, 7693612, 7151502, 7029917]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Gerar gráfico de bolhas
fig = px.scatter(df, x='state', y='value', size='value', hover_name='state', 
                 title="Bubble Chart of States",
                 labels={"state": "State", "value": "Value"})

# Mostrar gráfico
fig.show()
