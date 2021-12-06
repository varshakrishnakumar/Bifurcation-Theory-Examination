import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.figure_factory as ff

x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(x, y)
r = np.arange(-2, 2, 0.1)

# when r = -1
dy = 1 + Y**2
dx = np.ones(dy.shape)

dyu = dy / np.sqrt(dy**2 + dx**2)
dxu = dx / np.sqrt(dy**2 + dx**2)

fig = ff.create_quiver(X, Y, dxu, dyu, arrow_scale = 0.05)
fig.update_layout(title = "Saddle-Node Bifurcation Diagram when r = 1")
fig.show()
fig.write_image("plot-snapshots\saddplenodept3.png")



