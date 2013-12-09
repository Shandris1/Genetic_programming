import random
random.seed


def main():

    
    pool_fit = []
    parent_fit = []
    highest_fitness_total, p, Total_fitness = 0, 0, 0
    top_fitness_member = {}
    #Beginning of changibles__________________________
    #insert length of the gene here
    L = 50
    #insert the population size here
    Num = 50
    #insert number of parents here
    Parents = 50
    #insert number of generations here
    Overall_generations = 500
    #insert probability of crossover
    Crossover_chance = 90
    #insert probability of mutation
    mutation_chance = 1
    #end of chanibles_______________________________
    #populate the array with random binary number
    pool_gene = initialise_gene_pool(Num,L)
    for i in range(0,Num) :
        pool_fit.append(sum (pool_gene[i]))
        print ('this parent\'s fitness = ',pool_fit[i])
    Total_fitness = sum(pool_fit)
    Averege_fitness = Calculate_averege_fit (pool_fit, Num)
    top_fitness_member[0] = list(pool_gene[0])
    print("Total_fitness" ,Total_fitness)
    print("Averege_fitness" ,Averege_fitness)
#Main loop of the function
    for gen in range(0,Overall_generations) :
        top_fitness_member = find_top_fitness(pool_gene,top_fitness_member)
        #parent_gene = roulette_wheel_selection(pool_gene,pool_fit,Num,Parents,top_fitness_member)
        parent_gene = tournament_selection(pool_gene,pool_fit,Num,Parents,top_fitness_member)
        for p in range(0,Parents):
            parent_fit.append(sum (parent_gene[p]))
        Total_fitness = sum(parent_fit)
        Averege_fitness = Calculate_averege_fit (parent_fit, Num)
        mutant_gene=Mutation(parent_gene,mutation_chance,Num)
        crossed_gene=Crossover(mutant_gene,Crossover_chance,Num)
        print("Total_fitness" ,Total_fitness)
        print("Averege_fitness" ,Averege_fitness)
        highest_fitness_total = Total_fitness if Total_fitness > highest_fitness_total else highest_fitness_total
        print("highest_fitness_total=",highest_fitness_total)
        print("highest_member_total= ",sum(top_fitness_member[0]))
        if sum(top_fitness_member[0])==L:
            print("success! generations used =",gen)
            break
        p, Averege_fitness, Total_fitness = 0,0,0
        pool_gene = dict(crossed_gene)
        pool_fit = []
        parent_fit = []
        for fit in range(0,Num):
            pool_fit.append(sum (parent_gene[fit]))


def initialise_gene_pool(Num,length):
    length_in_binary = 2**length-1
    pool_gene = {}
    for i in range(0,Num) :
        random_integer = random.randint(0,length_in_binary)
        #current_fit = key_prefix2+str(i)
        pool_gene[i] = list(map(int,bin(random_integer)[2:].zfill(length)))
    return pool_gene


def find_top_fitness(pool_gene,top_fitness_member):
    pool_fit = []
    top_fitness_member_current = {}
    top_fitness_member_current[0] = 0
    for fit in range(0,len(pool_gene)):
        temp16 = sum (pool_gene[fit])
        pool_fit.append(temp16)
    for i in range(0,len(pool_gene)):
        if pool_fit[i] > sum(top_fitness_member[0]):
            top_fitness_member_current[0]=list(pool_gene[i])
            top_fitness_member[0] = list(top_fitness_member_current[0])
    if top_fitness_member_current[0] == 0:
        top_fitness_member_current[0] = list(top_fitness_member[0])
    return top_fitness_member_current


def roulette_wheel_selection(pool_gene,pool_fit,Num,Parents,Best_member):
    parent_gene = {}
    for x in range(0,Parents):
        fitness_sum = 0
        for i in range(0, len(pool_fit)):
            fitness_sum = fitness_sum + pool_fit[i]
        roulette_drop = random.randint(1,fitness_sum)
        i, fitness_sum = -1, 0
        while roulette_drop > fitness_sum:
            i = i + 1
            fitness_sum = fitness_sum + pool_fit[i]
        parent_gene[x] = list(pool_gene[i])
    parent_gene[0] = list(Best_member[0])
    return parent_gene

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
        
    
def Calculate_averege_fit(pool_fit,Size_of_population):
    Total_fitness = sum (pool_fit)
    Averege_fitness = Total_fitness/Size_of_population
    return Averege_fitness


def Mutation(parent_gene,mutation_chance,population_size):
    gene_length = 0 
    mutant_gene = {}
    for i in range(0,population_size):            
        mutating_gene = [] 
        mutating_gene = parent_gene[i]
        gene_length = len(mutating_gene)
        for x in range (0, gene_length) :
            if (random.randint(0,99) < mutation_chance):
                mutating_gene[x] = int(not mutating_gene[x])
        mutant_gene[i] = list(mutating_gene)
    return mutant_gene


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
            crossover_gene_1 = mutant_gene[r]
            s = random.choice(numbers)
            numbers.remove(s)
            crossover_gene_2 = mutant_gene[s]
            pt = random.randint(1,population_size-1)
            crossover_gene_3 = crossover_gene_1[:pt] + crossover_gene_2[pt:]
            crossover_gene_4 = crossover_gene_2[:pt] + crossover_gene_1[pt:]
            mutant_gene [r] = list(crossover_gene_3) 
            mutant_gene [s] = list(crossover_gene_4)
    return mutant_gene


main()
