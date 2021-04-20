# Program Number 4:
#Write a program to calculate simple interest based on the type of loan they availed.
#The interest rate is 10% for housing loan, 12% for vehicle loan and 11% for business loan.
#Get the principal, time and type pf loan from the users. Display the simple interest.
#_____________________________________________________
# Author: Sonam Wangchu
# Date: April 20

# Get principal from users
principal = float(input("Enter the principal of the loan:"))
# Get time period of the loan
time = float(input("Enter the time: "))
# Get type of loans user wants to avail
loan_type = int(input("Enter number 1 for Housing, number 2 for Vehicle and number 3 for Business loan :"))
housing_rate = 0.1
vehicle_rate = 0.12
business_rate = 0.11
#Caluclate the simple interest
if loan_type == 1:
    si = principal * housing_rate * time
    # Print the simple interest
    print(f"The simple interest on the loan of Nu.{principal} at {housing_rate}% over the period of {time} years is Nu.",format(si,'.2f'))
elif loan_type == 2:
    si = principal * vehicle_rate * time
    # Print the simple interest
    print(f"The simple interest on the loan of Nu.{principal} at {vehicle_rate}% over the period of {time} years is Nu.",format(si,'.2f'))
else:
    si = principal * business_rate * time
    # Print the simple interest
    print(f"The simple interest on the loan of Nu.{principal} at {business_rate}% over the period of {time} years is Nu.",format(si,'.2f'))
    
