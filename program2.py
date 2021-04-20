# Program Number 2:
# A ball is dropped from a tower of height h. 
# It has initial velocity zero and accelerates downwards under gravity. 
# Write a program that asks the user to enter the height in meters of the tower and a time interval t in seconds, 
# then prints on the screen the height of the ball above the ground at time t after it is dropped, ignoring air resistance. 
# If the height of the ball is zero then print the ball hit the ground.
# -------------------------------------------------------------------------
#Author: Sonam Wangchu
#Date : April 20 2021

# Get height of the tower from the user
tower_height = float(input("Enter the height of the tower in meters:"))
# Get the time interval after the ball is being dropped
time = float(input("Enter the time interval:"))

# Caluclate the distance travlled by the ball after a time under earth's gravity
# formula s = (1/2)*g*t**2 , where g = 9.8 m/ sec square

ball_travelled = 0.5 * 9.8 * time * time
distance_diff = tower_height - ball_travelled

# Check if the ball touched the ground

if distance_diff <= 0:       # if the difference is equal to zero or negative then the ball is on the ground
    print("The ball touched the ground.")
else:
    print("The ball is still in the air at ",format(ball_travelled,'.3f'),"meter.")
    # format(ball_travelled,'.3f') with print a numnber with three dicimal places.
