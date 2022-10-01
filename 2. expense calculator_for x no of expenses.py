#if no of expenses are not known, 
#start with sum as zero

sum=0
while True:
    x=int(input("Enter expense or Enter 0 to end loop \n"))# code to update 
    sum+=x #take here sum of x no of expenses
    if x == 0: #make sure you never make mistake here, there will be 2 equal signs :)
        sum+=x
        break
    else:
        print(sum)
