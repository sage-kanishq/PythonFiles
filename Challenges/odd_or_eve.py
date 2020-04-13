from random import randrange as rr
from os import system 
player = 0
player2 =0
out = True
warning1 = 0
warning2 = 0
print('Player Batting')
while out:
    print(f'Score : {player}')
    shot_val = int(input('Run : '))
    comp = rr(0,7)
    if shot_val > 6 :
        warning1+=1
        print(f'Warning{warning1}: Number Invalid!')
        continue

    print(f'Bowler Bowls :{comp} \n')
    if comp == shot_val or warning1 >= 2:
        out = False
    else:
        player+=shot_val

out = True
system('clear')
print('Player Bowling')
while out:

    print(f'{player+1-player2} to win')

    print(f'Computer Score : {player2}')
    comp = rr(0,7)
    bowl = int(input('Ball : '))
    if bowl > 6 :
        warning2+=1
        print(f'Warning{warning2}: Number Invalid!')

    print(f'Batsman tries for a {comp}\n')

    if comp == bowl :
        out = False
    else:
        player2+=comp

    if player2>player or warning2 == 3:
        print('Computer Wins !')
        break

if player>player2:
    print('Player Wins')

elif player == player2:
    system('clear')
    print('Super Over')
    player = 0
    player2 = 0 
    supe = 6
    print('Player Bowling')
    print('\nRule :6 Wickets & 6 Balls||||||| Scores of both teams is 0 ')
    
    system('clear')
    
    print('Player batting')
    
    for i in range(6):
        print(f'Computer Score : {player2}\n')
        print(f'Balls Remaining : {supe-i}')
        comp = rr(0,7)
        bowl = int(input('Ball : '))
        if bowl > 6 :
            warning2+=1
            print(f'Number Invalid! Ball deducted')
            continue

        print(f'Batsman goes for a {comp}\n')

        if comp == bowl or warning2 == 3:
            continue
        else:
            player2+=comp
    supe = 6

    for i in range(6):
        print(f'Score : {player}\n')
        print(f'{player2+1-player} to win')
        print(f'Balls Remaining : {supe-i}')
        shot_val = int(input('Run : '))
        comp = rr(0,7)
        if shot_val > 6 :
            warning1+=1
            print(f'Warning{warning1}: Number Invalid!')

        print(f'Bowler Bowls :{comp} \n')
        if comp == shot_val or warning1 == 3:
            out = False
        else:
            player+=shot_val

        if player>player2:
            print('Player Wins')

if player<player2:
    print('Computer Wins')
    