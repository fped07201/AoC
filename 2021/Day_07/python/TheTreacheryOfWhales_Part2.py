with open("../input.txt",'r') as fd:
    h_pos = [int(x) for x in fd.read().split(',')]
    h_pos_max = max(h_pos)
    h_pos_min = min(h_pos)

    min_fuel=None
    min_pos=None
    for i in range(h_pos_min, h_pos_max+1):
        fuel = sum([sum(list(range(abs(x-i)+1))) for x in h_pos])
        if min_fuel is None or fuel<min_fuel:
            min_fuel=fuel
            min_pos=i

    print("Min fuel %d in position %d"%(min_fuel,min_pos))
