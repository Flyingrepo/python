Basic legends
The legend_label parameter is used to add a basic

label to any one of the glyph.

from bokeh.plotting import figure, output_file,
show
x = [val for val in range(10)]
y = [val for val in range(0, 20, 2)]
output_file("basiclegend.html")
p = figure()
p.line(x, y, legend_label="My Red Line",
line_color="red")
p.line(y, x, legend_label="My Orange Line",
line_color="orange")
p.line(y[::-1], x, legend_label="My Green Line",
line_color="green")
show(p)

Automatic Grouping can be used when we want to group multiple legend items to
be grouped into one.
from bokeh.plotting import figure, output_file,
show
from bokeh.models import ColumnDataSource
p = figure(x_range=(0.5, 2.5), y_range=(0.5, 2.5))
source = ColumnDataSource(dict(
x=[1, 1, 2, 2, 1.5],
y=[1, 2, 1, 2, 1.5],
color=['red', 'red', 'red', 'red', 'blue'],
label=['corner', 'corner', 'corner', 'corner',
'center']
))
p.circle(x='x', y='y', radius=0.05, color='color',
legend_group='label',

source=source)
output_file("AutomaticGrouping.html")
show(p)