from brownie import NewGame
from scripts.helpful_scripts import get_account, mock_accounts
from scripts.contracts_balance import get_balance
from scripts.fund_game import fund_to_start, winners_prize
from random import randint
import time

contract_address = NewGame[-1]

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]
computer_account = mock_accounts()


# set player to False
player = False
player_account = get_account()

while player == False:
    amount = 1000000000000000

    # Funding contract 
    print('Player funding contract!')
    time.sleep(2)
    fund_to_start(player_account, contract_address, amount)
    print(f"Player has deposited {amount}\n")
    print('Computer is funding the contract!')
    time.sleep(2)
    fund_to_start(computer_account, contract_address, amount)
    print(f"Computer has deposited {amount}\n")

    time.sleep(3)
    print(f"The game's balance is {get_balance(contract_address)}\n")

    # set player to True
    # Players input
    print('=====  Player, please select one option  =====\n')
    player = input("=====  Rock, Paper, Scissors?  =====\n")
    
    # Game starts
    time.sleep(3)
    if player == computer:
        print("==== Tie! ====\n")
    elif player == "Rock":
        if computer == "Paper":
            print("==== You lose! ====", computer, "covers\n", player)
            time.sleep(5)
            print("====== Starting New Game ======\n \n")
        else:
            print("==== You win! =====", player, "smashes\n", computer)
            print(f"Your prize is of {get_balance(contract_address)}\n")
            winners_prize(contract_address, player_account)
            time.sleep(5)
            print("====== Starting New Game ======\n \n")

    elif player == "Paper":
        if computer == "Scissors":
            print("==== You lose! ====", computer, "cut\n", player)
            time.sleep(5)
            print("====== Starting New Game ======\n \n")
        else:
            print("==== You win! =====", player, "covers\n", computer)
            print(f"Your prize is of {get_balance(contract_address)}\n")
            winners_prize(contract_address, player_account)
            time.sleep(5)
            print("====== Starting New Game ======\n \n")

    elif player == "Scissors":
        if computer == "Rock":
            print("==== You lose! ====", computer, "smashes\n", player)
            time.sleep(5)
            print("====== Starting New Game ======\n \n")
        else:
            print("==== You win! =====", player, "cut\n", computer)
            print(f"Your prize is of {get_balance(contract_address)}\n")
            winners_prize(contract_address, player_account)
            time.sleep(5)
            print("====== Starting New Game ======\n \n")
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]