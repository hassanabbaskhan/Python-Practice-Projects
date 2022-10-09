

"""
Problem Statement:

You have to check through code, either the input no is a prime no or not"""

prime= True #Starting with True statment
num = int(input("Enter no. \n")) #the input value, which should be greater than 1

if num >1:

    for i in range(2,num):  #starting for loop, [i is the initiator] we are declaring a range starting from 2 upto num with increment of 1

        if (num % i)==0:      # if in loop, any time remainder is zero, 
                          #if above statement is to be tested like for num=5, which means
                          #comments.. range is 2,3,4,5 and input value will be divided by each no of range, 
                          #num % i means, 5/2 and 5/3 and 5/4 (in all these cases, remainder is not zero)
                          
                          #for num=6, we will have num % i like 
                            # (6/2 results in zero remainder, so the loop will stop here, )

            prime= False         # if remainder condion is met, in such case prime will be False...
if not prime:                 # if conditions is met above, like i tried to describe, it will not be prime no..., 
    print(num, "is not Prime number") 
else:
    print(num,"is a Prime number")
