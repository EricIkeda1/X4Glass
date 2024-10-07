import plotly.graph_objects as go
import plotly.io as pio

def criar_grafico():
    # Dados fictícios - substitua pelos seus dados reais
    x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    group1_y = [10, 15, 13, 17, 20, 23, 24, 25, 28, 30]
    group2_y = [16, 18, 19, 21, 22, 25, 27, 29, 30, 34]
    group3_y = [12, 14, 15, 18, 19, 21, 23, 26, 28, 32]
    group4_y = [22, 25, 28, 30, 33, 36, 38, 42, 45, 50]

    # Criando os traces (linhas) para cada grupo
    trace1 = go.Scatter(x=x_values, y=group1_y, mode='lines', name='Group 1', line=dict(color='purple'))
    trace2 = go.Scatter(x=x_values, y=group2_y, mode='lines', name='Group 2', line=dict(color='blue'))
    trace3 = go.Scatter(x=x_values, y=group3_y, mode='lines', name='Group 3', line=dict(color='green'))
    trace4 = go.Scatter(x=x_values, y=group4_y, mode='lines', name='Group 4', line=dict(color='yellow'))

    # Organizando os dados
    data = [trace1, trace2, trace3, trace4]

    # Configurando o layout
    layout = go.Layout(
        title='Exemplo de Gráfico',
        xaxis=dict(title='Eixo X'),
        yaxis=dict(title='Eixo Y'),
    )

    # Criando a figura
    fig = go.Figure(data=data, layout=layout)

    # Salva o gráfico como HTML para ser embutido no template
    graph_html = pio.to_html(fig, full_html=False)

    return graph_html
