import os
def play_game():
	word=input('Enter word : ').upper()
	expresser = ['_']*len(word)
	answer = "".join(expresser)
	life = 7
	inputs =[]
	vowels = ['A','E','I','O','U']
	hint=input('Enter Hint : ')
	os.system('clear')
	print(f'Hint : {hint}')
	print(f'Length : {len(word)}')

	for i in range(len(word)):
		if word[i] in vowels:
			expresser[i]=word[i]
			answer = "".join(expresser)

	num_word = 1

	for i in range(len(word)):
		if word[i] == ' ':
			expresser[i]=word[i]
			answer = "".join(expresser)
			num_word+=1

	print('Number of words : ',num_word)

	while life:
		print('\n',' '.join(expresser),'\n')
		letter = input("Enter Word :")
		letter = letter.upper()
		if letter in word and len(letter)==1 and letter not in inputs and letter not in vowels:
			inputs.append(letter)
			for i in range(len(word)):
				if word[i] == letter:
					expresser[i]=letter
					answer = "".join(expresser)


		else:
			life-=1

		if life==6:
			print('    /\\    ')
			print('   /  \\   ')
			print('   \\  /   ')
			print('    \\/    ')

		elif life == 5:
			print('    /\\    ')
			print('   /  \\   ')
			print('   \\  /   ')
			print('    \\/    ')
			print('     |    ')
			print('     |    ')
			print('     |    ')

		elif life == 4:
			print('    /\\    ')
			print('   /  \\   ')
			print('   \\  /   ')
			print('    \\/    ')
			print('     | \\  ')
			print('     |  \\ ')
			print('     |   \\ ')

		elif life == 3:
			print('    /\\    ')
			print('   /  \\   ')
			print('   \\  /   ')
			print('    \\/    ')
			print('   / | \\  ')
			print('  /  |  \\ ')
			print(' /   |   \\ ')

		elif life == 2:
			print('    /\\    ')
			print('   /  \\   ')
			print('   \\  /   ')
			print('    \\/    ')
			print('   / | \\  ')
			print('  /  |  \\ ')
			print(' /   |   \\')
			print('    /    ')
			print('   /     ')
			print('  /      ')

		elif life == 1:
			print('    /\\    ')
			print('   /  \\   ')
			print('   \\  /   ')
			print('    \\/    ')
			print('   / | \\  ')
			print('  /  |  \\ ')
			print(' /   |   \\ ')
			print('    / \\   ')
			print('   /   \\  ')
			print('  /     \\ ')

		elif life == 0:
			print(f'The Answer : {word}')
			print('You lose')
		if answer == word:
			print(answer,'\n')
			print('You Win')
			break