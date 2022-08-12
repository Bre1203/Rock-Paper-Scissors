import random

def rock_paper_scissors():
    print('rock,paper,scissors, 1, 2, 3,!')
    player=input('Pick one! (r,p,s!): ')
    ai_player=random.randint(1,3)
    if ai_player ==1:
        ai_player= 'r'

    if ai_player ==2:
        ai_player = 'p'

    if ai_player==3:
        ai_player='S'

    print('Computer played:  '+ ai_player)
    print('You played: '+ player)

    if ai_player == player:
        print('draw!')
    elif (ai_player=='r' and player =='s') or (ai_player=='p' and player =='r') \
    or (ai_player=='s' and player =='p'):
        print('loss!')

    else:
       print('Win!')

rock_paper_scissors()
