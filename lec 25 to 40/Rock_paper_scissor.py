'''
                ROCK PAPER SCISSOR GAME AGAINST COMPUTER
    Rules:
        rock wins against scissors          0=rock
        scissors wins against paper         1=paper
        paper wins against rock             2=scissor

    choices:        human       machine
                    0           0               :tie condition
                    0           1           :comp win
                    0           2           :user win
                    1           0           :user win
                    1           1               :tie condition
                    1           2           :com win 
                    2           0           :com win
                    2           1           :user win
                    2           2               :tie condition

Player 1: computer
Player 2: human

'''
import random

human=int(input("Input 0 for rock \n 1 for paper \n 2 for scissor \t"))
computer=random.randint(0,2)

if human==0 and computer==2:
    print("Human wins")

elif human==2 and computer==1:
    print("Human wins")

elif human==1 and computer==0:
    print("Human wins")

else:
    print("Computer wins")

print(f"you entered {human}")
print(f"computer entered {computer}")