# Program Number 5:
# Write a python program to calculate the population density of a country.
#Your program should get the total population and total area of the country.
# Display the population density with correct units.
#_____________________________________________________
# Author: Sonam Wangchu
# Date: April 20

# Get total population of a country from users
population = int(input("Enter population of the country :"))
# Get area of a country
area = float(input("Enter the area of the country : "))

# Calculate the population density
# pd = population / area

density = population / area

print(f"The population density of a country with {population} people and area of {area} Sq. Km is ", round(density),"person per square KM.")
