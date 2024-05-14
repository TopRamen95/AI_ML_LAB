#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

data={
    'Name':['John','Emma','Sant','Lisa','Tome'],
    'Age' : [25,30,28,32,27],
    'Country' : ['USA', 'Canada', 'India', 'UK', 'Australia'],
    'Salary':[50000,60000,70000,80000,65000]
}

df = pd.DataFrame(data)

print("Original DataFrame")

print(df)

name_age=df[['Name','Age']]
print("Name and Age columns")
print(name_age)

filtered_df=df[df['Country']=='USA']
print("\n Filerered Dataframe( Country == USA)")
print(filtered_df)

sorted_df = df.sort_values("Salary",ascending=False)
print("\n Sorted DAtaFRame(By Salary in descending order)")
print(sorted_df)

average_salary = df['Salary'].mean()
print("\n Average Salary : ", average_salary)

df['Experience']=[3,6,4,8,5]
print("\n Data Frame with added experience")
print(df)

df.loc[df['Name']=='Emma','Salary']=65000
print("]nDataFrame with updating emma salary")
print(df)

df.drop('Experience',axis=1)
print("\nData frame after deleting Experience column")
print(df)


# In[ ]:




