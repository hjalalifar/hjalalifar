# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:34:23 2022

@author: Asus
"""
from random import randint

def playTurn():        
        diesum = 0
        again = "y"
        while again == "y" and diesum <= 21:
            diesum += randint(1,6)
            print(f"You now have {diesum}")
            again = input("Throw again? (y/n)")
        if diesum == 21:
            print("You win!")
        if diesum > 21:
            print("You lose.") 
        with open("player.txt", "w") as sc:    
            sc.write(str(diesum))
        return diesum

def dealerTurn():        
        diesum = 0
        again = "y"
        while again == "y" and diesum <= 21:
            diesum += randint(1,6)
            print(f"You now have {diesum}")
            again = input("Throw again? (y/n)")
        if diesum == 21:
            print("You win!")
        if diesum > 21:
            print("You lose.") 
        with open("dealer.txt", "w") as sc:    
            sc.write(str(diesum))
        return diesum
    
playing = True
while playing:
    dealerSum = 0
    print("Player throws:")
    playerSum = playTurn()
    if playerSum < 21:
        print("Dealer throws:")
        dealerSum = dealerTurn()
    score = playerSum-dealerSum
    if score == 0:
        print("Tie!")
    elif score < 0:
        print("Dealer wins")
    else:
        print("Player wins")        


    playing = input("Play again? (y/n)") == "y"
print(f"Thank you for playing blackjack. I hope you had a good time.")
