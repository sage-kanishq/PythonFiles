try:
    sides,obs = list(map(int,input().split(' ')))
    queenPos = tuple(map(int,input().split(' ')))
    obstacles = set()
    answer = 0
    safe = True
    for i in range(obs):
        position = tuple(map(int,input().split(' ')))
        obstacles.add(position)

    for l in range(1,sides+1):
        if (queenPos[0],queenPos[1]-l) not in obstacles and queenPos[1]-l!=0:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0]-l,queenPos[1]) not in obstacles and queenPos[0]-l!=0:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0]-l,queenPos[1]-l) not in obstacles and queenPos[0]-l!=0 and queenPos[1]-l!=0:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0]-l,queenPos[1]+l) not in obstacles and queenPos[0]-l!=0 and queenPos[1]+l!=sides+1:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0],queenPos[1]+l) not in obstacles and queenPos[1]+l!=sides+1:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0]+l,queenPos[1]) not in obstacles and queenPos[0]+l!=sides+1:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0]+l,queenPos[1]+l) not in obstacles and queenPos[0]+l!=sides+1 and queenPos[1]+l!=sides+1:
            answer+=1

        else:
            break

    for l in range(1,sides+1):
        if (queenPos[0]+l,queenPos[1]-l) not in obstacles and queenPos[0]+l!=sides+1 and queenPos[1]-l!=0:
            answer+=1

        else:
            break
    print(answer)

except Exception as e:
    print(e)



