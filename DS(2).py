#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[13]:


df=pd.read_excel('C://Users//Sahyadri//Downloads//Employee_Salary_Dataset.xlsx')
print("first few rows")
print(df.head())
print("Summarry stats")
print(df.describe())
filtered_data=df[df['Age']>30]
print("Filtered data (Age>30)")
print(filtered_data)
sorted_data=df.sort_values(by='Salary',ascending=False)
print("sorted data(by Salary)")
print(sorted_data)
df['Bonus']=df['Salary']*0.1
print("data with new coloumn(Bonus)")
print(df)
df.to_excel('Output.xlsx',index=False)
print("Data written to output.xlsx")


# In[ ]:





# In[ ]:





# In[ ]:




