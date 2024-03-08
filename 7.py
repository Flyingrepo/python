
HistPlot:

import numpy as np
import seaborn as sns
sns.set(style="dark") # white,
dark, ticks
# Generate a random univariate
dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)
# Plot a simple histogram and
kde
sns.histplot(d, kde=True,
color="m")

linePlot:
    
    a=pd.DataFrame({'Day':[1,2,3,4,5
,6,7],

'Grocery':[30,80

,45,23,51,46,76],

'Clothes':[13,40

,34,23,54,67,98],

'Utensils':[12,3

2,27,56,87,54,34]}

,index=[1,2,3,4,5

,6,7])
g = sns.relplot(x="Day",
y="Utensils", kind="line",
data=a)

Using both Matplotlib and sea born

# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
# draw lineplot
sns.lineplot(x="sepal_length",
y="sepal_width", data=data)
# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')
plt.show()


colour Plot 

import seaborn as sns
import matplotlib.pyplot as plt
palette = sns.color_palette()
sns.palplot(palette)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
palette =
sns.light_palette("Blue",10)
sns.palplot(palette)
plt.show()