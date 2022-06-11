def AppendHeight(h_list,i,j,h):
    h_list.append({'row':i,'col':j,'height':h})

# with open("../input.txt", 'r') as fd:
with open("test_data.txt", 'r') as fd:
    data = fd.read().split('\n')
    n_rows = len(data)
    n_cols = len(data[0])
    low_points = []

    print(n_cols)
    print(n_rows)

    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0:
                if j == 0:
                    if (data[i][j] < data[i+1][j]) and (data[i][j] < data[i][j+1]):
                        AppendHeight(low_points,i,j,data[i][j])
                elif j == (n_cols-1):
                    if (data[i][j] < data[i+1][j]) and (data[i][j] < data[i][j-1]):
                        AppendHeight(low_points,i,j,data[i][j])
                else:
                    if (data[i][j] < data[i+1][j]) and (data[i][j] < data[i][j-1]) and (data[i][j] < data[i][j+1]):
                        AppendHeight(low_points,i,j,data[i][j])
            elif i == (n_rows-1):
                if j == 0:
                    if (data[i][j] < data[i-1][j]) and (data[i][j] < data[i][j+1]):
                        AppendHeight(low_points,i,j,data[i][j])
                elif j == (n_cols-1):
                    if (data[i][j] < data[i-1][j]) and (data[i][j] < data[i][j-1]):
                        AppendHeight(low_points,i,j,data[i][j])
                else:
                    if (data[i][j] < data[i-1][j]) and (data[i][j] < data[i][j-1]) and (data[i][j] < data[i][j+1]):
                        AppendHeight(low_points,i,j,data[i][j])
            else:
                if j == 0:
                    if (data[i][j] < data[i-1][j]) and (data[i][j] < data[i+1][j]) and (data[i][j] < data[i][j+1]):
                        AppendHeight(low_points,i,j,data[i][j])
                elif j == (n_cols-1):
                    if (data[i][j] < data[i-1][j]) and (data[i][j] < data[i+1][j]) and (data[i][j] < data[i][j-1]):
                        AppendHeight(low_points,i,j,data[i][j])
                else:
                    if (data[i][j] < data[i-1][j]) and (data[i][j] < data[i+1][j]) and (data[i][j] < data[i][j-1]) and (data[i][j] < data[i][j+1]):
                        AppendHeight(low_points,i,j,data[i][j])

    risk_level = sum([int(x['height'])+1 for x in low_points])

    print("Risk level is %d"%risk_level)