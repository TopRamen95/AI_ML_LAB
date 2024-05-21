#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


dataset = pd.read_csv('advertising.csv')
dataset.shape
dataset.isna().sum()
dataset.duplicated().any()
print(dataset)


# In[19]:


fig,axs = plt.subplots(3,figsize=(5,5))
plt1=sns.boxplot(dataset['TV'],ax = axs[0])
plt2=sns.boxplot(dataset['Newspaper'],ax = axs[1])
plt3=sns.boxplot(dataset['Radio'],ax = axs[2])
plt.tight_layout()
sns.distplot(dataset['Sales']);
sns.pairplot(dataset,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',height=4,aspect=1,kind='scatter')
plt.show()
sns.heatmap(dataset.corr(),annot=True)
plt.show()


# In[20]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Assuming you've already loaded your dataset into 'dataset'

x = dataset[['TV']]
y = dataset[['Sales']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

slr = LinearRegression()
slr.fit(x_train, y_train)

print('Intercept:', slr.intercept_)
print('Coefficient:', slr.coef_)
print('Regression Equation: Sales = {:.3f} + {:.3f} * TV'.format(slr.intercept_[0], slr.coef_[0][0]))

plt.scatter(x_train, y_train)
plt.plot(x_train, slr.predict(x_train), 'r')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.title('Linear Regression: TV vs. Sales')
plt.show()

y_pred_slr = slr.predict(x_test)
print("Predictions for the test set:", y_pred_slr)

slr_diff = pd.DataFrame({'Actual value': y_test['Sales'], 'Predicted value': y_pred_slr.flatten()})
print(slr_diff)

r2_value = r2_score(y, slr.predict(x))
print('R-squared value of this model: {:.2f}'.format(r2_value * 100))


# In[ ]:




