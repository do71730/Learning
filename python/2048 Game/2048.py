import random as r
def main():
    num = [2,4]
    size = 4
    board = [[0 for i in range(size)] for j in range(size)] 
    while any(0 in x for x in board ):
        x = r.randint(0,3)
        y = r.randint(0,3)
        v = r.randint(0,1)
        board[x][y] = num[v]
        print(board)

if __name__ == '__main__':
    main()