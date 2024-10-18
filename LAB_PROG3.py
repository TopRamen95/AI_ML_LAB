#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plt

# Sample IQ scores
iq_scores = [126, 89, 90, 101, 102, 74, 93, 101, 66, 120, 108, 97, 98,
             105, 119, 92, 113, 81, 104, 108, 83, 102, 105, 107, 103,
             89, 89, 110, 71, 110, 120, 85, 111, 83, 122, 120, 102, 84,
             118, 100, 100, 114, 81, 109, 69, 97, 95, 106, 116, 109, 114,
             98, 90, 92, 98, 91, 81, 85, 86, 102, 93, 112, 76, 89, 110, 75,
             100, 90, 96, 94, 107, 108, 95, 96, 96, 114, 93, 95, 117, 141, 115,
             95, 86, 100, 121, 103, 66, 99, 96, 111, 110, 105, 110, 91, 112, 102, 112, 75]

# Histogram
plt.figure(figsize=(6, 4), dpi=150)
plt.hist(iq_scores, bins=10)
plt.axvline(x=100, color='r')
plt.axvline(x=115, color='r', linestyle='--')
plt.axvline(x=85, color='r', linestyle='--')
plt.xlabel('IQ SCORE')
plt.ylabel('Frequency')
plt.title('IQ scores for a test group of hundred adults')
plt.show()

# Boxplot for IQ scores
plt.figure(figsize=(6, 4), dpi=150)
plt.boxplot(iq_scores)
ax = plt.gca()
ax.set_xticklabels(['Test Group'])
plt.ylabel('IQ scores')  # Corrected line
plt.title('IQ scores for group of hundred')
plt.show()

# Groups A, B, C, D
group_a = [118, 103, 125, 107, 111, 96, 104, 97, 96, 114, 96, 75, 114, 107, 87, 117, 117, 114, 117, 122, 107, 133, 94, 91, 118, 110, 117, 86, 143, 83, 106, 86, 98, 126, 109, 91, 112, 109, 91, 112, 120, 108, 111, 107, 96, 89, 113, 117, 81, 113, 112, 84, 115, 96, 93, 128, 115, 138, 121, 87, 113, 110, 79, 100, 84, 115, 93, 108, 130, 107, 16, 181, 117, 93, 94, 103, 112, 98, 103, 70, 139, 94, 110, 105, 122, 94, 94, 105, 129, 110, 12, 97, 109, 121, 106, 118, 131, 88, 121, 125, 93, 78]
group_b = [120, 105, 127, 109, 113, 98, 106, 99, 98, 116, 98, 77, 116, 109, 89, 119, 119, 116, 119, 124, 109, 135, 96, 93, 120, 112, 119, 88, 145, 85, 108, 88, 100, 128, 111, 93, 114, 111, 93, 114, 122, 110, 113, 109, 98, 91, 115, 119, 83, 115, 114, 86, 117, 98, 95, 130, 117, 140, 123, 89, 115, 112, 81, 102, 86, 117, 95, 110, 132, 109, 18, 183, 119, 95, 96, 105, 114, 100, 105, 72, 141, 96, 112, 107, 124, 96, 96, 107, 131, 112, 14, 99, 111, 123, 108, 120, 133, 90, 123, 127, 95, 80]
group_c = [122, 107, 129, 111, 115, 100, 108, 101, 100, 118, 100, 79, 118, 111, 91, 121, 121, 118, 121, 126, 111, 137, 98, 95, 122, 114, 121, 90, 147, 87, 110, 90, 102, 130, 113, 95, 116, 113, 95, 116, 124, 112, 115, 111, 100, 93, 117, 121, 85, 117, 116, 88, 119, 100, 97, 132, 119, 142, 125, 91, 117, 114, 83, 104, 88, 119, 97, 112, 134, 111, 20, 185, 121, 97, 98, 107, 116, 102, 107, 74, 143, 98, 114, 109, 126, 98, 98, 109, 133, 114, 16, 101, 113, 125, 110, 122, 135, 92, 125, 129, 97, 82]
group_d = [124, 109, 131, 113, 117, 102, 110, 103, 102, 120, 102, 81, 120, 113, 93, 123, 123, 120, 123, 128, 113, 139, 100, 97, 124, 116, 123, 92, 149, 89, 112, 92, 104, 132, 115, 97, 118, 115, 97, 118, 126, 114, 117, 113, 102, 95, 119, 123, 87, 119, 118, 90, 121, 102, 99, 134, 121, 144, 127, 93, 119, 116, 85, 106, 90, 121, 99, 114, 136, 113, 22, 187, 123, 99, 100, 109, 118, 104, 109, 76, 145, 100, 116, 111, 128, 100, 100, 111, 135, 116, 18, 103, 115, 127, 112, 124, 137, 94, 127, 131, 99, 84]

# Boxplot for different groups
plt.figure(figsize=(6, 4), dpi=150)
plt.boxplot([group_a, group_b, group_c, group_d])
ax = plt.gca()
ax.set_xticklabels(['Group A', 'Group B', 'Group C', 'Group D'])  # Corrected line
plt.ylabel('IQ scores')  # Corrected line
plt.title('IQ scores for different test groups')
plt.show()


# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ensure inline plotting in Jupyter notebooks
get_ipython().run_line_magic('matplotlib', 'inline')

# Load the data
data = pd.read_csv('anage_data.csv')

# Define the columns for longevity and mass
longevity = 'Maximum longevity (yrs)'  # Check the exact column name in your CSV
mass = 'Body mass (g)'  # Check the exact column name in your CSV

# Filter out rows with non-finite values in the specified columns
data = data[np.isfinite(data[longevity]) & np.isfinite(data[mass])]

# Filter the data for class 'Aves'
aves = data[data['Class'] == 'Aves']

# Further filter for body mass less than 2000 grams
aves = aves[aves[mass] < 2000]

# Create the figure and gridspec layout
fig = plt.figure(figsize=(8, 8), dpi=150, constrained_layout=True)
gs = fig.add_gridspec(4, 4)

# Create the subplots
histx_ax = fig.add_subplot(gs[0, :-1])
histy_ax = fig.add_subplot(gs[1:, -1])
scatter_ax = fig.add_subplot(gs[1:, :-1])

# Scatter plot
scatter_ax.scatter(aves[mass], aves[longevity])

# Histograms
histx_ax.hist(aves[mass], bins=20, density=True)
histx_ax.set_xticks([])

histy_ax.hist(aves[longevity], bins=20, density=True, orientation='horizontal')
histy_ax.set_yticks([])

# Set labels
scatter_ax.set_xlabel('Body mass (g)')
scatter_ax.set_ylabel('Maximum longevity (yrs)')

# Set the title
fig.suptitle('Scatter plot with marginal histograms')

# Show the plot
plt.show()


# In[25]:


import numpy as np
import matplotlib.pyplot as plt

group_a = [118,103,125,107,111,96,104,97,96,114,96,75,114,107,87,117,117,114,117,122,107,133,94,91,118,110,117,86,143,83,106,86,98,126,109,91,112,109,91,112,120,108,111,107,96,89,113,117,81,113,112,84,115,96,93,128,115,138,121,87,113,110,79,100,84,115,93,108,130,107,16,181,117,93,94,103,112,98,103,70,139,94,110,105,122,94,94,105,129,110,12,97,109,121,106,118,131,88,121,125,93,78]
group_b = [120, 105, 127, 109, 113, 98, 106, 99, 98, 116, 98, 77, 116, 109, 89, 119, 119, 116, 119, 124, 109, 135, 96, 93, 120, 112, 119, 88, 145, 85, 108, 88, 100, 128, 111, 93, 114, 111, 93, 114, 122, 110, 113, 109, 98, 91, 115, 119, 83, 115, 114, 86, 117, 98, 95, 130, 117, 140, 123, 89, 115, 112, 81, 102, 86, 117, 95, 110, 132, 109, 18, 183, 119, 95, 96, 105, 114, 100, 105, 72, 141, 96, 112, 107, 124, 96, 96, 107, 131, 112, 14, 99, 111, 123, 108, 120, 133, 90, 123, 127, 95, 80]
group_c = [122, 107, 129, 111, 115, 100, 108, 101, 100, 118, 100, 79, 118, 111, 91, 121, 121, 118, 121, 126, 111, 137, 98, 95, 122, 114, 121, 90, 147, 87, 110, 90, 102, 130, 113, 95, 116, 113, 95, 116, 124, 112, 115, 111, 100, 93, 117, 121, 85, 117, 116, 88, 119, 100, 97, 132, 119, 142, 125, 91, 117, 114, 83, 104, 88, 119, 97, 112, 134, 111, 20, 185, 121, 97, 98, 107, 116, 102, 107, 74, 143, 98, 114, 109, 126, 98, 98, 109, 133, 114, 16, 101, 113, 125, 110, 122, 135, 92, 125, 129, 97, 82]
group_d = [124, 109, 131, 113, 117, 102, 110, 103, 102, 120, 102, 81, 120, 113, 93, 123, 123, 120, 123, 128, 113, 139, 100, 97, 124, 116, 123, 92, 149, 89, 112, 92, 104, 132, 115, 97, 118, 115, 97, 118, 126, 114, 117, 113, 102, 95, 119, 123, 87, 119, 118, 90, 121, 102, 99, 134, 121, 144, 127, 93, 119, 116, 85, 106, 90, 121, 99, 114, 136, 113, 22, 187, 123, 99, 100, 109, 118, 104, 109, 76, 145, 100, 116, 111, 128, 100, 100, 111, 135, 116, 18, 103, 115, 127, 112, 124, 137, 94, 127, 131, 99, 84]

plt.figure(figsize=(12,8),dpi=150)
plt.subplot(2,2,1)
plt.scatter(group_a,group_b,color="blue")
plt.xlabel('Group A')
plt.ylabel('Group B')
plt.title('Group A vs Group B')
plt.subplot(2,2,2)
plt.scatter(group_a,group_c,color="green")
plt.xlabel('Group A')
plt.ylabel('Group C')
plt.title('Group A vs Group C')
plt.subplot(2,2,3)
plt.scatter(group_a,group_d,color="red")
plt.xlabel('Group A')
plt.ylabel('Group D')
plt.title('Group A vs Group D')
plt.subplot(2,2,4)
plt.scatter(group_b,group_c,color="purple")
plt.xlabel('Group b')
plt.ylabel('Group c')
plt.title('Group B vs Group C')
plt.tight_layout()
plt.show()


# In[ ]:




