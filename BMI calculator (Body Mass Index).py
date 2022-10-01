#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Develop a BMI calculator to monitor health.
#use persons height and weigth and output the BMI score.
#BMI = weight / sq. of height >> weight in kg and heigth in meters.
#make sure that both the inputs are as float.

#code starts here.
weight=float(input("Enter weight in kg \n")) #float will be used, otherwise decimal entry will create error
height=float(input("Enter height in meters \n")) #float will be used, otherwise decimal entry will create error

BMI=weight / height**2

if BMI < 18.5:
    print("You are underweight  \n")
elif BMI >= 18.5 and BMI <25:
    print("Your BMI score is normal \n")
elif BMI >=25 and BMI <30:
    print("You are overweight \n")
else:
    print("Obesity")

