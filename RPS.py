#importing the libraries

import random
import math

#defining variables

inventory = ['rock','scissors','paper']
choice_human = ""
choice_bot = random.choice(inventory)

#the main game is located in the infinite cycle

while True:
    
    #making a new choice evert time game ends
    
    choice_bot = random.choice(inventory)
    choice_human = input('rock/scissors/paper\n').strip().lower()
    
    if choice_human == "exit": #exit option
        break 
    if 'exit' not in choice_human and choice_human not in inventory:
        print("Uh oh, gotta go...") #checking for an idiot
        continue
    
    #algorithm for finding the winner
    
    elif choice_human in choice_bot:
        print("░░░░░░░░░░░░\n")
        print("Draw!")
        continue
    elif math.sqrt((inventory.index(choice_human) - inventory.index(choice_bot))**2) == 2 and inventory.index(choice_human) > inventory.index(choice_bot):
        print("You won!")
        continue
    elif math.sqrt((inventory.index(choice_human) - inventory.index(choice_bot))**2) == 1 and inventory.index(choice_human) > inventory.index(choice_bot):
        print("You lose!")
        continue
    elif math.sqrt((inventory.index(choice_human) - inventory.index(choice_bot))**2) == 1 and inventory.index(choice_human) < inventory.index(choice_bot):
        print("You won!")
        continue
    elif math.sqrt((inventory.index(choice_human) - inventory.index(choice_bot))**2) == 2 and inventory.index(choice_human) < inventory.index(choice_bot):
        print("You lose!")
        continue