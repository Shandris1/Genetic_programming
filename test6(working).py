import random
random.seed
p = 0

def main():
    pool_gene={}
    pool_fit=[]
    parent_gene={}
    parent_fit=[]
    offspring_gene={}
    global p
    p = 0
    Total_fitness = 0
    #insert length of the gene here
    L = 10
    #insert the population size here
    Num = 10
    #insert number of parents here
    Parents = 10
    #insert number of generations here
    Overall_generations= 5
    #insert probability of crossover
    Crossover_chance=10
    #insert probability of mutation
    mutation_chance=10
    

    Lr = 2**L-1 #length of gene in binary
    key_prefix="person_"
    #key_prefix2="fit_"

    
    #populate the array with random binary number
    for i in range(0,Num) :
        A= random.randint(0,Lr)
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
    print('firstish combo',pool_gene)
    

    for gen in range(0,Overall_generations) :

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
        print('starting combo',parent_gene)
        for i in range(0,Parents):
            current_mutant = key_prefix+str(i)
            offspring_gene[current_mutant] = Mutation(parent_gene,mutation_chance,i)
        print('final combo',offspring_gene)
        Crossover(offspring_gene,Crossover_chance,Num)
        p=0
        Averege_fitness=0
        Total_fitness=0
        pool_gene=offspring_gene
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
    global p
    for i in range(0, len(pool_fit)):
        fitness_sum = fitness_sum + pool_fit[i]
    roulette_drop = random.randint(0,fitness_sum)
    i, fitness_sum = -1, 0
    while roulette_drop > fitness_sum:
        i=i+1
        fitness_sum = fitness_sum + pool_fit[i]
    if (i==-1):
        i=i+1
    chosen_parent = pool_gene [key_prefix+str(i)]
    return chosen_parent
        
    
def Calculate_averege_fit(pool_fit,Size_of_population):
    Total_fitness = sum (pool_fit)
    Averege_fitness = Total_fitness/Size_of_population
    return Averege_fitness

def Mutation(parent_gene,mutation_chance,current_member):
    
   key_prefix="person_"
   gene_length = 0
   mutating_gene = [] 
   mutating_gene = parent_gene [key_prefix+str(current_member)]
   
  # print (mutating_gene)
   gene_length = len(mutating_gene)
   for x in range (0, gene_length) :
     if random.randint(0,100) < mutation_chance:
        mutating_gene [x]= int(not mutating_gene [x])
  # mutating_gene = 
   return mutating_gene 
    


def Crossover(parent_gene,Crossover_chance,population_size):
   key_prefix="person_"
   #gene_length = len(parent_gene)
   for x in range (1,population_size):
        if(random.randint(0,100)<100):#replace 100 with Crossover_chance
            numbers = list(map(int,range(1,population_size)))
            numbers.remove(x)
            r = random.choice(numbers)
            crossover_gene_1 = parent_gene [key_prefix+str(r)]
            numbers.remove(r)
            s = random.choice(numbers)
            crossover_gene_2 = parent_gene [key_prefix+str(s)]
            pt= random.randint(1,7)
            crossover_gene_3 = crossover_gene_1[:pt] + crossover_gene_2[pt:]
            crossover_gene_4 = crossover_gene_2[:pt] + crossover_gene_1[pt:]
            parent_gene [key_prefix+str(r)] = crossover_gene_3 
            parent_gene [key_prefix+str(s)] = crossover_gene_4

main()
    
