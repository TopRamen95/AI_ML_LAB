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
