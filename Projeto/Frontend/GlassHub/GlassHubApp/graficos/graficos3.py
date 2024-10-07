import plotly.graph_objects as go
import plotly.io as pio

def criar_grafico():
    # Dados de exemplo
    options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6', 'Option 7', 'Option 8', 'Option 9', 'Option 10']
    y_values1 = [40, 45, 50, 55, 52, 48, 50, 55, 53, 54]  # Valores do Grupo 1
    y_values2 = [20, 25, 30, 35, 32, 28, 30, 35, 33, 34]  # Valores do Grupo 2
    error_y1 = [3, 2, 4, 3, 2, 3, 4, 2, 3, 4]  # Erros do Grupo 1
    error_y2 = [1, 2, 1, 3, 2, 1, 2, 1, 2, 1]  # Erros do Grupo 2

    # Trace 1 (Grupo 1)
    trace1 = go.Scatter(
        x=options,
        y=y_values1,
        mode='lines+markers',
        name='Group 1',
        line=dict(color='blue'),
        error_y=dict(type='data', array=error_y1),  # Adiciona barras de erro
    )

    # Trace 2 (Grupo 2)
    trace2 = go.Scatter(
        x=options,
        y=y_values2,
        mode='lines+markers',
        name='Group 2',
        line=dict(color='orange'),
        error_y=dict(type='data', array=error_y2),  # Adiciona barras de erro
    )

    # Layout
    layout = go.Layout(
        title='Título do Gráfico',
        xaxis=dict(title='Options'),
        yaxis=dict(title='Title', range=[0, 60]),
        showlegend=True
    )

    # Figura final
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Salva o gráfico como HTML para embutir no template
    graph_html = pio.to_html(fig, full_html=False)

    return graph_html
