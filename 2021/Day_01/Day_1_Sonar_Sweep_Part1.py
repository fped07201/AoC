counter=0

with open("input.txt",'r') as fd:
    lines = fd.readlines()
    previous_data=int(lines[0])

    for line in lines[1:]:
        if int(line) > previous_data:
            counter = counter + 1

        previous_data = int(line)

    print("%d measurements are larger than previous measurements." % (counter))