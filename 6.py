Simple Line Plots
In [1]:

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


In [2]:

fig = plt.figure()
ax = plt.axes()


# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np
# define data values

x = np.array([1, 2, 3, 4]) # X-axis points
y = x*2 # Y-axis points
plt.plot(x, y) # Plot the chart
plt.show() # display

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
# Creating vectors X and Y
x = np.linspace(-2, 2, 100)
y = x ** 2
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)
# Show the plot
plt.show()

Customization of plots


Function Description
plt.xlim() sets the limits for X-axis
plt.ylim() sets the limits for Y-axis

plt.grid() adds grid lines in the plot

plt.title() adds a title

plt.xlabel() adds label to the horizontal axis

plt.ylabel() adds label to the vertical axis

plt.axis() sets axis properties (equal, off, scaled, etc.)

plt.xticks() sets tick locations on the horizontal axis

plt.yticks() sets tick locations on the vertical axis

plt.legend() used to display legends for several lines in the same figure

plt.savefig() saves figure (as .png, .pdf, etc.) to working directory

plt.figure() used to set new figure properties

Once we have created an axes, we can use the ax.plot function to plot some
data. Let's start with a simple sinusoid:

In [3]:

fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)

ax.plot(x, np.sin(x));

Adjusting the Plot: 

In [6]:

plt.plot(x, np.sin(x - 0), color='blue') # specify color by name
plt.plot(x, np.sin(x - 1), color='g') # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75') # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44') # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported


In [7]:

plt.plot(x, x + 0, linestyle='solid')

plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');
# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-') # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':'); # dotted