import plotly.graph_objects as go
import plotly.io as pio

def criar_grafico_barras_empilhadas():
    # Dados para o gráfico de barras empilhadas
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    blue_data = [20000, 30000, 25000, 35000, 40000, 15000, 20000, 25000, 30000, 50000, 40000, 45000]
    gray_data = [40000, 50000, 60000, 80000, 70000, 50000, 60000, 70000, 60000, 110000, 90000, 120000]

    # Criar o gráfico de barras empilhadas
    fig = go.Figure(data=[
        go.Bar(name='Blue Data', x=x, y=blue_data, marker_color='blue'),
        go.Bar(name='Gray Data', x=x, y=gray_data, marker_color='gray')
    ])

    # Atualizar o layout para barras empilhadas
    fig.update_layout(
        barmode='stack', 
        title='Exemplo de Gráfico de Barras Empilhadas',
        xaxis_title='Meses',
        yaxis_title='Valores'
    )

    # Salva o gráfico como HTML para embutir no template
    graph_html = pio.to_html(fig, full_html=False)

    return graph_html
