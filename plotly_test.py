import plotly.graph_objects as go

# Create a list of nodes
nodes = [
    go.Scatterpolar(
        r=[0],  # Distance from the center of the plot
        theta=[0],  # Angular position
        mode='markers',
        marker=dict(size=15, color='blue')
    ),
    go.Scatterpolar(
        r=[1],
        theta=[90],
        mode='markers',
        marker=dict(size=15, color='blue')
    ),
    go.Scatterpolar(
        r=[1],
        theta=[45],
        mode='markers',
        marker=dict(size=15, color='blue')
    ),
    # Add more nodes as needed
]

# Create a list of edges
edges = [
    go.Scatterpolar(
        r=[0, 1],
        theta=[0, 90],
        mode='lines',
        line=dict(width=2, color='black')
    ),
    go.Scatterpolar(
        r=[0, 1],
        theta=[0, 45],
        mode='lines',
        line=dict(width=2, color='black')
    ),
    # Add more edges as needed
]

# Create the layout configuration
layout = go.Layout(
    polar=dict(
        radialaxis=dict(visible=False),  # Hide radial axis labels and ticks
        angularaxis=dict(visible=False)  # Hide angular axis labels and ticks
    )
)

# Create the figure
fig = go.Figure(data=nodes + edges, layout=layout)

# Set the size of the figure
fig.update_layout(width=600, height=600)

# Display the figure
fig.show()
