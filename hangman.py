import random

filename = open("hangman.txt")

dictionary = filename.read()
dic_split = dictionary.split()
random_word = random.sample(dic_split,1)
random_word = str(random_word[0])

blank_guess = []

for each in range(len(random_word)):
	blank_guess.append(" __ ")


print random_word
print "Welcome to hangman. You get seven chances to guess the mystery word."
print "-" * 7
# apple

player_guess = raw_input("Pick a letter ---> ")
player_guess.capitalize()


# if player_guess == #the previous guesses
# 	print "Sorry, you already guessed '%'" %letter
for letter in random_word:
	if letter == player_guess:
		blank_guess[random_word.find(letter)] = letter
print blank_guess
print ''.join(blank_guess)
# if player_guess in random_word

	# write %letter on the blanks
	# else:
		# draw hangman

#print "Guessed letters: %s" %(letter)
print "-" * 7


#print "Sorry, you already guessed %s" (letter)

print '   O    \n \ | / \n   |   \n  / \\ ' 