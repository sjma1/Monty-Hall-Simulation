# Seong Ma

'''
This program is a short simulation of the Monty Hall problem.

The Monty Hall problem states...

     """
     Suppose you're on a game show, and you're given the choice of three doors:
     Behind one door is a car; behind the others, goats. You pick a door,
     say No. 1, and the host, who knows what's behind the doors, opens another door,
     say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?"
     Is it to your advantage to switch your choice?
     """

'''

import random


if __name__ == '__main__':
    
    door1 = False
    door2 = False
    door3 = True
    doors = [door1, door2, door3]
    num_of_simulations = 1000000
    win_count = 0
    
    for simulation in range(num_of_simulations):
        random.shuffle(doors)
        
        if not doors[1]:
            choice = doors[2]
        else:
            choice = doors[1] 
 
        if choice:  #choice is correct
            win_count += 1
            
    win_ratio = win_count / num_of_simulations * 100
    print("In " + str(num_of_simulations) + " games, having made the choice to switch, ", end = '')
    print("you would have won " + str(win_count) + " games or " + str(win_ratio) + "games.\n")
    print("This demonstrates that given this problem, you should generally make the choice to switch.")
    