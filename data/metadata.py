file = open("metadata_obamacops2.txt", 'r')

i = 0

for line in file:
	if line.find("+0000") != -1:
		i = 0
	if(i == 0):
		print line.replace("->", "DESCRIPTION:")
	elif(i == 1):
		print line.replace("->", "FOLLOWING:")
	elif(i == 2):
		print line.replace("->", "FOLLOWERS:")
	elif(i ==3):
		print line.replace("->", "LANGUAGE:")
	elif(i == 4):
		print line.replace("->", "LOCATION:")
	elif(i == 5):
		print line.replace("->", "FAVORITES:")
	elif(i == 6):
		print line.replace("->", "PLACE:")
	elif(i == 7):
		print line.replace("->", "CREATED:")
	i=i+1
