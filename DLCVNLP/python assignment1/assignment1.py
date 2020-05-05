'''Question1
Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.
'''
for i in range(2000,3201):
    if (i%5!=0 and i%7==0):
        print(i,end=",")  
print("")

'''Question2
Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
'''

first = input("Enter first name:")
last = input("Enter last name:")
print(last+" "+first)

'''Question3
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3'''
from math import pi
d=12
sphere_volume=4.0/3.0*pi*(d/2)**3
print("Volume of sphere is :",sphere_volume)



