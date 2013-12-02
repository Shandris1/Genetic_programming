import random
random.seed
import pprint

def main():
    global pp
    pp = pprint.PrettyPrinter(indent = 4)
    highest_fitness_total = 0
    #insert length of the gene here
    L = 50
    #insert the population size here
    Num = 50
    #insert number of parents here
    Parents = 50
    #insert number of generations here
    Overall_generations = 50
    #insert probability of mutation
    mutation_chance = 5
    #populate the array with random binary number
    pool_gene = initialise_gene_pool(Num,L)
    current_fitness_total = sum_of_fitness(pool_gene)
    pp.pprint(current_fitness_total)



    for gen in range(0,Overall_generations) :
        parents_gene = roulette_wheel_selection(pool_gene, Num, Parents)

        mutant_gene=Mutation(parents_gene, Num, L, mutation_chance)
        crossed_gene=Crossover(mutant_gene, Parents,L)
        
        pool_gene = crossed_gene
        
        pool_gene = fitness_of_members(pool_gene, Num, L)
        current_fitness_total = sum_of_fitness(pool_gene)
        pp.pprint(current_fitness_total)
        Averege_fitness = current_fitness_total/Num
        pp.pprint(Averege_fitness)
        highest_fitness_total = current_fitness_total if current_fitness_total > highest_fitness_total else highest_fitness_total
        print("highest_fitness_total=",highest_fitness_total)








def initialise_gene_pool(Num,Length):

    pool_gene = {}
    for member in range(0,Num):
        value_gene = list(range(Length))
        value_member = {}
        for gene in range(0,Length):
            value_gene[gene] = random.randint(0,1)
        value_fitness = sum(value_gene)
        value_member["genes"] = value_gene
        value_member["fitness"] = value_fitness
        pool_gene[member] = value_member
    return pool_gene





def roulette_wheel_selection(pool_gene, gene_size, parents_number):
    parents_gene = {}
    current_fitness_total = sum_of_fitness(pool_gene)
    for parent in range(0,parents_number):
        cutoff = random.randint(0,current_fitness_total)
        fitness_sum = 0 #resets the fitness counter
        for member in range(0,gene_size):
            fitness_sum = fitness_sum + pool_gene[member]["fitness"] #increases the fitness counter by the current members fitness
            if fitness_sum >= cutoff: 
                parents_gene[parent] = pool_gene[member]
                break
    return parents_gene
        
    
def Calculate_averege_fit(pool_fit,Size_of_population):
    Total_fitness = sum (pool_fit)
    Averege_fitness = Total_fitness/Size_of_population
    return Averege_fitness

def Mutation(parents_gene,gene_size,length_of_gene,mutation_rate):
    mutated_gene = {}

    for member in range(0,gene_size):
        mutated_gene_list = list(range(length_of_gene))
        for x in range (0,length_of_gene):
            if (random.randint(0,99) < mutation_rate): #random.random returns a float between 0 and 1
                mutated_gene_list[x] = parents_gene[member]["genes"][x] ^ 1 #inverts the gene
            else:
                mutated_gene_list[x] = parents_gene[member]["genes"][x] #leaves gene the same
        mutated_gene[member] = {"genes":mutated_gene_list}
    return mutated_gene


def Crossover(mutant_gene,  parents_number, gene_length):
    children_gene = {}

    for member in range(0, parents_number,2):
        gene1 = mutant_gene[member]["genes"]
        gene2 = mutant_gene[member + 1]["genes"]


        crossover_point = random.randint(1,gene_length-1)

        gene3 = gene1[:crossover_point] + gene2[crossover_point:]
        gene4 = gene2[:crossover_point] + gene1[crossover_point:]

        children_gene[member] = {"genes":gene3}
        children_gene[member + 1] = {"genes":gene4}

    return children_gene

def fitness_of_members(pool_gene, pool_size, gene_length):
    for member in range(0,pool_size):
        pool_gene[member]["fitness"] = sum(pool_gene[member]["genes"])
    return pool_gene


def sum_of_fitness(pool_gene):
    current_total = 0
    for member, value in pool_gene.items():
        current_total = current_total + pool_gene[member]["fitness"]
    return current_total

main()
