counter=0

with open("../input.txt",'r') as fd:
    lines = [int(line) for line in fd.read().splitlines()]
    average_list = [(lines[i-2] + lines[i-1] + lines[i]) for i in range(2,len(lines))]
    previous_data=average_list[0]

    for val in average_list[1:]:
        if val > previous_data:
            counter = counter + 1

        previous_data = val

    print("%d measurements are larger than previous measurements." % (counter))