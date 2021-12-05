from random import randint, choice

board = [[(randint(10, 20), choice([True, False])) for j in range(5)] for i in range(5)]

for row in board:
    print(row)

win = any(all(board[j][i][1] for j in range(5)) for i in range(5))

print(win)
