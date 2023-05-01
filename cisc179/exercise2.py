### Exercise 2
# Create a figure with three subplots, aligned vertically.
# Create a bar graph for a and b on the first two, but at the last one draw both a and b, but put b on top of a! (Hint: use the bottom argument in the bar function)
# Make sure the color for a and b are consistent in all the subplots!
# **Extra Challenge**: Write the magnitude of each bar on top of it

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
# fig, ax = plt.subplots(3, 1, figsize=(15, 18))
#
# ax[0].bar(df.index.values, df['a'])
# for i in range(df.shape[0]):
#     ax[0].text(i, df['a'][i] + 1, df['a'][i], horizontalalignment='center')
# ax[0].legend('a')
#
# ax[1].bar(df.index.values, df['b'])
# for i in range(df.shape[0]):
#     ax[1].text(i, df['b'][i] + 1, df['b'][i], horizontalalignment='center')
# ax[1].legend('b')
#
# ax[2].bar(df.index.values, df['a'])
# ax[2].bar(df.index.values, df['b'], bottom=df['a'])
# for i in range(df.shape[0]):
#     ax[2].text(i, df['a'][i] + df['b'][i] + 1, df['a'][i] + df['b'][i], horizontalalignment='center')
# ax[2].legend(['a', 'b'])

plt.show()
