import plotly.graph_objects as go

# Dados de exemplo
x = ['Option 1', 'Option 2', 'Option 3']
y1 = [80, 95, 120]  # Valores para o primeiro grupo
y2 = [90, 110, 130]  # Valores para o segundo grupo

# Erros associados a cada barra
error_y1 = [10, 15, 12]  # Erro para o primeiro grupo
error_y2 = [8, 10, 15]   # Erro para o segundo grupo

# Criar gráfico de barras
fig = go.Figure(data=[
    go.Bar(name='Grupo 1', x=x, y=y1, error_y=dict(type='data', array=error_y1), marker_color='red'),
    go.Bar(name='Grupo 2', x=x, y=y2, error_y=dict(type='data', array=error_y2), marker_color='lightblue')
])

# Atualizar o layout do gráfico
fig.update_layout(
    title='Exemplo de Gráfico de Barras com Erro',
    xaxis_title='Opções',
    yaxis_title='Valores',
    barmode='group'  # Colocar barras lado a lado
)

# Exibir o gráfico
fig.show()
