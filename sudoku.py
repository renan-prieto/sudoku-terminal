# sudoku
from random import shuffle, randint

# constants
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ]
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]
BOARD_SIZE = 81
# numero de dicas retiradas
EASY = 20
MEDIUM = 35
HARD = 45
EXTREME = 54
IMPOSSIBLE = 64

# functions
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

def remove_tips(diff, board):
    count = 0
    while True:
        for i in range(9):
            for j in range(9):
                if count >= diff: 
                    break
                removed_tip = randint(0, BOARD_SIZE)
                if removed_tip < diff:
                    board[i][j] = '_'
                    count += 1
        if count >= diff: 
            break
    print(count)

def show_board():
    print("  ", *ALPHABET[0:3]," ", *ALPHABET[3:6:], " ", *ALPHABET[6:9:] )
    for i in range(0, 9):
        print( NUMBERS[i], "", *sudoku_board[i][0:3], "║", *sudoku_board[i][3:6], "║",  *sudoku_board[i][6:9])
        if i == 2 or i == 5:
            # ╬ ═
            print(f"   {6*'═'}╬{7*'═'}╬{6*'═'}" )


sudoku_board = mount_board()
remove_tips(EASY, sudoku_board)
show_board()
