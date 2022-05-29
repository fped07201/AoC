days=256
with open("../input.txt",'r') as fd:
    population = [int(x) for x in fd.read().split(',')]

    population_dict={}
    for i in range(9):
        population_dict[i]=0

    for i in range(len(population)):
        if population[i] in population_dict.keys():
            population_dict[population[i]] = population_dict[population[i]]+1

    for day in range(1,days+1):
        population_zeroes=population_dict[0]
        for i in range(8):
            population_dict[i]=population_dict[i+1]
        population_dict[6]=population_dict[6]+population_zeroes
        population_dict[8]=population_zeroes

    print("After %d days, there are %d lanternfish"%(day, sum([population_dict[i] for i in population_dict.keys()])))
    