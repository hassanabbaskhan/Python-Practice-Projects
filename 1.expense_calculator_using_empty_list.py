#!/usr/bin/env python
# coding: utf-8

# In[5]:


# the code calculates the sum of numbers in list.
# this code helps you in calculating the total of x no of expenses
#starting with empty list and initially with total as zero.

mylist=[]
total=0
while True:
    x=int(input("Enter expense, or Enter 0 to end the loop \n")) # expenses to be entered
    mylist.append(x) #expense is included in list
    print(mylist)  #lsit will be displayed for understanding
    total=sum(mylist) # sum of expense will be done here
    if x==0:
        print("the sum of all expenses will be",total) # this is only an addition, for easy output understanding
        break
    else:
      print("the sum of all expenses will be",total)


# In[ ]:





# In[ ]:




