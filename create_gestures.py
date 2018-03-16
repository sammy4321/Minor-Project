import random

letters = 'abcdefghijklmnopqrstuvwxyz'


no_of_gestures = 15
no_letters_in_name = 4

file = open('gestures','w')
ff = open('activate_functions.py','w')

for _ in range(no_of_gestures):
	line = ''
	for _ in range(no_letters_in_name):
		index = random.randint(0,25)
		line = line + letters[index]
	ff.write('def '+line+'():\n')
	ff.write('\tprint("Inside Function '+line+'")\n\n')
	line = line + '-'
	for _ in range(8):
		number = random.randint(0,25)
		line = line + str(number) + ','
	line = line[:-1] + '\n'
	#index = random.randint(0,25)
	#print(line)
	file.write(line)

file.close()
ff.close()