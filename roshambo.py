import random

print "Welcome to Rock, Paper, Scissors!"
print "How many points are required for a win?"
points = int(raw_input())


long_word = {'r':'rock', 's':'scissors','p': 'paper'}

human_score = 0
comp_score = 0

message = ['A draw','Computer wins!','Human wins!']
message_key = 0

while human_score != points and comp_score != points:
	answer_key = random.randrange(0, 3)
	answer = ['r', 'p', 's']
	print "Choose (R)ock, (P)aper, or (S)cissors?"
	choice = raw_input()
	if choice == answer[answer_key]:
		message_key = 0
	elif choice == 'r' and answer[answer_key] == 's':
		message_key = 2
		human_score += 1
	elif choice == 'r' and answer[answer_key] == 'p':
		message_key = 1
		comp_score += 1
	elif choice == 'p' and answer[answer_key] == 'r':
		message_key = 2
		human_score += 1
	elif choice == 'p' and answer[answer_key] == 's':
		message_key = 1
		comp_score += 1
	elif choice == 's' and answer[answer_key] == 'p':
		message_key = 2
		human_score += 1
	elif choice == 's' and answer[answer_key] == 'r':
		message_key = 1
		comp_score += 1
	print "Human: %s  Computer: %s,  %s" % (long_word[choice], long_word[answer[answer_key]], message[message_key])
print "Final Score: Human", human_score, " Computer ", comp_score
