def take_rounds(name):
    rounds_prompt=(f"Hey {name} How many round you want to play\n")
    flag = True
    while flag:
        rounds=int(input(rounds_prompt))
        if(rounds%2 == 1):
            print("Good Choice")
        
            if rounds>2 and rounds<10:
                print("Perfect")
                flag=False
                return rounds
            else:
                print("Choose odd number of rounds between 3 and 9")   
        else:
            print("No even rounds allowed")
        
        

import random
def computer_choice():
    option_list = ("Rock","Paper","Scissor")
    return random.choice(option_list)


def player_choice():
    option = input("R = Rock, P = Paper, S = Scissor --> ")
    
    if option=='r' or option=='R':
        return 'Rock'
    elif option=='p' or option=='P':
        return 'Paper'
    elif option=='s' or option=='S':
        return 'Scissor'
    else:
        player_choice()


def winning(computer_input,player_input):
    if player_input == computer_input:
        return 'draw'
    
    elif player_input == "Scissor" and computer_input == "Rock":
        return 'Computer'
    elif player_input == "Rock" and computer_input == "Paper":
        return 'Computer'
    elif player_input == "Paper" and computer_input == "Scissor":
        return 'Computer'
    
    
    elif player_input == "Rock" and computer_input == "Scissor":
        return 'Player'
    elif player_input == "Paper" and computer_input == "Rock":
        return 'Player'
    elif player_input == "Scissor" and computer_input == "Paper":
        return 'Player'
    

def check_Winner(round_list):
    player = round_list.count('Player')
    computer = round_list.count('Computer')
    draw = round_list.count('draw')
    
    if player>computer:
        return "Player"
    elif player<computer:
        return "Computer"
    else:
        return "--"


name = input("Hey Enter Your Name - ")
rounds = take_rounds(name)
subround_winning_list = []
for i in range(rounds):
    com_choice = computer_choice()
    pla_choice = player_choice()
    
    print(f"You chose {pla_choice} and computer chose {com_choice}")
    subround_winner = winning(com_choice,pla_choice)
    print(f"{subround_winner} won!!!")
    subround_winning_list.append(subround_winner)
    print("\n")
    
print(subround_winning_list)
print(f"{check_Winner(subround_winning_list)} is the winner!!!")


    