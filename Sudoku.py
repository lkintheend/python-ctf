from socket import socket


def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def procesInput(input):
    lines = str(input).splitlines()[0:9]
    result = []
    for line in lines:
        row = []
        for x in range(9):
            if line[x * 2] == '_':
                row.append(0)
            else:
                row.append(int(line[x * 2]))
        result.append(row)

    return result


def revertResult(result):
    str_result = ''
    for row in result:
        for x in row:
            str_result += str(x) + " "
        str_result = str_result[0:-1] + "\n"
    print str_result
    return str_result


sock = socket()
sock.connect(('188.166.218.1', 2015))
data = sock.recv(10240)
data = sock.recv(10240)
data = sock.recv(10240)
# print data
input = procesInput(data)
# print input
solveSudoku(input)
str_result = revertResult(input)
# print str_result
sock.send((str_result).encode())

while True:
    data = sock.recv(10240)
    print(data + '1')
    data = sock.recv(10240)
    print(data + '2')
    data = sock.recv(10240)
    print(data + '3')
    temp = procesInput(data)
    # print temp
    solveSudoku(temp)
    str_result = revertResult(temp)
    sock.send(str_result.encode())
