import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("./benefits.csv")

labels = list(set(df['source'].to_list() + df['dest'].to_list()))
indices = {}
for i,x in enumerate(labels):
    indices[x] = i

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = list(indices.keys()),
      color = "blue"
    ),
    link = dict(
      source = [indices[i] for i in df['source'].to_list()], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [indices[i] for i in df['dest'].to_list()],
      value = [df['amount'].to_list()]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
print(fig)
fig.show()