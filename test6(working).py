import random
random.seed

def main():


    pool_gene = {}
    pool_fit = []
    parent_gene = {}
    mutant_gene = {}
    crossed_gene = {}
    parent_fit = []
    p = 0
    Total_fitness = 0
    #insert length of the gene here
    L = 5
    #insert the population size here
    Num = 5
    #insert number of parents here
    Parents = 5
    #insert number of generations here
    Overall_generations = 5
    #insert probability of crossover
    Crossover_chance = 10
    #insert probability of mutation
    mutation_chance = 10
    
    Lr = 2**L-1 #length of gene in binary
    key_prefix = "person_"
    #key_prefix2="fit_"

    #populate the array with random binary number
    for i in range(0,Num) :
        A = random.randint(0,Lr)
        current_member = key_prefix + str(i)
        #current_fit = key_prefix2+str(i)
        pool_gene[current_member] = convert_to_boolean_array (A,L)
        temp15 = sum (pool_gene[current_member])
        pool_fit.append(temp15)
        print ('this parent\'s fitness = ',pool_fit[i])
    
    #stating overall fitness
    Total_fitness = sum(pool_fit)
    print ('original fitness = ',Total_fitness)
    #stating averege fitness
    Averege_fitness = Calculate_averege_fit (pool_fit, Num)
    print ('original averege fitness = ',Averege_fitness)
    print("pool_fit",pool_fit)
    
    for gen in range(0,Overall_generations) :

        print('start combo ',pool_gene)
        while p < Parents:
            parent_gene[key_prefix + str(p)] = roulette_wheel_selection(pool_gene,pool_fit,Num)
            current_parent = key_prefix + str(p)
            temp16 = sum (parent_gene[current_parent])
            parent_fit.append(temp16)
            p=p+1
        Total_fitness = sum(parent_fit)
        print ('child fitness = ',Total_fitness)

        Averege_fitness = Calculate_averege_fit (parent_fit, Num)
        print ('child averege fitness = ',Averege_fitness)
        
        print("parent_geneb4",parent_gene)
        mutant_gene=Mutation(parent_gene,mutation_chance,Num)
        print("parent_geneam",mutant_gene)
        crossed_gene=Crossover(mutant_gene,Crossover_chance,Num)
        print("parent_geneat",crossed_gene)
        
        p=0
        Averege_fitness=0
        Total_fitness=0
        pool_gene=crossed_gene
        print("pool_gene=",pool_gene)
        pool_fit=[]
        parent_fit=[]
        for fit in range(0,Num):
            current_parent = key_prefix + str(fit)
            temp16 = sum (parent_gene[current_parent])
            pool_fit.append(temp16)






def convert_to_boolean_array(rand_num,length):
    return list(map(int,bin(rand_num)[2:].zfill(length)))


def roulette_wheel_selection(pool_gene,pool_fit,Num):
    fitness_sum = 0
    key_prefix="person_"
    chosen_parent=[]
    for i in range(0, len(pool_fit)):
        fitness_sum = fitness_sum + pool_fit[i]
    roulette_drop = random.randint(1,fitness_sum)
    i, fitness_sum = -1, 0
    while roulette_drop > fitness_sum:
        i=i+1
        fitness_sum = fitness_sum + pool_fit[i]
    chosen_parent = pool_gene[key_prefix+str(i)]
    return chosen_parent
        
    
def Calculate_averege_fit(pool_fit,Size_of_population):
    Total_fitness = sum (pool_fit)
    Averege_fitness = Total_fitness/Size_of_population
    return Averege_fitness

def Mutation(parent_gene,mutation_chance,population_size):
   
    gene_length = 0
    key_prefix="person_" 
    mutant_gene=dict()

    for i in range(0,population_size):
        current_mutant = key_prefix+str(i)            
   
        mutating_gene = [] 
        mutating_gene = parent_gene[key_prefix+str(i)]
        print("mutating_gene",mutating_gene)
        gene_length = len(mutating_gene)
        # print (mutating_gene)
        for x in range (0, gene_length) :
            if (random.randint(0,99) < mutation_chance):
                mutating_gene[x]= int(not mutating_gene[x])
                print("trigger")
        mutant_gene[current_mutant]=mutating_gene
        print("mutating_gene",mutating_gene)
    return mutant_gene

    


def Crossover(mutant_gene,Crossover_chance,population_size):
    key_prefix="person_"

    #gene_length = len(mutant_gene)
    for x in range (1,population_size):
        if(random.randint(0,99)<Crossover_chance):#replace 100 with Crossover_chance
            numbers = list(map(int,range(1,population_size)))
            numbers.remove(x)
            r = random.choice(numbers)
            crossover_gene_1 = mutant_gene[key_prefix+str(r)]
            numbers.remove(r)
            s = random.choice(numbers)
            crossover_gene_2 = mutant_gene[key_prefix+str(s)]
            pt= random.randint(1,population_size-1)
            crossover_gene_3 = crossover_gene_1[:pt] + crossover_gene_2[pt:]
            crossover_gene_4 = crossover_gene_2[:pt] + crossover_gene_1[pt:]
            mutant_gene [key_prefix+str(r)] = crossover_gene_3 
            mutant_gene [key_prefix+str(s)] = crossover_gene_4
    return mutant_gene

main()
    
