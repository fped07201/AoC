gamma_rate = []
epsilon_rate = []

with open("../input.txt",'r') as fd:
    lines = [list(map(int,list(x))) for x in fd.read().splitlines()]

    for i in range(len(lines[0])):
        num_ones = sum([x[i] for x in lines])
        gamma_rate.append('1' if (num_ones > (len(lines) - num_ones)) else '0')
        epsilon_rate.append('0' if (num_ones > (len(lines) - num_ones)) else '1')

    gamma_rate   = int(''.join(gamma_rate),2)
    epsilon_rate = int(''.join(epsilon_rate),2)

    print("Gamma rate: %d"%gamma_rate)
    print("Epsilon rate: %d"%epsilon_rate)

    power_consumption = gamma_rate*epsilon_rate
    print("Power consumption: %d"%power_consumption)
