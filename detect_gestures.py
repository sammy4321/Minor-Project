import numpy as np
import random
import activate_functions



def get_data(filename):
	file = open(filename,'r')
	data = []
	for line in file.readlines():
		line = line[:-1]
		splits = line.split('-')
		row=[]
		#print('Name : ',splits[0])
		#print('Values : ',splits[1])
		row.append(splits[0])
		for j in splits[1].split(','):
			row.append(int(j))
		data.append(row)
	#print(data)
	file.close()
	return data

def get_gesture_name(values,data):
	dist = 99999
	name = ''
	for row in data:
		new_dist = (row[1] - values[0])**2 + (row[2] - values[1])**2 + (row[3] - values[2])**2 + (row[4] - values[3])**2 + (row[5] - values[4])**2 + (row[6] - values[5])**2 + (row[7] - values[6])**2 + (row[8] - values[7])**2
		if new_dist < dist:
			dist = new_dist
			name = row[0]
	return name


def main():
	data = get_data('gestures')
	value = []
	for _ in range(8):
		value.append(random.randint(0,25))
	name = get_gesture_name(value,data)
	#name = 'hello'
	method_to_call = getattr(activate_functions,name)
	method_to_call()
	#print(name)


main()