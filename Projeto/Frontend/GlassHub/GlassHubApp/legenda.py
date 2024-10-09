import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Criando o dataframe com as categorias
data = {
    'Categoria': ['Verde', 'Amarelo', 'Laranja', 'Vermelho'],
    'Duração (minutos)': [22.5, 45, 90, 120],  # Média das durações
    'Descrição': [
        'Paradas curtas que não afetam o fluxo de produção.',
        'Paradas moderadas que podem causar atrasos.',
        'Paradas críticas que comprometem o processo produtivo.',
        'Paradas graves que levam à paralisação completa.'
    ]
}

df = pd.DataFrame(data)

# Inicializando o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Classificação dos Tempos de Parada"),
    
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(
            df,
            x='Categoria',
            y='Duração (minutos)',
            color='Categoria',
            text='Descrição',
            title='Classificação de Paradas na Produção de Vidros',
            labels={'Duração (minutos)': 'Duração Média (minutos)'},
            template='plotly_dark'
        ).update_traces(textposition='auto')
    ),
    
    html.Div([
        html.H3("Descrição das Categorias"),
        html.Ul([
            html.Li(f"{row['Categoria']}: {row['Descrição']}") for index, row in df.iterrows()
        ])
    ])
])

# Rodando o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
