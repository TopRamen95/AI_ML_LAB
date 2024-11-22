#2a
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

# Load the data
google = pd.read_csv('GOOGL_data.csv')
facebook = pd.read_csv('FB_data.csv')
apple = pd.read_csv('AAPL_data.csv')
amazon = pd.read_csv('AMZN_data.csv')
microsoft = pd.read_csv('MSFT_data.csv')

# Set the figure size and resolution
plt.figure(figsize=(16, 8), dpi=300)

# Plot the data
plt.plot(google['date'], google['close'], label='GOOGLE')
plt.plot(facebook['date'], facebook['close'], label='FACEBOOK')
plt.plot(apple['date'], apple['close'], label='APPLE')
plt.plot(amazon['date'], amazon['close'], label='AMAZON')
plt.plot(microsoft['date'], microsoft['close'], label='MICROSOFT')

# Set the x and y ticks
plt.xticks(np.arange(0, len(google['date']), 40), rotation=70)
plt.yticks(np.arange(0, 1450, 100))

# Add title and labels
plt.title('Stock Trend', fontsize=16)
plt.ylabel('Closing Price ($)', fontsize=14)

# Add grid and legend
plt.grid()
plt.legend()

# Show the plot
plt.show()


# In[24]:
#2b

movie_scores = pd.read_csv('D://datasets//exp2//movie_scores.csv')
plt.figure(figsize=(10, 5), dpi = 300)
pos = np.arange(len(movie_scores['MovieTitle']))
width = 0.3
plt.bar(pos-width/2, movie_scores['Tomatometer'], width, label = 'Tomatometer')
plt.bar(pos+width/2, movie_scores['AudienceScore'], width, label = 'Audience Score')
plt.xticks(pos, rotation = 10)
plt.yticks(np.arange(0, 101, 20))
ax = plt.gca()
ax.set_xticklabels(movie_scores['MovieTitle'])
ax.set_yticks(np.arange(0, 100, 5), minor = True)
ax.yaxis.grid(which = 'major')
ax.yaxis.grid(which = 'minor', linestyle = "--")
plt.title("Movie Comparision")
plt.legend()
plt.show()


# In[17]:

#2c
import pandas as sb
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

bills=sns.load_dataset('tips')
days=['Thur','Fir','Sat','Sun']
days_range=np.arange(len(days))
smoker=['Yes','No']
bills_by_days=[bills[bills['day']==day]for day in days]
bills_by_days_smoker=[[bills_by_days[day][bills_by_days[day]['smoker']==s]for s in smoker ]for day in days_range]
total_by_days_smoker=[[bills_by_days_smoker[day][s]['total_bill'].sum() for s in range(len(smoker))]for day in days_range]
totals=np.asarray(total_by_days_smoker)

plt.figure(figsize=(10,5),dpi=300)
plt.bar(days_range,totals[:,0],label='smoker')
plt.bar(days_range,totals[:,1],bottom=totals[:,0],label='Non-smoker')
plt.legend()
plt.xticks(days_range)
ax=plt.gca()
ax.set_xticklabels(days)
ax.yaxis.grid()
plt.ylabel('Daily total sales in $')
plt.title('Restaurant performance')
plt.show()


# In[19]:

#2d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Load the data
scales = pd.read_csv("smartphone_sales.csv")

# Set the figure size and resolution
plt.figure(figsize=(10, 6), dpi=300)

# Define the labels for the stack plot
labels = scales.columns[1:]

# Create the stack plot
plt.stackplot(scales['Quarter'], scales['Apple'], scales['Samsung'], scales['Huawei'], scales['Xiaomi'], scales['OPPO'], labels=labels[1:])

# Add legend, labels, and title
plt.legend()
plt.xlabel('Quarter')
plt.ylabel('Sales units in thousands')
plt.title('Smartphone Sales Units')

# Show the plot
plt.show()





