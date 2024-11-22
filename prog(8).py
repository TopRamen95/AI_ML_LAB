#Write a python program to explain working with bokeh line graph using annotations and legends and plotting a different types of plot using bokeh
from bokeh.plotting import figure, show
from bokeh.models import Legend, LegendItem
import numpy as np


# Display plots inline in a Jupyter Notebook
output_notebook()

#Smple_data
# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a new plot
p1 = figure(title="Line Plot with Annotations and Legend", x_axis_label='X-Axis', y_axis_label='Y-Axis')

#Lineplot with annotations and legends
def line_plot_with_annotations():
    p=figure(title="Line Plot with Annotations and Legends",x_axis_label='X',y_axis_label='Y',width=800,height=400)

#Plot thr sine and cosine lines without legend labels
line1 = p.line(x,y,width=2,color="blue")
line1 = p.line(x,y2,width=2,color="green")

#Create a legend manually using legenditem
legend = Legend(items=[LegendItem(label="sin(x),renderers=[line1]"),LegendItem(label="cos(x),renderers=[line2]")])
p.add_layout(legend,'right')
show(p)
scatter_plot(p)
