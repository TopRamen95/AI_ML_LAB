import pandas as sb
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

%matplotlib inline 

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


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
scales=pd.read_csv("")
plt.figure(figsize=(10,6),dpi=300)
labels=scales.columns[2:]
plt.stackplot('Quarter','Apple','Samsung','Huaweu','Xiaomi','OPPO',data=scales,labels=labels)
plt.legends()
plt.xlabels('Quarter')
plt.ylabel('scales unit in thousands')
plt.title('Smart phones scales unit')
plt.show()
