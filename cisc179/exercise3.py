### Exercise 3
# Visualize the mock data given below.<br>
# Create bars to represent the turnover for each market.<br>
# Keep in mind that showing too much information on a graph can be overwhelming, so do it with discretion !<br>
# Use labels to make sure your audience understands the graph.<br>
# **Extra Challenge**:  On the opposite axis, draw a line to show each market share. (Hint: use `ax.twinx()`)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

turnover_data = pd.DataFrame({'boardid' : ['DAY', 'DAY_X', 'DAY_U', 'TSE'],
                              'turnover' : np.random.randint(1e6, 1e9, 4)})

# sort by turnover value
turnover_data = turnover_data.sort_values(by='turnover').reset_index().drop('index', axis=1)

# convert value to Million unit for easy-reading
turnover_data['turnover_simplified'] = turnover_data['turnover'] // 1000000

# market share
turnover_data['market_share'] = round((turnover_data['turnover'] / sum(turnover_data['turnover'])*100), 1)

turnover_data

# TODO: Add your code here


# TODO: End your code here

### Sample Solution
# fig, ax1 = plt.subplots(figsize=(15,10))
#
# ax1.bar(turnover_data['boardid'], turnover_data['turnover'], width=0.5, color='lightgreen')
# for i in range(turnover_data.shape[0]):
#     ax1.text(turnover_data['boardid'][i], turnover_data['turnover'][i]+1e7, str(turnover_data['turnover_simplified'][i])+'M', fontsize=15, horizontalalignment='center')
#
# ax1.set_title('Turnover Data', fontsize=20)
# ax1.set_xticklabels(turnover_data['boardid'], fontsize=15);
#
# ax1.tick_params(labelsize=15, axis='y')
#
# ax1.set_ylabel('Turnover Values(Million)', fontsize=20)
# ax1.set_ylim(0, max(turnover_data['turnover']+1e8))
#
# # Format ax1 y axis - method 1
# vals = ax1.get_yticks()
# ax1.set_yticklabels([str(x/1000000)+'M' for x in vals])
#
#
# ax2 = ax1.twinx()
# ax2.plot(turnover_data['boardid'], turnover_data['market_share'], c='red', lw=4, marker='o')
# for i in range(turnover_data.shape[0]):
#     ax2.text(turnover_data['boardid'][i], turnover_data['market_share'][i]+1, str(turnover_data['market_share'][i])+'%', fontsize=15, horizontalalignment='center', color='black')
#
# ax2.set_ylabel('Market Shares(%)', fontsize=20)
# ax2.tick_params(labelsize=15, axis='y', rotation=30)
#
# # Format ax2 y asix - method 1
# # ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y/100)))
#
# # Format ax2 y asix - method 2
# vals = ax2.get_yticks()
# ax2.set_yticklabels([str(x)+'%' for x in vals]);

plt.show()