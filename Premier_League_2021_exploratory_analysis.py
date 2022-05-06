#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib


# In[4]:


epl = pd.read_csv(r"C:\Users\mehar\OneDrive\Documents\EPL_20_21.csv")


# In[5]:


#Seeing what the data set looks like
print(epl.head())


# In[11]:


epl.shape


# In[12]:


#checking for null values
epl.isnull().sum()


# In[16]:


#Willy Caballero was the oldest player in the premier league last season
epl[epl['Age']==epl['Age'].max()]


# In[17]:


#Shoretire, Scarlett, Chukwuemeka and Hackford were the youngest players in the premier league last year
epl[epl['Age']==epl['Age'].min()]


# In[20]:


#How was age distributed amongst teams?
sns.boxplot(x='Club', y='Age', data=epl)
plt.xticks(rotation=90)


# In[22]:


#How was age distributed amongst the league
sns.displot(epl['Age'])


# In[24]:


pip install squarify


# In[25]:


import squarify


# In[55]:


fig = plt.figure(figsize=(18,20))
sizes=epl.groupby('Nationality',)['Name'].count().sort_values(ascending= False).tolist() 
label=epl.groupby('Nationality',)['Name'].count().sort_values(ascending= False).index.values.tolist()


# In[52]:


#how players are distributed by nationality
squarify.plot(sizes=sizes, label=label, alpha=0.6 )


# In[60]:


#Which teams scored the most goals?
goals_per_team = pd.DataFrame(epl.groupby('Club', as_index=False)['Goals'].sum())


# In[58]:


print(goals_per_team)


# In[62]:


sns.barplot(x='Club', y='Goals', data=goals_per_team)
plt.xticks(rotation=90)


# In[64]:


#Who were the top marksmen in the premier league?
top_marksmen = epl.sort_values(by='Goals', ascending=False)[:10]


# In[65]:


print(top_marksmen)


# In[66]:


sns.barplot(x='Name', y='Goals', data=top_marksmen)
plt.xticks(rotation=90)


# In[7]:


#Who are the top assisters?
top_assisters = epl.sort_values(by='Assists', ascending=False)[:10]


# In[8]:


sns.barplot(x='Name', y='Assists', data=top_assisters)
plt.xticks(rotation=90)


# In[12]:


#Who Were the least efficient goal scorers? (Biggest overperformance of xG)
attacking_stats_df = epl[['Name', 'Club', 'Mins', 'Goals', 'Assists', 'Penalty_Goals', 'Penalty_Attempted', 'xG', 'xA']]


# In[13]:


attacking_stats_df['expected_goals'] = attacking_stats_df['xG']*(attacking_stats_df['Mins']/90)
attacking_stats_df['Goal_involvement'] = attacking_stats_df['Goals']+attacking_stats_df['Assists']
attacking_stats_df['min_per_goal_inv'] = attacking_stats_df['Mins']/attacking_stats_df['Goal_involvement']


# In[33]:


attacking_stats_df['Over or Under performance of xG'] = attacking_stats_df['Goals']-attacking_stats_df['expected_goals']


# In[37]:


overperformers_df = attacking_stats_df[['Name', 'Over or Under performance of xG']].sort_values(by='Over or Under performance of xG', ascending= False)[:10]


# In[38]:


print(overperformers_df)


# In[43]:


p = sns.barplot(x='Name', y='Over or Under performance of xG', data=underperformers_df)
plt.xticks(rotation=90)
p.set(xlabel='Name', ylabel='Over performance of xG')


# In[44]:


#Who were the most efficient scorers (biggest xG over achievers)
underperformers_df = attacking_stats_df[['Name', 'Over or Under performance of xG']].sort_values(by='Over or Under performance of xG', ascending= False)[-10:]


# In[45]:


print(underperformers_df)


# In[48]:


m = sns.barplot(x='Name', y='Over or Under performance of xG', data=underperformers_df)
plt.xticks(rotation=90)
m.set(xlabel='Name', ylabel='under performers of xG')


# In[50]:


#Who had the best minutes per goal involvment efficiency?


# In[51]:


#Who had the highest minutes per goal efficiency (minimum of 1000 minutes)?
attacking_stats_df['expected_goal_inv'] = (attacking_stats_df['xG']+attacking_stats_df['xA'])*(attacking_stats_df['Mins']/90)
attacking_stats_df['min_per_exp_goal_inv']= attacking_stats_df['Mins']/attacking_stats_df['expected_goal_inv']


# In[55]:


efficiency = attacking_stats_df[['Name', 'Club', 'Mins', 'min_per_goal_inv', 'min_per_exp_goal_inv']][attacking_stats_df['Mins']>1000].sort_values(by="min_per_goal_inv")[:10]
efficiency


# In[54]:


attacking_stats_df[['Name', 'Club', 'Mins', 'min_per_goal_inv', 'min_per_exp_goal_inv']][attacking_stats_df['Mins']>1000].sort_values(by="min_per_exp_goal_inv")[:10]


# In[58]:


plt.figure(figsize=(15, 10))
ax = sns.barplot(x='Name', y='min_per_goal_inv', data=efficiency)
width_scale = 0.45
plt.xticks(rotation=90)
for bar in ax.containers[0]:
    bar.set_width(bar.get_width() * width_scale)
ax.set_ylim(0, 250)

ax2 = ax.twinx()
sns.barplot(x='Name', y='min_per_exp_goal_inv', data=name, alpha=0.7, hatch='xx', ax=ax2)

for bar in ax2.containers[0]:
    x = bar.get_x()
    w = bar.get_width()
    bar.set_x(x + w * (1- width_scale))
    bar.set_width(w * width_scale)
ax2.set_ylim(0, 250)

#Suggests Jesse Lingard is the most efficent PL player when taking into account minutes 


# In[ ]:




