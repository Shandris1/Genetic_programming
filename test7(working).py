import random
random.seed

def main():

    
    pool_fit = []
    parent_fit = []
    highest_fitness_total = 0
    p = 0
    Total_fitness = 0
    #insert length of the gene here
    L = 50
    #insert the population size here
    Num = 50
    #insert number of parents here
    Parents = 50
    #insert number of generations here
    Overall_generations = 50
    #insert probability of crossover
    Crossover_chance = 80
    #insert probability of mutation
    mutation_chance = 1
    #populate the array with random binary number
    pool_gene = initialise_gene_pool(Num,L)
    for i in range(0,Num) :
        temp15 = sum (pool_gene[i])
        pool_fit.append(temp15)
        print ('this parent\'s fitness = ',pool_fit[i])
    Total_fitness = sum(pool_fit)
    Averege_fitness = Calculate_averege_fit (pool_fit, Num)

    print("Total_fitness" ,Total_fitness)
    print("Averege_fitness" ,Averege_fitness)

    for gen in range(0,Overall_generations) :
        parent_gene = roulette_wheel_selection(pool_gene,pool_fit,Num,Parents)
        while p < Parents:
            temp16 = sum (parent_gene[p])
            parent_fit.append(temp16)
            p=p+1
        Total_fitness = sum(parent_fit)
        Averege_fitness = Calculate_averege_fit (parent_fit, Num)
        mutant_gene=Mutation(parent_gene,mutation_chance,Num)
        crossed_gene=Crossover(mutant_gene,Crossover_chance,Num)
        
        print("Total_fitness" ,Total_fitness)
        print("Averege_fitness" ,Averege_fitness)
        highest_fitness_total = Total_fitness if Total_fitness > highest_fitness_total else highest_fitness_total
        print("highest_fitness_total=",highest_fitness_total)
        p = 0
        Averege_fitness = 0
        Total_fitness = 0
        pool_gene = crossed_gene
        pool_fit = []
        parent_fit = []
        for fit in range(0,Num):
            temp16 = sum (parent_gene[fit])
            pool_fit.append(temp16)





def initialise_gene_pool(Num,length):
    length_in_binary = 2**length-1
    pool_gene = {}

    for i in range(0,Num) :
        random_integer = random.randint(0,length_in_binary)
        #current_fit = key_prefix2+str(i)
        pool_gene[i] = list(map(int,bin(random_integer)[2:].zfill(length)))
    return pool_gene
    """
def initialise_gene_pool(pool_size = 2, gene_length = 2):
    pool_gene = {}
    for member in range(0,pool_size):
        value_gene = list(range(gene_length))
        for gene in range(0,gene_length):
            value_gene[gene] = random.randint(0,1)
        pool_gene[member] = value_gene
    return pool_gene"""





def roulette_wheel_selection(pool_gene,pool_fit,Num,Parents):
    
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
        # print (mutating_gene)
        for x in range (0, gene_length) :
            if (random.randint(0,99) < mutation_chance):
                mutating_gene[x] = int(not mutating_gene[x])
        mutant_gene[i] = list(mutating_gene)
    return mutant_gene


def Crossover(mutant_gene,Crossover_chance,population_size):


    #gene_length = len(mutant_gene)
    for x in range (1,population_size):
        if(random.randint(0,99)<Crossover_chance):#replace 100 with Crossover_chance
            numbers = list(map(int,range(1,population_size)))
            numbers.remove(x)
            r = random.choice(numbers)
            crossover_gene_1 = mutant_gene[r]
            numbers.remove(r)
            s = random.choice(numbers)
            crossover_gene_2 = mutant_gene[s]
            pt = random.randint(1,population_size-1)
            crossover_gene_3 = crossover_gene_1[:pt] + crossover_gene_2[pt:]
            crossover_gene_4 = crossover_gene_2[:pt] + crossover_gene_1[pt:]
            mutant_gene [r] = list(crossover_gene_3) 
            mutant_gene [s] = list(crossover_gene_4)
    return mutant_gene

main()
