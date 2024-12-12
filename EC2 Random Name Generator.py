import random #module that provides random functions
import string #module for strings ie Ascii chars

#i = 0
Department=['Marketing','Accounting','FinOps']
DeptLow=['marketing','acconting','finops']
print ('The EC2 Name Generator is only for',Department,' departments, do not use any other names!')

Dprtnm = input("What is your Department name? ").lower()

if Dprtnm in DeptLow:
    EC2cnt = int(input("Please enter how many EC2's that require a name "))
    print ('Okay you will receive',EC2cnt,'Name(s) for',Dprtnm,'.')
    for i in range(EC2cnt):        
        print (Dprtnm, random.choice(string.ascii_uppercase),random.choice(string.digits))
else:
    print('You must be in one of the following Departments:\n',Department,'\n Please do not use the Name Generator!')

First_char = random.choice(string.ascii_uppercase)
Second_char = random.choice(string.digits)
#RandomName = First_char + Second_char

#RandomNumber = random.randint(1,10) #generates a random interger between 1 and 100
#Chars = string.ascii_uppercase + string.digits
#Length = 2
#Random_sequence = ''.join(random.choices(Chars, k=Length))




