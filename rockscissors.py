import random

print "Welcome to Rock, Paper, Scissors!"
print "How many points are required for a win?"
points = int(raw_input())

ranks = { 	"r": "s",
			"s": "p",
			"p": "r"}

long_word = {'r':'rock', 's':'scissors','p': 'paper'}
message = ['A draw','Computer wins!','Human wins!']
message_key = 0

human_score = 0
comp_score = 0

while human_score != points and comp_score != points:
	print "Choose (R)ock, (P)aper, or (S)cissors?"
	hx = raw_input()
	loser = ranks[hx]
	hy_key = random.randrange(0, 3)
	hy = ['r', 'p', 's']
	if hx == hy:
		message_key = 0
	elif hy == loser:
		message_key = 2
		human_score += 1
	else:
		message_key = 1
		comp_score += 1
	print "Human: %s  Computer: %s,  %s" % (long_word[hx], long_word[hy[hy_key]], message[message_key])
print "Final Score: Human %d Computer %d" % (human_score, comp_score)





