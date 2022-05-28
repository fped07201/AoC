def MarkNumber(num, board_list):
    for board in board_list:
        # Remove num from board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == num:
                    board[i][j] = None

def CheckWinnerRow(num, board_list):
    for board in board_list:
        # Detect row winner
        for i in range(len(board)):
            if all([x==None for x in board[i]]):
                return board_list.index(board)
    return None

def CheckWinnerCol(num, board_list):          
    for board in board_list:
        # Detect col winner
        for j in range(len(board[0])):
            col = []
            for i in range(len(board)):
                col.append(board[i][j])
            if all([x==None for x in col]):
                return board_list.index(board)
    return None

def CheckWinner(num, board_list):
    winner_row = CheckWinnerRow(num, board_list)
    return winner_row if winner_row!= None else CheckWinnerCol(num, board_list)

def SumUnmarked(board):
    summa = 0
    for i in range(len(board)):
        summa = summa + sum([x for x in board[i] if x!= None])
    return summa

with open("../input.txt",'r') as fd:
    lines = fd.read().splitlines()
    if lines[-1] != '':
        lines.append('')

    separators = []
    [separators.append(i) for i in range(len(lines)) if lines[i] == '']

    draw = [int(x) for x in lines[separators[0]-1].split(',')]

    boards = []
    for i in range(len(separators)-1):
        board_data = [data.split() for data in lines[separators[i]+1:separators[i+1]]]
        board_data = [list(map(int, data.split())) for data in lines[separators[i]+1:separators[i+1]]] 
        boards.append(board_data)

    for num in draw:
        MarkNumber(num, boards)
        winner = CheckWinner(num, boards)
        if winner != None:
            summa = SumUnmarked(boards[winner])
            result = summa * num
            print("Result is %d (%d * %d)"%(result, num, summa))
            break