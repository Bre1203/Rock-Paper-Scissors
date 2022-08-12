import random

def rock_paper_scissors():
    print("Rock,Paper,Scissors,1,2,3!")
    player = input("Pick one! r,p,or s: ")
    ai_player = random.randint(1, 3)
    if player != 'r,s,or p':
        player=input("Oops...you didn't pick r,p,or s: ")


    if ai_player == 1:
        ai_player = 'r'

    if ai_player == 2:
        ai_player = 'p'

    if ai_player == 3:
        ai_player = 's'

    print("Computer played: " + ai_player)
    print("You played: " + player)

    if ai_player == player:
        print("Draw!")

    elif(ai_player == 'r' and player == 's') or (ai_player == 'p' and player == 'r')\
    or (ai_player == 's' and player == 'p'):
        print("You Loss")

    else:
        print("You Won!")

rock_paper_scissors()
