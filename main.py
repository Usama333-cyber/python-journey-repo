#!st Day of Python Coding
#task 1:
#print your age
print("I am 21 years old")

# task 2:
#Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!
years = 27

#to convert years into days multiply it with 365
days = years * 365

#to convert it into weeks divide days by 7

weeks = days / 7

#to convert weeks into months multiply it by 4

months = days / 30

# Now print days weeks months
print("Total days in 27 years are: ", days)
print("Total weeks in 27 years are: ", weeks)
print("Total months in 27 years are: ", months)

# Task 3:
# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
radius = 5
pi = 3.1416

# formula for the area of the circle is area = pi * r**2
area = pi * pow(5, 2)
print("Area of the circle is :", area)