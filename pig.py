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
        return self.user_choice

    def user_turn(self):
        user_turn_bank = 0
        player_to_roll = True
        while player_to_roll == True:
            roll_num = self.user_roll()
            print(roll_num)
            if roll_num == 1:
                user_turn_bank = 0
                print("Round Over")
                player_to_roll = False
            else:
            user_turn_bank += roll_num
            user_decision = self.user_choose()
                if user_decision == "h":
                    player_to_roll = False
                    self.user_bank += user_turn_bank
                    print(self.user_bank)
                else:
                    print(user_turn_bank)
                    player_to_roll = True
