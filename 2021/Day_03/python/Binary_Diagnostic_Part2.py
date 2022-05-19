
with open("../input.txt",'r') as fd:
    lines = [list(map(int,list(x))) for x in fd.read().splitlines()]

    remaining_oxygen = lines
    for i in range(len(lines[0])):
        num_ones = sum([x[i] for x in remaining_oxygen])
        dominant = 1 if (num_ones >= (len(remaining_oxygen) - num_ones)) else 0
        remaining_oxygen = [x for x in remaining_oxygen if x[i] == dominant]
        if len(remaining_oxygen) == 1:
            remaining_oxygen = [str(x) for x in remaining_oxygen[0]]
            break

    remaining_co2 = lines
    for i in range(len(lines[0])):
        num_ones = sum([x[i] for x in remaining_co2])
        dominant = 1 if (num_ones >= (len(remaining_co2) - num_ones)) else 0
        remaining_co2 = [x for x in remaining_co2 if x[i] != dominant]
        if len(remaining_co2) == 1:
            remaining_co2 = [str(x) for x in remaining_co2[0]]
            break

    remaining_oxygen = int(''.join(remaining_oxygen),2)
    remaining_co2    = int(''.join(remaining_co2),2)

    print("Oxygen: %d"%remaining_oxygen)
    print("CO2: %d"%remaining_co2)

    life_support = remaining_oxygen*remaining_co2
    print("Life support: %d"%life_support)
