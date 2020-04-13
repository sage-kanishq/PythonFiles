import enchant
Dictionary = enchant.Dict("en_UK")

player1 = True
player2 = False
arr_1 = []
word = ''
arr_2 = []
ghost = 'GHOST'
def play_game():
    game_on = True
    global word
    global player1
    global player2
    word = ''
    while(game_on):
        print(word)
        if player1:
            letter = input("Player1's chance : ")
            if letter.upper()=="CHALLENGE":
                challenge(arr_2)
                break      
            elif len(letter)>=2:
                word+= letter[0]
                if Dictionary.check(word):
                    pass
                else:
                    print(f"You cannot call continuous always.{word} is not a word")
                    print("Player1 wins this round")
                    arr_1.append(ghost[len(arr_1)])
                    break


            elif len(letter)==1:
                word+=letter
                if Dictionary.check(word) and len(word)>=2:
                    print(f"Player2 has won this round, {word} is a word")
                    arr_1.append(ghost[len(arr_1)])
                    game_on = False
                    break

        elif player2:
            letter = input("Player2's chance : ")
            if letter.upper()=="CHALLENGE":
                challenge(arr_1)
                break   
            elif len(letter)>=2:
                word+= letter[0]
                if Dictionary.check(word):
                    pass
                else:
                    print(f"You cannot call continuous always.{word} is not a word")
                    print("Player1 wins this round")
                    arr_2.append(ghost[len(arr_2)])
                    break

            elif len(letter)==1:
                word+=letter
                if Dictionary.check(word) and len(word)>1:
                    print(f"Player1 has won this round, {word} is a word")
                    arr_2.append(ghost[len(arr_2)])
                    break
        if player1:
            player1 = False
            player2 = True

        elif player2:
            player2 = False
            player1 = True

def challenge(arr):
    if arr is arr_1:
        letter = input(f"Player1 has been challenged. What was the word you were thinking about :\n")
        length = len(word)
        if letter[:length]==word and Dictionary.check(letter):
            arr_2.append(ghost[len(arr_2)])
            print("Player1 had thought of a word correctly.")
            print("Player2 will lose a life.")
            return

        else:
            print("Player1 could not think of a word correctly so he/she will lose a point")
            arr_1.append(ghost[len(arr_1)])
            return

    if arr is arr_2:
        letter = input(f"Player2 has been challenged. What was the word you were thinking about :\n")
        length = len(word)
        if letter[:length]==word and Dictionary.check(letter):
            arr_1.append(ghost[len(arr_1)])
            print("Player2 had thought of a word correctly.")
            print("Player1 will lose a life.")
            return

        else:
            print("Player2 could not think of a word correctly so he/she will lose a point")
            arr_2.append(ghost[len(arr_2)])
            return



for i in range(10):
    print("\n\n")
    print(f"Player1 : {''.join(arr_1)}")
    print(f"Player2 : {''.join(arr_2)}")
    print("\n")
    print(f"Round {i+1}")
    play_game()
    if "".join(arr_1) == ghost:
            print("Player2 has won the game!")
            break
    elif "".join(arr_2)== ghost:
        print("Player1 has won the game!")
        break
    
    

 