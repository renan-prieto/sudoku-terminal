# sudoku
from random import shuffle
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ]
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]

def mount_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = ((i * 3 + i // 3 + j) % 9) + 1
    numbers = list(range(1, 10))
    shuffle(numbers)
    for i in range(9):
        for j in range(9):
            board[i][j] = numbers[board[i][j] - 1]
            
    return board


def show_board():
    print("  ", *ALPHABET[0:3]," ", *ALPHABET[3:6:], " ", *ALPHABET[6:9:] )
    for i in range(0, 9):
        print( NUMBERS[i], "", *sudoku_board[i][0:3], "║", *sudoku_board[i][3:6], "║",  *sudoku_board[i][6:9])
        if i == 2 or i == 5:
            # ╬ ═
            print(f"   {6*'═'}╬{7*'═'}╬{6*'═'}" )

sudoku_board = mount_board()
show_board()
