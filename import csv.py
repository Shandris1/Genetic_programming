import csv
import random


def main():
	learning_list,testing_list = grab_file ('n:/data1.txt')
	print (learning_list)
	print (testing_list)



def grab_file(filepath):
	with open(filepath, newline='') as inputfile:
 		results = list(csv.reader(inputfile))
 		#results.remove ('32 rows x 5 variables (+ class', ' space separated', ' CR EOL)')
 		del results[0]
 		random.shuffle (results)
 		learning_list,testing_list=split_list(results)

	return(learning_list,testing_list)

def split_list(input_list):
	length =len (input_list)
	length = int(length/2)
	learning_list = input_list[length:]
	testing_list = input_list[:length]
	return (learning_list,testing_list)

def fitness_check(input_list, tested_list, rules):
	for n in xrange(0,len(input_list)):
		
		pass
	
	pass

def output_check(input_list,tested_list,rules):
	
	pass


main()