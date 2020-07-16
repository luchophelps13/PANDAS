#!/usr/bin/env python
# coding: utf-8

# # Pandas Intro/Explanation

# ## What is Pandas used for?

# In[37]:


print('In short, "[...] pandas is a software library written for the Python programming language for data manipulation and analysis." src = https://en.wikipedia.org/wiki/Pandas_(software)')


# ## How to Install Pandas

# In[28]:


print('In your Anaconda/Miniconda Prompt, type and run "pip install pandas".')


# ## Importing Pandas

# In[2]:


import pandas as pd


# # Loading Data

# ## Loading .csv files

# In[3]:


df = pd.read_csv(r'C:\Users\luchc\Downloads\pokemon_data.csv.txt')


# In[24]:


print('First 5:\n\n', df.head(), '\n\n', 'Last 5:\n\n', df.tail())


# ## Loading Excel Files

# In[18]:


df_xlsx = pd.read_excel(r'C:\Users\luchc\Downloads\pandas-master\pokemon_data.xlsx')


# In[25]:


print('First 5:\n\n', df_xlsx.head(), '\n\n', 'Last 5:\n', df_xlsx.tail())


# ## Loading ".txt" files as "csv"s

# In[26]:


df_txt = pd.read_csv(r'C:\Users\luchc\Downloads\pandas-master\pokemon_data.txt', delimiter='\t')


# In[28]:


print('First 5:\n\n', df_txt.head(), '\n\n', 'Last 5:\n', df_txt.tail())


# # Reading Data into Pandas

# ## Headers

# In[22]:


# Headers
print(df.columns)


# ## Reading Specific Columns

# In[23]:


#df['insert column name'][index] (index is exclusive)
print(df['Name'][4:16])
#only shows 4-15, meaning it goes from 4 UP TO 16, not including 16

#Multiple
print(df[['Name', 'Type 1', 'Type 2']])


# ## Rows

# In[24]:


df.iloc[1]


# ## Multiple Rows

# In[48]:


df.iloc[7:9]


# ## Accessing Specific Value using (R,C)

# In[47]:


#Location (R,C)
#Rows go down, columns go across
#Lets say we want to access & print the value in the 2nd row and 1st column
df.iloc[2,1]


# # Iterate Through Rows & Columns

# ## Printing All Values in 1 Row

# In[57]:


for index, row in df.iterrows():
    print(index, row['Name'])


# # Getting Rows Based On Specific Condition(s)

# ## Printing All Values with a Certain Col. Name

# In[58]:


df.loc[df['Type 1'] == 'Fire']


#  # Sorting and Describing Data

# ## Using the "describe" function

# In[5]:


df.describe()


# ## Sorting Values

# ### Sorting Single Rows

# In[8]:


df.sort_values('Name') #In alphabetical order


# In[10]:


df.sort_values('Type 1') #Alphabetical Order


# In[11]:


df.sort_values('Generation') #Numerical Order


# ### Using Index to Attain Specific Values

# In[13]:


#Using index
df.sort_values('Name')[5:12]


# ### Ascending = True/False

# In[14]:


df.sort_values('Name', ascending=False)


# ### Sorting Multiple rows

# In[16]:


df.sort_values(['Type 1', 'HP'])
#Sorts all of the Type 1 pokemon in alphabetical order by type and ascending order based on HP


# ### Multiple Rows w/ 1 Ascending and the other Descending

# In[21]:


df.sort_values(['Type 1', 'HP'], ascending = [1,0])
# 1 means ascending, 0 means descending


# # Making Changes to Data

# ## Creating New Columns

# In[68]:


#Longer, yet more intuitive way:
#df['Total Stats'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#Shorter way:
df['Total Stats'] = df.iloc[:, 4:10].sum(axis = 1)
# ':,' means all (rows)
# axis = 1 is horizontal, axis = 0 is vertical
df.head(3)


# ## Deleting a Column

# In[36]:


# df = df.drop(columns = ['Total Stats'])
# df.head()


# ## Rearranging Columns

# In[69]:


cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(3)


# # Saving Data

# ## Saving Files AS a csv

# In[5]:


df.to_csv('modified.csv', index = False, sep = '\t')


# ## Saving files as an Excel

# In[ ]:


df.to_excel('modified.xslx', index = False)


# # Filtering Data

# ## >1 Requests, Advanced Filtering

# ### And ('&') Request

# In[7]:


#In pandas, & is used instead of 'and'
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]


# ### Or ('I') Request

# In[13]:


#In pandas, | is used instead of 'or'
df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]


# ### <, >, <=, >= Conditions

# In[19]:


df.loc[(df['Type 1'] == 'Grass') & (df['HP'] > 50)]


# ## Filtering Based on Text Patterns/Specific Words

# In[44]:


mega_df = df.loc[df['Name'].str.contains('Mega')]
mega_df.head()


# In[45]:


notmega_df = df.loc[~df['Name'].str.contains('Mega')]
notmega_df.head()


# ### Regex Filtering

# In[49]:


import re

fireorgrass = df.loc[df['Type 1'].str.contains('Fire|Grass', regex = True)]
fireorgrass


# In[51]:


#flags = re.I means ignore capitals
fireorgrass1 = df.loc[df['Type 1'].str.contains('fire|grass', flags = re.I, regex = True)]
fireorgrass1


# In[56]:


containswithpidf = df.loc[df['Name'].str.contains('Pi[a-z]*', regex=True)]
#Format: 'Characters You Want[other characters can be the any character]*'
# * means 0 or more characters
containspidf


# In[59]:


startswithlu = df.loc[df['Name'].str.contains('^Lu[a-z]*')]
startswithlu
# ^ means starts with


# # Reset Index

# In[38]:


new_df = df.loc[df['Generation'] == 2]
new_df
#What if we want the index (0th column) to start over at 0?


# ## Using .reset_index()

# In[ ]:


new_df = new_df.reset_index()
new_df


# ## Dropping Old Column

# In[37]:


#COOL! But the 1st column is the old index column. Let's drop it.
#new_df = new_df.reset_index(drop=True)
#new_df


# ## Using inplace=True

# In[39]:


new_df.reset_index(drop=True, inplace=True)
new_df


# # Conditional Changes

# ## Changing Values based on >1 Condition

# In[62]:


df.loc[df['Type 1'] == 'Rock', 'Type 1'] = 'Earth'
df


# In[65]:


df.loc[df['Type 1'] == 'Earth', 'Legendary'] = True
df
#Now all Earth pokemon are legendary


# In[72]:


df.loc[df['Total Stats'] > 500, ['Generation', 'Legendary']] = 'DEMO VALUE'
df.tail()


# # Aggregate Statistics (GroupBy)

# In[87]:


df = pd.read_csv('modified.csv')

# The .groupby() function is a way to look at the collective statistics of the parameter
df1 = df.groupby(['Type 1']).mean()
df1


# In[91]:


defensedf = df1.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
#Sorts Defense in order from smallest to largest
defensedf


# In[93]:


df.groupby(['Type 1']).count()


# In[95]:


df['count'] = 1
df


# In[99]:


df.groupby(['Type 1']).count()['count']


# # Working with Large Amounts of Data

# ## Using chunksize = # of Rows

# In[104]:


for df in pd.read_csv('modified.csv', chunksize = 5): #will load 5 rows
    print('CHUNK OF DF \n')
    print(df, '\n')


# ## Using pd.concat()

# In[108]:


new_df = pd.DataFrame(columns = df.columns)
#Creates new, empty dataframe with the same column name

for df in pd.read_csv('modified.csv', chunksize = 5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results], sort = True) 
    #Pends on results to 'new_df'
    
    print(new_df.head())


# # My First Pokemon

# In[23]:


df.loc[df['Name'] == 'Petilil']


# In[72]:


from PIL import Image
import matplotlib.pyplot as plt
im = Image.open(r'C:\Users\luchc\Downloads\petilil.png')
plt.imshow(im)

