"""The program allows the user to enter the raduis of the sphere 
and calculate the volume given that (volume = (4/3)*3.14 *(r*r*r)"""
pie  = 3.14
r = int(input("Enter the radius of the sphere:"))
volume = (4/3)* pie * (r*r*r)

print("The volume is: ",volume)