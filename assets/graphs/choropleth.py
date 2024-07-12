import pandas as pd
import plotly.express as px

def func():
    df = pd.read_csv("countries.csv")
    fig = px.choropleth(df, locationmode="country names", 
        locations="location", color="visited",
    )
    
    fig.update_traces(hovertemplate="%{location}", 
        selector=dict(type='choropleth')
    )

    fig.update_layout(title=dict(
        text="Countries I've Visisted",
    ))

    fig.update_geos(projection_type="natural earth")

    print(fig)
    return fig

fig = func()
fig.write_html(file="world-travel.html",
    include_plotlyjs="cdn"
    )
# fig.show()
