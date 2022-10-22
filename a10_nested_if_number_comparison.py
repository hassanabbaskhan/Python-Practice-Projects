#!/usr/bin/env python
# coding: utf-8

# In[23]:


#comparison of numbers using Boolean expressions ( Or and statements)
num1=float(input("Enter Num1  "))
num2=float(input("Enter Num2  "))
if num1==num2:
    print("Both numbers are equal. ")
    print("Both numbers have same sign. ")
else:
    if num1 - num2 <=1 and num1 - num2 >=0 and num1 >0 and num2 >0:
        print("Both numbers are almost equal.")
        print("Both numbers are positive !")
    else:
        if num2 - num1 <= 1 and num2 - num1 >= 0 and num1 >0 and num2 >0:
            print("Both numbers are almost equal.")
            print("Both numbers are positive !")
        else:    
            if num1 - num2 <=1 and num1 - num2 >= 0 and num1 > 0 and num2 <0:
                print("Both numbers are almost equal.")
                print("Both numbers have different signs !") 
            else:
                if num2 - num1 <= 1 and num2 - num1 >= 0 and num1 > 0 and num2 <0:
                    print("Both numbers are almost equal.")
                    print("Both numbers have different signs !") 
                else:
                    if num1 > num2 and num1 > 0 and num2 > 0:
                        print("Num 1 is greater ")
                        print("Both numbers are postive")
                    else:
                        if num2 > num1 and num1 > 0 and num2 > 0:
                            print("Num 2 is greater ")
                            print("Both numbers are postive")
                        else:
                            if num1 > num2 and num1 > 0 and num2 < 0:
                                print("Num 1 is greater ")
                                print("Both numbers have different signs")
                            else:
                                if num2 > num1 and num2 > 0 and num1 < 0:
                                    print("Num 2 is greater ")
                                    print("Both numbers have different signs")
                                else:
                                    if num1 > num2 and num1 < 0 and num2 < 0:
                                        print("Num 1 is greater ")
                                        print("Both numbers are negetive")
                                    else:
                                        if num1 - num2 <=1 and num1 - num2 >=0 and num1 <0 and num2 <0:
                                            print("Both numbers are almost equal.")
                                            print("Both numbers are negetive !")
                                        else:
                                            if num2 - num1 <= 1 and num2 - num1 >= 0 and num1 <0 and num2 <0:
                                                print("Both numbers are almost equal.")
                                                print("Both numbers are negetive !")
                                            else:
                                                print("Recheck")


# In[ ]:




