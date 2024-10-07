import plotly.graph_objects as go

# Definir os dados para o gráfico
labels = ["Property 1", "Property 2", "Property 3", "Property 4", 
          "Subprop 1.1", "Subprop 1.2", "Subprop 2.1", "Subprop 2.2", 
          "Subprop 3.1", "Subprop 3.2", "Subprop 3.3"]

parents = ["", "", "", "", 
           "Property 1", "Property 1", "Property 2", "Property 2", 
           "Property 3", "Property 3", "Property 3"]

values = [10, 15, 50, 20, 
          3, 10, 8, 15, 
          8, 2, 50]

# Criar o gráfico de treemap
fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents,
    values = values,
    textinfo = "label+value",
    marker_colors = ['lightblue', 'orange', 'orange', 'orange', 
                     'lightpink', 'lightpink', 'lightblue', 'orange', 
                     'lightpink', 'lightblue', 'orange']
))

# Ajustar o layout do gráfico
fig.update_layout(
    title="Treemap Exemplo",
    margin = dict(t=50, l=25, r=25, b=25)
)

# Exibir o gráfico
fig.show()
