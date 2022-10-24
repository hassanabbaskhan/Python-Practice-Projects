#Q 5 Take 3 seperate List of Names age birth date

#and combine them and print them as single list like 
#('ali', 33, '1985_10_1') 
#('hassan', 30, '1990_12_1)

#use loops to auto fetch the combined list.

name=['ali','hassan','akbar','Farhan', 'Haris','Rizwan']
age=[30,40,20,23,45,27]
birth_date=['1992_12_30','1982_05_13','1993_10_15','1985_05_13','2007_05_16','2002_04_22']

x=len(name) #calculating the length of a list for loop working

while x>0:
    x=x-1     
    list=name[x],age[x],birth_date[x]
    print(list)
    
'''
The results will be as following...

('Rizwan', 27, '2002_04_22')
('Haris', 45, '2007_05_16')
('Farhan', 23, '1985_05_13')
('akbar', 20, '1993_10_15')
('hassan', 40, '1982_05_13')
('ali', 30, '1992_12_30')

'''
