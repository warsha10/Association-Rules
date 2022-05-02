#!/usr/bin/env python
# coding: utf-8

# ### 1. Import Necessasy libraries

# In[2]:


import pandas as pd


# ### 2. Import Data

# In[4]:


retail_data = pd.read_excel('Online Retail.xlsx')
retail_data


# In[5]:


retail_data.head(20)


# ### 3. Data Understanding

# In[6]:


retail_data.shape


# In[7]:


retail_data.describe(include= 'all')


# In[9]:


print(retail_data['Country'].unique())


# In[10]:


retail_data['InvoiceNo'].nuniquenique()


# In[11]:


retail_data.isna().sum()


# In[12]:


del retail_data['CustomerID']


# In[13]:


retail_data.dropna(axis = 0, inplace=True)


# In[14]:


retail_data.isna().sum()


# ### Pick Up United Kingdom and get the Best Associates

# In[17]:


uk_data = retail_data[retail_data['Country'] == 'United Kingdom']
uk_data


# In[18]:


uk_data['InvoiceNo'].nunique()


# In[19]:


uk_data['Description'].nunique()


# ### Pick up France and get the Best Associates

# In[22]:


france_data = retail_data[retail_data['Country'] == 'France']
france_data


# In[26]:


france_pivot_data = pd.pivot_table(data = france_data,values='Quantity',index='InvoiceNo',columns='Description').fillna(0)
france_pivot_data


# In[31]:


france_pivot_data = france_pivot_data.applymap(lambda x:1 if x>0 else 0)
france_pivot_data
#Apply - we have to pik up the column
#AAplymap - we dont need to pass the column name


# ### Prepare the data according to the Apriori Algorithm Expectation

# In[24]:


uk_pivot_data = pd.pivot_table(data = uk_data,values='Quantity',index='InvoiceNo',columns='Description').fillna(0)
uk_pivot_data


# In[33]:


uk_pivot_data = uk_pivot_data.applymap(lambda x:1 if x>0 else 0)
uk_pivot_data


# In[ ]:





# ### Model Building

# In[20]:


from mlxtend.frequent_patterns import apriori,association_rules


# In[37]:


frequent_item_sets = apriori(df =uk_pivot_data ,min_support=0.03, use_colnames=True) #Frequent itemsets
frequent_item_sets


# In[39]:


association_rules(df = frequent_item_sets ,metric='confidence',min_threshold=0.05,)


# In[ ]:




