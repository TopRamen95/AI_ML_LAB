import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set()
data = pd.read_csv('northern_surface_temperature.csv',index_col = ['Year'])
data = data.transpose()
heat_colormap = sns.diverging_palette(240,15,s=99,as_cmap=True)
plt.figure(dpi=200)
sns.heatmap(data.iloc[:,::5],cmap=heat_colormap,center=0)
plt.title("Temperature Changes from 1880 to 2015(base perioud 1951-1980)")
plt.show()
