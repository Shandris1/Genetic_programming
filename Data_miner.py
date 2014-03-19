import random
random.seed
import re
import pprint
import csv


def main():

    global pp
    pp = pprint.PrettyPrinter(indent = 2)
    pool_fit = []
    parent_fit = []
    highest_fitness_total, p, Total_fitness = 0, 0, 0
    top_fitness_member = []
    #Beginning of changibles__________________________
    #insert length of the gene here
    L = 5
    #insert the population size here
    Num = 5
    #insert number of parents here
    Parents = 5
    #insert number of generations here
    Overall_generations = 500
    #insert probability of crossover
    Crossover_chance = 90
    #insert probability of mutation
    mutation_chance = 10
    #end of chanibles_______________________________
    #populate the array with random binary number
    #replace pool fit and intergrate it into pool_gene

    learning_list,testing_list = grab_file ('n:/data1.txt')

    pool_gene = initialise_rule_pool(Num,L)
    #pp.pprint(pool_gene)
    pool_gene = fitness_check (pool_gene,learning_list)
    #for i in range(0,Num) :
    #    pool_fit.append(sum (pool_gene[i][0]))
    #    print ('this parent\'s fitness = ',pool_fit[i])
    for i in range(0,len(pool_gene)):
        Total_fitness += pool_gene[i][2]
    Averege_fitness = Calculate_averege_fit (pool_gene, Num)
    #print ("pool_gene",pool_gene)
    top_fitness_member = pool_gene[0]
    #print("Total_fitness" ,Total_fitness)
    #print("Averege_fitness" ,Averege_fitness)
#Main loop of the function
    for gen in range(0,Overall_generations) :
        top_fitness_member = find_top_fitness(pool_gene,top_fitness_member)
        parent_gene = roulette_wheel_selection(pool_gene,pool_fit,Num,Parents,top_fitness_member)
        #print("parent_gene = ", parent_gene)
        #parent_gene = tournament_selection(pool_gene[0],pool_fit,Num,Parents,top_fitness_member)
        #for p in range(0,Parents):
        #    parent_fit.append(sum (parent_gene[p][0]))
        #Total_fitness = sum(parent_gene[p][0])
        #Averege_fitness = Calculate_averege_fit (parent_fit, Num)
        #print("parent_gene",parent_gene)
        mutant_gene=Mutation(parent_gene,mutation_chance,Num)
        #print("parent_gene",parent_gene)
        #print("mutation   ",mutant_gene)
        crossed_gene=Crossover(mutant_gene,Crossover_chance,Num)
        
        

        pool_gene = crossed_gene
        pool_gene = fitness_check (pool_gene,learning_list)
        #print(pool_gene)
        for i in range(0,len(pool_gene)):
            Total_fitness += pool_gene[i][2]
        Averege_fitness = Calculate_averege_fit (pool_gene, Num)
        print("        Total_fitness=" ,Total_fitness)
        print("      Averege_fitness=" ,Averege_fitness)
        highest_fitness_total = Total_fitness if Total_fitness > highest_fitness_total else highest_fitness_total
        print("highest_fitness_total=",highest_fitness_total)
        print(" highest_member_total= ",top_fitness_member[2])
        if top_fitness_member[0][2]==L:
            print("success! generations used =",gen)
            break
        p, Averege_fitness, Total_fitness = 0,0,0
        pool_fit = []
        parent_fit = []
        #for fit in range(0,Num):
            #pool_fit.append(sum (parent_gene[fit]))



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
    for i in range(0,len(rules)):
        fitness = 0      
        rule_string = ''.join(rules[i][0])
        #print("list=",input_list)
        for data in input_list:
            #print("rule string/datastring",rule_string,data[0])
            if re.match(rule_string,data[0]):
                fitness += 1
                if rule_string[1] == data[1]:
                    fitness += 1
            rules[i][2]=fitness
        #print("rules = ", rules)
    return rules

def initialise_rule_pool(rule_input_length,rule_length):
    rule_set = []
    value_member = []
    for member in range(0,rule_input_length):
        value_rule = list(range(rule_length))
        for rule in range(0,rule_length):
            value_rule[rule] = random.choice(['0','1','[01]'])
        value_fitness = 0
        value_member.append([value_rule,random.choice([0,1]),value_fitness])

    return value_member

def find_top_fitness(pool_gene,top_fitness_member):
    pool_fit = []
    top_fitness_member_current = {}
    top_fitness_member_current[0] = 0
    for fit in range(0,len(pool_gene)):
        pool_fit.append(pool_gene[fit][2])
    for i in range(0,len(pool_gene)):
        if int(pool_fit[i]) > int(top_fitness_member[2]):
            top_fitness_member_current=list(pool_gene[i])
            top_fitness_member = list(top_fitness_member_current)
    if top_fitness_member_current[0] == 0:
        top_fitness_member_current = list(top_fitness_member)
    return top_fitness_member_current


def roulette_wheel_selection(pool_gene,pool_fit,Num,Parents,Best_member):
    parent_gene = []
    for x in range(0,Parents):
        fitness_sum = 0
        for i in range(0, len(pool_gene)):
            fitness_sum += pool_gene[i][2]
        #print("fitness_sum",pool_gene)
        roulette_drop = random.randint(1,fitness_sum)
        i, fitness_sum = -1, 0
        while roulette_drop > fitness_sum:
            i = i + 1
            fitness_sum += pool_gene[i][2]
        parent_gene.append(list(pool_gene[i]))
    parent_gene[0] = Best_member
    return parent_gene
"""

def tournament_selection(pool_gene,pool_fit,Num,Parents,Best_member):
    parent_gene= {}
    top_fitness_member_tournament={}
    for population in range (0,Num):
        tournament_temp = {}
        numbers = list(map(int,range(0,Num)))
        for x in range (0,10):
            r = random.choice(numbers)
            tournament_temp[x]=list(pool_gene[r])

            numbers.remove(r)
        top_fitness_member_tournament[0] = list(pool_gene[r])
        top_fitness_member_tournament = find_top_fitness(tournament_temp,top_fitness_member_tournament)
        parent_gene[population] = list (top_fitness_member_tournament[0])
        top_fitness_member_tournament = [r]
    return parent_gene
        """
    
def Calculate_averege_fit(pool_fit,Size_of_population):
    Total_fitness = 0
    for i in range(0,len(pool_fit)):
        Total_fitness += pool_fit[i][2]
    Averege_fitness = Total_fitness/Size_of_population
    return Averege_fitness

# 
def Mutation(parent_gene,mutation_chance,population_size):

    gene_length = 0 
    mutant_gene_pool = []
    #print("parent_gene", parent_gene)
    for i in range(0,population_size):            
        mutant_gene = [] 
        gene_length = len(parent_gene[0][0])
        for x in range (0, gene_length) :
            if (random.randint(0,99) < mutation_chance):
                mutant_gene.append(random.choice(['0','1','[01]']))
            else:
                mutant_gene.append(parent_gene[i][0][x])
        #mutant_gene_pool_temp=[mutant_gene,parent_gene[i][1],parent_gene[i][2]]
        mutant_gene_pool.append([mutant_gene,parent_gene[i][1],parent_gene[i][2]])
    #print("mutant_gene",mutant_gene)
    return mutant_gene_pool

def Crossover(mutant_gene,Crossover_chance,population_size):
    #gene_length = len(mutant_gene)
    #print("crossover_gene",mutant_gene)
    crossover_times=population_size
    if (crossover_times%2==0):
        crossover_times=int((crossover_times/2))
        population_size_crossover=population_size
    else:
        crossover_times=int((crossover_times-1)/2)
        population_size_crossover=population_size-1
    numbers = list(map(int,range(0,population_size_crossover)))#possible bug. if broken change 0 to 1
    for x in range(1,crossover_times):
        if(random.randint(0,99)<Crossover_chance):
            r = random.choice(numbers)
            numbers.remove(r)
            #print("r",r)
            crossover_gene_1 = mutant_gene[r]
            s = random.choice(numbers)
            numbers.remove(s)
            #print("s",s)
            crossover_gene_2 = mutant_gene[s]
            pt = random.randint(1,population_size-1)
            #print("crossover_gene_1",crossover_gene_1)
            #print("crossover_gene_2",crossover_gene_2)
            crossover_gene_3 = crossover_gene_1[:pt] + crossover_gene_2[pt:]
            crossover_gene_4 = crossover_gene_2[:pt] + crossover_gene_1[pt:]
            #print("crossover_gene_3",crossover_gene_3)
            #print("crossover_gene_4",crossover_gene_4)
            mutant_gene [r] = list(crossover_gene_3) 
            mutant_gene [s] = list(crossover_gene_4)
    return mutant_gene


main()
