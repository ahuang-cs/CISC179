### Exercise 1
# Create a figure of size 15x8 with two subplots, top and bottom.
# Draw two lines in the top axes, one green and one orange.
# Add a legend for the top plot, *Green* and *Orange*. Put this legend in the top-middle of graph.
# **Extra Challenge**: In the bottom axes, create a graph of only the data points, marked by circles, but with no line connecting the points.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(data={'a':np.random.randint(0, 100, 30),
                        'b':np.random.randint(0, 100, 30),
                        'c':np.random.randint(0, 100, 30)})
df.head()

# TODO: Add your code here


# TODO: End your code here

### Sample Solution
# fig, ax = plt.subplots(2, 1, figsize=(15,8))
# ax[0].plot(df.index.values, df['a'], c='green')
# ax[0].plot(df.index.values, df['b'], c='orange')
# ax[0].legend(loc=9) # "9": upper center
# ax[1].plot(df.index.values, df['c'], marker='o', lw=0) # set line width = 0, means no visuable line

plt.show()