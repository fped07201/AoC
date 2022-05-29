days=80
with open("../input.txt",'r') as fd:
    population = [int(x) for x in fd.read().split(',')]

    for day in range(1,days+1):
        for i in range(len(population)):
            if population[i]==0:
                population.append(8)
                population[i] = 6
            else:
                 population[i]= population[i]-1

    print("After %d days, there are %d lanternfish"%(day, len(population)))
    