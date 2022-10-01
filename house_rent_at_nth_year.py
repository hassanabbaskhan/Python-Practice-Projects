#!/usr/bin/env python
# coding: utf-8

# In[3]:


#this code is to calculate the house rent after nth no of year.
#assuming the increase in rent remains the same, like 10 percent annually.
#now let's start typing the code

x=int(input("Enter the current rent \n"))
y=int(input("Enter the no of years, after which the rent to be calculated \n"))
rent=x*1.1**y #1.1 is actually 10% increase of rent annually, which would be written as (100% + 10%)/100
print("The rent after",y,"years will be",rent)


# In[ ]:




