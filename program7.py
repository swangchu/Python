import random
import time

first_no = int(input("Enter the first roll number:"))
last_no = int(input("Enter the last roll number:"))


def displayProcess():
    print("Next class presenter is ")
    time.sleep(3)
    print("...processing")
    time.sleep(2)
    print(".....processing")
    time.sleep(2)
    print(".....almost there")
    time.sleep(1)
    print("The presenter for the next class is :")
    time.sleep(1)
    print("Roll number:")
    time.sleep(1)
    
def randomRoll():
    roll_number = random.randint(first_no,last_no)
    return roll_number    

displayProcess()        
r = randomRoll()

print(r)   
