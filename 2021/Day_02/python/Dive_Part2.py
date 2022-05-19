horizontal = 0
depth = 0
aim = 0

map_keys = ["cmd","number"]

with open("../input.txt",'r') as fd:
    # lines = [line.split() for line in fd.read().splitlines()]

    lines = [dict(zip(map_keys, line.split())) for line in fd.read().splitlines()]
    
    for line in lines:
        if line["cmd"] == "forward":
            horizontal = horizontal + int(line["number"])
            depth = depth + aim*int(line["number"])
        elif line["cmd"] == "down":
            aim = aim + int(line["number"])
        elif line["cmd"] == "up":
            aim = aim - int(line["number"])
        else:
            print("Unknown command")
        
    print("Horizontal: %d, Depth: %d, Aim: %d"%(horizontal, depth, aim))
    print("Horizontal * Depth: %d"%(horizontal*depth))