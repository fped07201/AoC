from collections import Counter

def InputToDict(lines):
    data=[]
    for line in lines:
        aux_dict={}
        aux_dict["x1"]=int(line.split()[0].split(',')[0])
        aux_dict["y1"]=int(line.split()[0].split(',')[1])
        aux_dict["x2"]=int(line.split()[2].split(',')[0])
        aux_dict["y2"]=int(line.split()[2].split(',')[1])
        data.append(aux_dict)
    return data

def FilterHorizontalVertical(data):
    return [coor for coor in data if (coor["x1"]==coor["x2"] or coor["y1"]==coor["y2"])]

def ExpandData(data):
    out_data=[]
    for coor in data:
        if coor["x1"]==coor["x2"]:
            for val in [[coor["x1"], y] for y in range(min(coor["y1"],coor["y2"]), max(coor["y1"],coor["y2"])+1)]:
                out_data.append(val)
        elif coor["y1"]==coor["y2"]:
            for val in [[x,coor["y1"]] for x in range(min(coor["x1"],coor["x2"]), max(coor["x1"],coor["x2"])+1)]:
                out_data.append(val)
        else:
            print("Neither horizontal nor vertical line")
    return out_data

def OverlappedPoints(data):
    counter_data = Counter(tuple(x) for x in expanded_data)
    cnt=0
    for x in counter_data:
        if counter_data[x]>1:
            cnt=cnt+1
    return cnt

with open("../input.txt",'r') as fd:
    lines = fd.read().splitlines()
    
    data = InputToDict(lines)
    filtered_data = FilterHorizontalVertical(data)
    expanded_data = ExpandData(filtered_data)
    counter_data = Counter(tuple(x) for x in expanded_data)
    overlapped_points = OverlappedPoints(counter_data)

    print("Number of overlapped points:%d"%overlapped_points)