# Program Number 3:
#Write a python program to calculate the simple interest
#for a loan. Your program should get principal, rate and
#time in year form the users. Display the simple interest.
#_____________________________________________________
# Author: Sonam Wangchu
# Date: April 20

# Get principal from users
principal = float(input("Enter the principal of the loan:"))
# Get rate in decimal from the user
rate = float(input("Enter the rate in decimal: "))
# Get time period of the loan
time = float(input("Enter the time: "))

#Caluclate the simple interest

si = principal * rate * time
# Print the simple interest
print(f"The simple interest on the loan of Nu.{principal} at {rate}% take over the period of {time} years is Nu.",format(si,'.2f'))

