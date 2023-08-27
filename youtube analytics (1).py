#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data=pd.read_csv(r"C:\Users\bhavy\Downloads\top-5000-youtube-channels.csv")


# In[4]:


#Display Top 5 Rows
data.head()


# In[5]:


#Displaying All Rows Except The Last 5 Rows
data.head(-5)


# In[6]:


#Displaying The Last 5 Rows
data.tail()


# In[7]:


#All The Rows Except The First 5 Rows 
data.tail(-5)


# In[8]:


#Number Of Rows And Columns Of The Dataset
data.shape


# In[9]:


print("Number Of Rows=",data.shape[0])
print("Number of Columns=",data.shape[1])


# In[10]:


#Total No. Of Rows,Columns,Datatypes Of Each Column And Memory Reqiurod
data.info()


# In[11]:


#Overall Statistics About Dataframe IN Integer Format
pd.options.display.float_format='{:.2f}'.format


# In[12]:


data.describe()


# In[13]:


import numpy as np


# In[14]:


#Data Cleaning To Replace'--' to NaN
data=data.replace('--',np.nan,regex=True)


# In[15]:


data.head(20)


# In[16]:


#Check Null Values
data.isnull().sum()


# In[17]:


per_missing = data.isnull().sum() * 100/len(data)


# In[18]:


per_missing


# In[19]:


#Missing Value Graph
sns.heatmap(data.isnull())


# In[20]:


#Dropping Missing Values
data.dropna(axis=0,inplace=True)


# In[21]:


sns.heatmap(data.isnull())


# In[22]:


data.head()


# In[23]:


data.tail()


# In[24]:


data.dtypes


# In[25]:


#Converting Datatype Of Rank Column To Integer
data['Rank']= data['Rank'].str[0:-2]


# In[26]:


data['Rank']= data['Rank'].str.replace(',','').astype('int')


# In[27]:


data.tail()


# In[28]:


data.dtypes


# In[29]:


#Data Cleaning For Video Uploads Adn Subscribers
data['Video Uploads']= data['Video Uploads'].astype('int')


# In[30]:


data['Subscribers']= data['Subscribers'].astype('int')


# In[31]:


data.dtypes


# In[32]:


#Data Cleaning Of Grade Column
data.head()


# In[33]:


data['Grade'].unique()


# In[34]:


#data['Grade'].astype(str).astype(int)


# In[35]:


data['Grade']=data['Grade'].map({'A++ ':5, 'A+ ':4, 'A ':3, 'A- ':2,'B+ ':1})


# In[ ]:





# In[36]:


#data['Grade'] = pd.to_numeric(data['Grade'], errors='coerce')


# In[37]:


data.dtypes


# In[38]:


#data['Grade']=data['Grade'].astype('int')


# In[39]:


data.columns


# In[40]:


#Find Average Views For Each Channel
data['Avg_views']=data['Video views']/data['Video Uploads']


# In[41]:


data.head()


# In[42]:


#Top 5 Channels With Maximum Number of Video Uploads
data.columns




# In[43]:


data.sort_values(by='Video Uploads',ascending=False).head()


# In[44]:


#Find Corelation matrix
data.corr()


# In[45]:


#Which Grade Has A Maximum Number Of Video Uploads
data.columns


# In[46]:


sns.barplot(x='Grade', y='Video Uploads',data=data)


# In[47]:


#Which Grade Has The Highest Average Views
data.columns


# In[48]:


sns.barplot(x='Grade', y='Avg_views',data=data)


# In[49]:


#Which Grade Has Thee Highest Number Of Subscribers
data.columns


# In[50]:


sns.barplot(x='Grade', y='Subscribers',data=data)


# In[51]:


#Which Grade Has The Highest Video Views
data.groupby('Grade').mean()


# In[55]:


# Load the dataset
data = pd.read_csv(r"C:\Users\bhavy\Downloads\top-5000-youtube-channels.csv")

# Create a scatter plot
plt.scatter(data['Subscribers'], data['Video views'])
plt.xlabel('Subscribers')
plt.ylabel('Video views')
plt.title('Subscribers vs. Video views')
plt.show()


# In[69]:


import matplotlib.pyplot as plt

# your code to create the plot
category_counts = data['Grade'].value_counts()
plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%', textprops={'fontsize': 5})
plt.title('Distribution of Video Uploads')

# set the figure size
fig = plt.gcf()
fig.set_size_inches(8, 8)  # set the width and height in inches
plt.legend(category_counts.index, loc="best")

plt.show()


# In[57]:





# In[71]:


x=np.random.randn(5000)

plt.title("Histogram")
plt.xlabel("Video views")
plt.ylabel("Frequency")
plt.hist(x,10)
plt.show()


# In[72]:


x=np.random.randn(5000)

plt.title("Histogram")
plt.xlabel("Subscribers")
plt.ylabel("Frequency")
plt.hist(x,10)
plt.show()


# In[ ]:


data = pd.read_csv(r"C:\Users\bhavy\Downloads\top-5000-youtube-channels.csv")
sns.pairplot(data, vars=["Subscribers", "Video views", 'Rank', 'Grade', 'Channel name', 'Video Uploads'])
sns.show()


# In[ ]:




