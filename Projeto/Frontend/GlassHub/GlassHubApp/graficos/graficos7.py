import plotly.graph_objects as go

# Data for the stacked bar chart
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
blue_data = [20000, 30000, 25000, 35000, 40000, 15000, 20000, 25000, 30000, 50000, 40000, 45000]
gray_data = [40000, 50000, 60000, 80000, 70000, 50000, 60000, 70000, 60000, 110000, 90000, 120000]

# Create the stacked bar chart
fig = go.Figure(data=[
    go.Bar(name='Blue Data', x=x, y=blue_data, marker_color='blue'),
    go.Bar(name='Gray Data', x=x, y=gray_data, marker_color='gray')
])

# Update the layout for stacked bars
fig.update_layout(barmode='stack', 
                  title='Stacked Bar Chart Example',
                  xaxis_title='Months',
                  yaxis_title='Values')

# Display the chart
fig.show()
