#This is my Pig Solitaire game
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

class Game:

    def __init__(self):
        self.rounds_counter = 0
        self.user_score = 0
        self.computer_score = 0

    def play_round(self):
        da_ussa = User()
        da_computa = Computer_Player()
        print("---------------------")
        da_ussa.user_turn()
        print("=====================")
        da_computa.computer_turn()
        self.rounds_counter +=1
        print("You have played {} rounds".format(self.rounds_counter))
        print("+++++++++++++++++++++")
        self.computer_score += da_computa.computer_bank
        self.user_score += da_ussa.user_bank
        return self.user_score, self.computer_score

    def game_over(self):
        pass


    def play_game(self):
        while self.rounds_counter < 7:
            self.play_round()
            print("User {}, Computer {}".format(self.user_score, self.computer_score))
        print("The Final score is {} for the User and {} for the Computer".format(self.user_score, self.computer_score))
        if self.user_score > self.computer_score:
            print("User wins!")
        elif self.user_score < self.computer_score:
            print("The Computer wins!")
        else:
            print("The game was a tie!")

game = Game()
game.play_game()
