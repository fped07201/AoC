horizontal = 0
depth = 0

map_keys = ["cmd","number"]

with open("../input.txt",'r') as fd:
    # lines = [line.split() for line in fd.read().splitlines()]

    lines = [dict(zip(map_keys, line.split())) for line in fd.read().splitlines()]
    
    for line in lines:
        if line["cmd"] == "forward":
            horizontal = horizontal + int(line["number"])
        elif line["cmd"] == "down":
            depth = depth + int(line["number"])
        elif line["cmd"] == "up":
            depth = depth - int(line["number"])
        else:
            print("Unknown command")
        
    print("Horizontal: %d, Depth: %d"%(horizontal, depth))
    print("Horizontal * Depth: %d"%(horizontal*depth))