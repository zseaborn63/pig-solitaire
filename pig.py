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
        self.user_choice = input("Do you want to Roll again "
                                 "or Hold? R/H \n").lower()
        return self.user_choice

    def user_turn(self):
        user_turn_bank = 0
        player_to_roll = True
        while player_to_roll == True:
            user_roll_num = self.user_roll()
            print(user_roll_num)
            if user_roll_num == 1:
                user_turn_bank = 0
                print("Round Over")
                print("Your total round score is {}".format(self.user_bank))
                player_to_roll = False
            else:
            user_turn_bank += user_roll_num
            user_decision = self.user_choose()
                if user_decision == "h":
                    player_to_roll = False
                    self.user_bank += user_turn_bank
                    print("Your total round score is {}".format(self.user_bank))
                else:
                    print("Your current round score is {}".format(user_turn_bank))
                    player_to_roll = True

class Computer_Player:

    def __init__(self):
        self.computer_bank = 0

    def computer_roll(self):
        computer_dice = Dice()
        self.computer_curve = computer_dice.dice_roll()
        return self.computer_curve

    def computer_choose(self):
        self.computer_choice = random.choice(['h', 'r'])
        return self.computer_choice

    def computer_turn(self):
        computer_turn_bank = 0
        computer_to_roll = True
        while computer_to_roll == True:
            computer_roll_num = self.computer_roll()
            print(computer_roll_num)
            if computer_roll_num == 1:
                computer_turn_bank = 0
                print("Round Over")
                print("Computer total turn score is {}".format(self.computer_bank))
                computer_to_roll = False
            else:
                computer_turn_bank += computer_roll_num
                computer_decision = self.computer_choose()
                if computer_decision == 'h':
                    computer_to_roll = False
                    self.computer_bank += computer_turn_bank
                    print("Computer total turn score is {}.".format(self.computer_bank))
                else:
                    print("Computer current turn score is {}.".format(computer_turn_bank))
                    computer_to_roll = True
