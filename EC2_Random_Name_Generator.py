import random #module that provides random functions
import string #module for strings ie Ascii chars

def EC2_Name_Generator():
    Department=['Marketing','Accounting','FinOps'] #list of current department requirements
    DeptLow=['marketing','accounting','finops']
    print ('The EC2 Name Generator is only for',Department,'departments, do not use any other names!')

    Dprtnm = input("What is your Department name? ").lower()

    if Dprtnm in DeptLow: #loop to print the number of EC2 names based on number of requested EC2 question
        EC2cnt = int(input("Please enter how many EC2's that require a name: "))
        print ('Okay you will receive',EC2cnt,'Name(s) for',Dprtnm.capitalize(),'.')
        for i in range(EC2cnt):        
            print (i+1,'.',Dprtnm.capitalize(), random.choice(string.ascii_uppercase),random.choice(string.digits))
            #prints out the count of EC2s along with entered department and assisgns a random letter and number to each instance.
    else:
        print('You must be in one of the following Departments:\n',Department,'\n Please do not use the Name Generator!')
EC2_Name_Generator






