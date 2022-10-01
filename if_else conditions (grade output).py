#calculating avegard and output the grade
#multiple if not allowed, instead use if elif elif elif and then else > print("Enter your marks")

Math=int(input("Enter marks of Math"))
English= int(input("Enter marks of English"))
Total=Math+English
avg=Total/2
if avg>=91 and avg<=100:  #avg < alone will not work at max range, <= together is working
    print("A+")
elif avg>=81 and avg<=90:
    print("A")
elif avg>=71 and avg<=80:
    print("B")
elif avg>=61 and avg<=70:
    print("C")
elif avg >=0 and avg<=60:
    print("Work Hard")
else:
    print("Invalid entry")
