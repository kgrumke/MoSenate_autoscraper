#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# # Building a scraper for bills filed in Missouri's Senate in the first extraordinary session
# Link: https://www.senate.mo.gov/21info/BTS_Web/BillList.aspx?SessionType=E1

# In[2]:


response = requests.get("https://www.senate.mo.gov/21info/BTS_Web/BillList.aspx?SessionType=E1")
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


print(doc)


# In[4]:


doc.select('.site-content')


# In[5]:


content = doc.select('.site-content')[0]
container = content.select('.tg-container')[0]


# In[14]:


type(container)


# In[12]:


container.select('.tbody')


# In[28]:


table = container.find('table')
bills = table.findAll('tr')[2]


# In[40]:


trs = bills.select('tr')


# In[48]:


len(trs)


# In[141]:


trs[0]


# In[242]:


rows = []

for bill in trs:
    a = bill.findAll('a')
    billname = a[0]
    senator = a[1]
    billname = billname.text
    senator = senator.text
    url = a[0]['href']
    link = f'https://www.senate.mo.gov/21info/BTS_Web/{url}'
    
    row = {}
    print(billname)
    row['Bill'] = billname
    print(senator)
    row['Senator'] = senator
    
    summary = bill.findAll('span')
    summary = summary[0].text
    print(summary)
    row['Summary'] = summary
    print(link)
    row['Bill_Link'] = link
    print("---")  
    
    rows.append(row)


# In[243]:


df = pd.DataFrame(rows)
df


# In[244]:


df = df.drop_duplicates()


# In[245]:


df


# In[246]:


df.to_csv('MOSenate_BillsFiled.csv')



# In[241]:


#calling the bill URL to add to the DF

#for bill in trs:
    #a = bill.findAll('a')
    #url = a[0]['href']
    #print(f'https://www.senate.mo.gov/21info/BTS_Web/{url}')


# # an easier way:

# In[217]:


#url = 'https://www.senate.mo.gov/21info/BTS_Web/BillList.aspx?SessionType=E1'
#df = pd.read_html(url)


# In[218]:


#df = df[1]


# In[195]:


#df['Bills'] = df


# In[219]:


#len(df)


# In[220]:


#df


# In[209]:


#df = df['Bills'].str.split("-", n = 2, expand = True)


# In[215]:


#df = df.rename(columns = {0 : 'Bill', 1 : 'Senator', 2 : 'Description'})


# In[221]:


#df


# In[ ]:




