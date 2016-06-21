file = open('generated_tweets.txt', 'r')

for line in file:
	lines = line.split(' ')
	for i in lines:
		print i
