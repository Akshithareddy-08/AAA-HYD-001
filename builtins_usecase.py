
#use random module-->rock,paper,scissors

import random
player1 = input('enter the choice:-->rock,paper,scissors:').lower()
player2 = random.choice(['rock','paper','scissors']).lower()
print("player2 selection:",player2)
if player1 == "rock" and player2 == "paper":
    print("player2 win")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins")
elif player1 == player2:
    print("Its a tie")
else:
    print("player1 wins")

#task-->biuld a game generator sequences-->choice menu
#1- rock paper game
#2- story generator (random.choice()) [when,what,who,where-->]
#3- OTP generate to email
#4- BMI calculation

#build our 