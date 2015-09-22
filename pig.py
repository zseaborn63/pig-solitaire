#This is my Pig Solitaire game
import random

import random

class Dice:

    def dice_roll(self):
        roll = random.randint(1, 6)
        return roll

class User:

    def __init__(self):
        self.user_bank = 0


    def user_roll(self):
        user_dice = Dice()
        self.user_curve = user_dice.dice_roll()
        return self.user_curve

    def user_choose(self):
        self.user_choice = input("Do you want to Roll again or Hold? R/H \n").lower()
        if self.user_choice == "h":
            return False
        else:
            return True

    def user_turn(self):
        user_turn_bank = 0
        player_to_roll = True
        while player_to_roll == True:
            x = self.user_roll()
            print(x)
            if x == 1:
                user_turn_bank = 0
                print("Round Over")
                player_to_roll = False
