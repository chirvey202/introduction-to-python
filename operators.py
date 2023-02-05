#basic operators in python
#addition of two operands
a=13
b=3
#addition of a and b
print(a+b)
#addition of b and a
print(b+a)
#subtract b from a
print(b-a)
#multiply b and a
print(b*a)
#divide b and a
print(b/a)
#divide b and a
print(b//a)
#modulers
print(b%a)


#a program that prompt the user to test if a number is divisible by 5
num=int(input("Enter a number:"))
if (num%5==0):
 print("The number is divisible by 5")
else:
     print("The number is not divisible by 5:")

     #print whether a number is even or odd
     num=int(input("Enter a number:"))
if (num%2==0):
       print("The number is even:")
else:
         print("The number is not even:")

#RELATIONAL OPERATORS

#write a program to assign a discount of 5% if amount of purchase exceeds sh 1000
amount=int(input("Enter amount:"))
discount=0.05*amount
if(amount>=1000):
  print("discount is given is:",discount)
else:
     print("a discount is not given:")

#LOGICAL OPERATORS
#A program to check if a person is eligible to vote or not
nationality = input("Enter nationality:")
age=int(input("enter the age:"))

if nationality=='kenyan' and age>=18:
  print("Eligible to vote")
else:
   print("NOT eligible to vote")   


"""computer program to implement the following;a bank will offer a loan is they are 21 and over and
have an annual income of atleast 21000.The customers age and income are input
Expected output
1.Congratulation if you qualify for a loan
2.Unfortunately.we are unable to offer you a loan at this time"""

age=(int("Enter the age:"))
annual_income=int("Enter the annual income:")

if age>=21 and annual_income>=21000:
   # print("Given a loan")
    print("congratulation for the qualification")
else:
    #print("Not given a loan") 
    print("unfortunately,we are unable to offer you loan at this time") 



