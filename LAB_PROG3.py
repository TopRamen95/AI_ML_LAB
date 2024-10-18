import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
iq_scores = [126,89,90,101,102,74,93,101,66,120,108,97,98,
             105,119,92,113,81,104,108,83,102,105,107,103,
             89,89,110,71,110,120,85,111,83,122,120,102,84,
             118,100,100,114,81,109,69,97,95,106,116,109,114,
             98,90,92,98,91,81,85,86,102,93,112,76,89,110,75,
             100,90,96,94,107,108,95,96,96,114,93,95,117,141,115,
             95,86,100,121,103,66,99,96,111,110,105,110,91,112,102,112,75]
plt.figure(figsize=(6,4),dpi=150)
plt.hist(iq_scores,bins=10)
plt.axvline(x=100,color='r')
plt.axvline(x=115,color='r',linestyle='--')
plt.axvline(x=85,color='r',linestyle='--')
plt.xlabel('IQ SCORE')
plt.ylabel('Frequency')
plt.title('IQ scores for a test group of hundred adults')
plt.show()
plt.figure(figsize=(6,4),dpi=150)
plt.boxplot(iq_scores)
ax=plt.gca()
ax.set_xticklabels(['Test Group'])
plt.y_label('IQ scores')
plt.title('Iq score sfor group of hundred')
plt.show()
group_a = [118,103,125,107,111,96,104,97,96,114,96,75,114,107,87,117,117,114,117,122,107,133,94,91,118,110,117,86,143,83,106,86,98,126,109,91,112,109,91,112,120,108,111,107,96,89,113,117,81,113,112,84,115,96,93,128,115,138,121,87,113,110,79,100,84,115,93,108,130,107,16,181,117,93,94,103,112,98,103,70,139,94,110,105,122,94,94,105,129,110,12,97,109,121,106,118,131,88,121,125,93,78]
plt.figure(figsize=(6,4),dpi=150)
plt.boxplot([group_a,group_b,group_c,group_d])
ax = plt.gca()
ax.set_xtickslabels(['Group A','Group B','Group C','Group D'])
plt.ylabel['IQ scores']
plt.title('IQ scores for different test groups')
plt.show()



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
data = pd.read_csv()
longevity = 'maximum longevity(yrs)'
mass = 'body mass(g)'
data = data[np.isfinite(data[longevity])&np.isfinite(data[mass])]
axes = data[data['class']=='Aves']
aves = aves[[mass]<2000]
fig = plt.figure(figsize = (8,8),dpi = 150,constrained_logout=True)
gs = fig.add_gridspec(4,4)
histx_ax=fig.add_subplot(gs[0,:-1])
histy_ax=fig.add_subplot(gs[1:,:-1])
scatter_ax=fig.add_subplot(gs[1:,:-1])
scatter_ax.scatter(aves[mass],aves[longetivity])
histx_ax.hist(aves[mass],bins=20,density=True)
histx=ax.set_xticks([])
histy_ax.hist(aves[longevity],bins = 20,density =True,orentiation = 'horizontal')
histy_ax.set_yticks([])
plt.xlabel('Bodymass in grams')
plt.ylabel('Maximum longrtivity in year')
fig.subtitle('Scatter plot with marginal histogram')
plt.show()
