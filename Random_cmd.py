import random
import string
import time
import os
from pathlib import Path

lower_Character = "abcdefghijklmnopqrstuvwxyz"
cap_character = lower_Character.upper()
nuberic = "0123456789"
sembol = ".@#$!<>@?:;*()"

inputuser = str(input(" Please choose your desired word to combine in the password : "))

all_character = inputuser + lower_Character + sembol + cap_character + nuberic

# Check is Empty File and Massage For User
with open("random_pass.txt", "r") as f:
    mypath = Path("random_pass.txt")
    passwords = f.readline()
    if mypath.stat().st_size == 0 and f.tell():
        print(" Storage space is empty and saving new values ")
    else:
        print("The storage location already contains password values")
# Created New Password in text File in renge   
start_time = time.time()
with open("random_pass.txt", "a") as f:
    rengeval = int(input(" Please enter your desired Range value : "))
    passlength = int(input("Please enter the length of the password : "))
    
    for i in range(rengeval):
        a = f.write(''.join(random.sample(all_character, passlength))+ '\n')
        
    if i == True :
        print(" The password list was created")
    else:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"The password list is being created {elapsed_time}")
    print("Your selected values have been created successfully")
    time.sleep(3)
        
      
   
            
