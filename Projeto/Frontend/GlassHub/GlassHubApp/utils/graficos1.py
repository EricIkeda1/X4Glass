import plotly.graph_objects as go

# Define the data
quarters = ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4']
values_1 = [75, 50, 90, 50]
values_2 = [50, 75, 125, 100]
values_3 = [25, 100, 100, 75]
values_4 = [50, 125, 150, 75]

# Create a bar chart with grouped bars
fig = go.Figure(data=[
    go.Bar(name='1', x=quarters, y=values_1, marker_color='#FDB813'),
    go.Bar(name='2', x=quarters, y=values_2, marker_color='#F59BBD'),
    go.Bar(name='3', x=quarters, y=values_3, marker_color='#6CC2BD'),
    go.Bar(name='4', x=quarters, y=values_4, marker_color='#00457C')
])

# Update layout
fig.update_layout(
    title="Vertical bars",
    xaxis_title="Legend",
    yaxis_title="Title",
    barmode='group',
    legend_title_text="Legend"
)

# Show the plot
fig.show()
