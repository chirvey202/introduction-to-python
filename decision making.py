"""write a program to find the largest of 3 numbers """
numb1=int(input("Enter the first number:"))
numb2=int(input("Enter the second number:"))
numb3=int(input("Enter the third number:"))
if(numb1>numb2 and numb1>numb3):
    print("Number1 is the largest")     
elif(numb2>numb1 and numb2>numb3):
    print("Number2 is the largest")
else:
    print("Number3 is the largest")

    """a program to ask the user to enter their salary and the years of service and print
    the net bonus amount given
    Time of bonus       Bonus
    more than 10 years    10%
    >=6 and <=10            8%
    Less than 6 years       5% """
    salary=int(input("Enter the salary:"))
    years_of_service=int(input("Enter the years of service:"))
    if(years_of_service>10):
        net_bonus_amount=salary+(salary*0.1)
    elif(years_of_service>=6 and years_of_service<=10):
        net_bonus_amount=salary*(salary*0.08)
        print("net bonus amount is",net_bonus_amount)
    else:
        (years_of_service>6)
        net_bonus_amount=salary+(salary*0.05)
        print("Net bonus amount is",net_bonus_amount) 


    """grading system"""
sub1=int(input("subject1 is:"))
sub2=int(input("subject2 is:"))
sub3=int(input("Subject3 is:"))
average=(sub1+sub2+sub3)/3

if(average>=70 and average<=100):
    print("Grade B")
elif(average<=60 and average<=69):
    print("Grade C")
elif(average>=50 and average<=59):
    print("FAIL") 
elif(average>=0 and average<=39):
    print("Grade")
else:
    print("Not found")             
        

