x = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""
y = x.split()

def sudboard(board):


    for row in range(len(board)):
        rsum = 0
        for strnum in range(len(board)):
            rsum += int(board[row][strnum])
        if rsum == 45:
            continue
        else:
            msgfalse = "The board IS NOT a valid Sudoku board."
            return msgfalse

    for col in range(len(board)):
        csum = 0
        for strnum in range(len(board)):
            csum += int(board[strnum][col])
        if csum == 45:
            continue
        else:
            msgfalse = "The board IS NOT a valid Sudoku board."
            return msgfalse

    for prerow in range(0,9,3):
        for precol in range(0,9,3):
            tsum = 0

            for row in range(prerow, prerow+3): # row takes prerow values 0-3,3-6,6-9
                for col in range(precol, precol+3): # col takes precol values 0-3,3-6,6-9
                    tsum += int(board[row][col])
            if tsum == 45:
                continue
            else:
                msgfalse = "The board IS NOT a valid Sudoku board."
                return msgfalse


    msgtrue = "The board IS a valid Sudoku board."
    return msgtrue


print(sudboard(y))