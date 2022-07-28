def AppendHeight(h_list,i,j,h):
    h_list.append({'row':i,'col':j,'height':h})

def FindLowestPoints(in_data):
    n_rows = len(in_data)
    n_cols = len(in_data[0])
    lowest = []

    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0:
                if j == 0:
                    if (in_data[i][j] < in_data[i+1][j]) and (in_data[i][j] < in_data[i][j+1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
                elif j == (n_cols-1):
                    if (in_data[i][j] < in_data[i+1][j]) and (in_data[i][j] < in_data[i][j-1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
                else:
                    if (in_data[i][j] < in_data[i+1][j]) and (in_data[i][j] < in_data[i][j-1]) and (in_data[i][j] < in_data[i][j+1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
            elif i == (n_rows-1):
                if j == 0:
                    if (in_data[i][j] < in_data[i-1][j]) and (in_data[i][j] < in_data[i][j+1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
                elif j == (n_cols-1):
                    if (in_data[i][j] < in_data[i-1][j]) and (in_data[i][j] < in_data[i][j-1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
                else:
                    if (in_data[i][j] < in_data[i-1][j]) and (in_data[i][j] < in_data[i][j-1]) and (in_data[i][j] < in_data[i][j+1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
            else:
                if j == 0:
                    if (in_data[i][j] < in_data[i-1][j]) and (in_data[i][j] < in_data[i+1][j]) and (in_data[i][j] < in_data[i][j+1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
                elif j == (n_cols-1):
                    if (in_data[i][j] < in_data[i-1][j]) and (in_data[i][j] < in_data[i+1][j]) and (in_data[i][j] < in_data[i][j-1]):
                        AppendHeight(lowest,i,j,in_data[i][j])
                else:
                    if (in_data[i][j] < in_data[i-1][j]) and (in_data[i][j] < in_data[i+1][j]) and (in_data[i][j] < in_data[i][j-1]) and (in_data[i][j] < in_data[i][j+1]):
                        AppendHeight(lowest,i,j,in_data[i][j])

    return lowest

def GetNewBasinPoints(point, basin, in_data):
    n_rows = len(in_data)
    n_cols = len(in_data[0])
    candidates=[]

    if point['row'] == 0:
        if point['col'] == 0:
            candidates.append({'row':point['row']+1,'col':point['col']  ,'height':data[point['row']+1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']+1,'height':data[point['row']][point['col']+1]})
        elif point['col'] == (n_cols-1):
            candidates.append({'row':point['row']+1,'col':point['col']  ,'height':data[point['row']+1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']-1,'height':data[point['row']][point['col']-1]})
        else:
            candidates.append({'row':point['row']+1,'col':point['col']  ,'height':data[point['row']+1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']+1,'height':data[point['row']][point['col']+1]})
            candidates.append({'row':point['row'],  'col':point['col']-1,'height':data[point['row']][point['col']-1]})
    elif point['row'] == (n_rows-1):
        if point['col'] == 0:
            candidates.append({'row':point['row']-1,'col':point['col']  ,'height':data[point['row']-1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']+1,'height':data[point['row']][point['col']+1]})
        elif point['col'] == (n_cols-1):
            candidates.append({'row':point['row']-1,'col':point['col']  ,'height':data[point['row']-1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']-1,'height':data[point['row']][point['col']-1]})
        else:
            candidates.append({'row':point['row']-1,'col':point['col']  ,'height':data[point['row']-1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']+1,'height':data[point['row']][point['col']+1]})
            candidates.append({'row':point['row'],  'col':point['col']-1,'height':data[point['row']][point['col']-1]})
    else:
        if point['col'] == 0:
            candidates.append({'row':point['row']-1,'col':point['col']  ,'height':data[point['row']-1][point['col']]})
            candidates.append({'row':point['row']+1,'col':point['col']  ,'height':data[point['row']+1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']+1,'height':data[point['row']][point['col']+1]})
        elif point['col'] == (n_cols-1):
            candidates.append({'row':point['row']-1,'col':point['col']  ,'height':data[point['row']-1][point['col']]})
            candidates.append({'row':point['row']+1,'col':point['col']  ,'height':data[point['row']+1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']-1,'height':data[point['row']][point['col']-1]})
        else:
            candidates.append({'row':point['row']-1,'col':point['col']  ,'height':data[point['row']-1][point['col']]})
            candidates.append({'row':point['row']+1,'col':point['col']  ,'height':data[point['row']+1][point['col']]})
            candidates.append({'row':point['row'],  'col':point['col']+1,'height':data[point['row']][point['col']+1]})
            candidates.append({'row':point['row'],  'col':point['col']-1,'height':data[point['row']][point['col']-1]})
    return [x for x in candidates if int(x['height'])<9 if x not in basin]



def FindBasin(low_point, in_data):
    basin=[]
    basin.append(low_point)

    proposed_points = GetNewBasinPoints(low_point, basin, in_data)
    basin.extend(proposed_points)

    while len(proposed_points)>0:
        proposed_points = []
        for point in basin:
            new_points = GetNewBasinPoints(point, basin, in_data)
            proposed_points.extend([x for x in new_points if x not in proposed_points])
        basin.extend(proposed_points)

    return basin


with open("../input.txt", 'r') as fd:
    data = fd.read().split('\n')
    basins=[]

    low_points = FindLowestPoints(data)

    for point in low_points:
        basins.append(FindBasin(point, data))

    lens = [len(x) for x in basins]
    lens.sort(reverse=True)
    result = lens[0]*lens[1]*lens[2]

    print(result)

