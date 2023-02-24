import plotly.express as px

def scatter_tsne(dataframe, val_x, val_y, val_title):
    fig = px.scatter(dataframe, x=val_x, y=val_y,
                     title = val_title,
                     labels = {val_x: '', val_y: ''},
                    )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(showlegend=False)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return fig

def scatter_tsne_color(dataframe, val_x, val_y, val_color, val_title):
    fig = px.scatter(dataframe, x=val_x, y=val_y, color=val_color,
                     title = val_title,
                     labels = {val_x: '', val_y: '', val_color:''},
                    )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(showlegend=False)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return fig