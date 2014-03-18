import csv
import random
random.seed
import pprint
import re


def main():
	Number_of_inputs = 20
	input_length = 5
	mutation_chance = 10
	Crossover_chance = 90
	generations = 1
	Num = 20
	Parents = 20
	global pp
	pp = pprint.PrettyPrinter(indent = 2)
	rules_dict = {}
	learning_list,testing_list = grab_file ('n:/data1.txt')
	print (learning_list)
	print (testing_list)
	Best_member={}




	rules_dict = initialise_rule_pool(Number_of_inputs,input_length)

	Best_member[0] = {"fitness":0}

	for gen in range(0,generations):
		print ("generation = ", gen)
		rules_dict = fitness_check( rules_dict, learning_list)
		Best_member[0] = dict(find_highest_fitness(rules_dict, Best_member))
		#pp.pprint(rules_dict)
		#Best_member = find_highest_fitness (rules_dict, Best_member)
		pp.pprint(rules_dict)
		rules_dict = roulette_wheel_selection (rules_dict,Num,Best_member)
		rules_dict = Mutation (rules_dict,mutation_chance,Num)
		pp.pprint(rules_dict)
		rules_dict = Crossover(rules_dict,Crossover_chance,Num)
		pp.pprint(rules_dict)
	pp.pprint(rules_dict)

def initialise_rule_pool(rule_input_length,rule_length):
	rule_set = {}
	for member in range(0,rule_input_length):
		value_rule = list(range(rule_length))
		value_member = {}
		for rule in range(0,rule_length):
			value_rule[rule] = random.choice(['0','1','[01]'])
		value_fitness = 0
		value_member["rule"] = value_rule
		value_member["result"] = random.choice([0,1])
		value_member["fitness"] = value_fitness
		rule_set[member] = value_member
	return rule_set
	




def grab_file(filepath):
	with open(filepath, newline='') as inputfile:
 		results = list(csv.reader(inputfile, delimiter=' ', quotechar='|'))
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

def fitness_check(rules, input_list):
	for key, member in rules.items():
		fitness = 0
		rule_string = ''.join(member['rule'])
		for data in input_list:
			if re.match(rule_string, data[0]):
				fitness += 1
				if member['result'] == data[1]:
					fitness += 1
		rules[key]['fitness'] = fitness
	return rules


def sum_of_fitness(pool_gene):
    current_total = 0
    for member, value in pool_gene.items():
        current_total = current_total + pool_gene[member]["fitness"]
    return current_total

def roulette_wheel_selection(pool_gene, parents_number, highest_fitness_member):
    parents_gene = {}
    pool_size=len(pool_gene)

    current_fitness_total = sum_of_fitness(pool_gene)
    for parent in range(0,parents_number-1):
        cutoff = random.randint(0,current_fitness_total)
        fitness_sum = 0 #resets the fitness counter
        for member in range(0,pool_size):
            fitness_sum = fitness_sum + pool_gene[member]["fitness"] #increases the fitness counter by the current members fitness
            if fitness_sum >= cutoff: 
                parents_gene[parent] = pool_gene[member]
                break
    parents_gene[parents_number-1] = dict(highest_fitness_member)
    return parents_gene
"""
def roulette_wheel_selection(pool_gene,Num,Parents,Best_member):
    parent_gene = {}
    for x in range(0,Parents):
        fitness_sum = 0
        print (pool_gene)
        for i in range(0, len(pool_gene["fitness"])):
            fitness_sum = fitness_sum + pool_gene[i]["fitness"]
        roulette_drop = random.randint(1,fitness_sum)
        i, fitness_sum = -1, 0
        while roulette_drop > fitness_sum:
            i = i + 1
            fitness_sum = fitness_sum + pool_gene[i]["fitness"]
        parent_gene[x] = list(pool_gene[i])
    parent_gene[0] = list(Best_member[0])
    return parent_gene"""


def find_highest_fitness(pool_gene, highest_fitness_member):
	highest_fitness_member_current = {}
	for member in range(0,len(pool_gene)):
		if pool_gene[member]["fitness"] > highest_fitness_member[0]["fitness"]:
			highest_fitness_member_current = dict(pool_gene[member])
			highest_fitness_member[0]["fitness"] = pool_gene[member]["fitness"]
	if not any(highest_fitness_member_current):
		highest_fitness_member_current = dict(highest_fitness_member[0])
	print (highest_fitness_member_current)
	return highest_fitness_member_current


def Mutation(parent_gene,mutation_chance,population_size):
	mutated_gene = {}
	
	pool_size=population_size
	gene_length=len(parent_gene[0]["rule"])
	print ("parent_gene = ",parent_gene)
	for member in range(0,pool_size-1):#fix this
		for gene in range (0,gene_length):
			if (random.randint(0,99) < mutation_chance*1.5):
				print ("member",member)
				print ("gene",gene)
				print ("parent_gene",parent_gene)
				parent_gene[member]["rule"][gene] = random.choice(['0','1','[01]'])

		#mutated_gene[member] = {"rule":parent_gene}
	print ("end of mutaton = ",parent_gene)
	return parent_gene


def Crossover(mutant_gene,Crossover_chance,population_size):
    #gene_length = len(mutant_gene)
    crossover_times=population_size
    if (crossover_times%2==0):
        crossover_times=int((crossover_times/2))
        population_size_crossover=population_size
    else:
        crossover_times=int((crossover_times-1)/2)
        population_size_crossover=population_size-1
    numbers = list(map(int,range(1,population_size_crossover)))
    for x in range(1,crossover_times):
        if(random.randint(0,99)<Crossover_chance):
            r = random.choice(numbers)
            numbers.remove(r)
            crossover_gene_1 = mutant_gene[r]["rule"]
            s = random.choice(numbers)
            numbers.remove(s)
            crossover_gene_2 = mutant_gene[s]["rule"]
            pt = random.randint(1,population_size-1)
            crossover_gene_3 = crossover_gene_1[:pt] + crossover_gene_2[pt:]
            crossover_gene_4 = crossover_gene_2[:pt] + crossover_gene_1[pt:]
            print ("crossover_gene1", crossover_gene_1)
            print ("crossover_gene2", crossover_gene_2)
            print ("crossover_gene3", crossover_gene_3)
            print ("crossover_gene4", crossover_gene_4)
            mutant_gene [r]["rule"] = list(crossover_gene_3) 
            mutant_gene [s]["rule"] = list(crossover_gene_4)
            print(mutant_gene)
    return mutant_gene


"""
gene_length = 0 
mutant_gene = {}
for key, member in parent_gene.items():
	rule_string = ''.join(member['rule'])
	for slot in range(0, 5):
		if (random.randint(0,99) < mutation_chance*1.5):
			print (rule_string)
			rule_string[slot] = random.choice(['0','1','[01]'])
		mutant_gene[member] = {"rule":rule_string}
return parent_gene
"""


main()