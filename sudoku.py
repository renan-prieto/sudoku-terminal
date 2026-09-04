# sudoku
from random import shuffle, randint
import copy
import os
import platform
from time import sleep
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

def remove_tips(diff, copy_board):
    count = 0
    while True:
        for i in range(9):
            for j in range(9):
                if count >= diff: 
                    break
                removed_tip = randint(0, BOARD_SIZE-1)
                if removed_tip < diff:
                    copy_board[i][j] = '_'
                    count += 1
        if count >= diff: 
            break
    return copy_board

def show_board(board):
    print("  ", *ALPHABET[0:3]," ", *ALPHABET[3:6:], " ", *ALPHABET[6:9:] )
    for i in range(0, 9):
        print( NUMBERS[i], "", *board[i][0:3], "║", *board[i][3:6], "║",  *board[i][6:9])
        if i == 2 or i == 5:
            # ╬ ═
            print(f"   {6*'═'}╬{7*'═'}╬{6*'═'}" )

def append_value(letter, number, value, board):
    msg = ""
    if copy_board[number][letter] != '_':
        msg = "IMPOSSIVEL COLOCAR AI MANO"
    elif value == board[number][letter]:
        msg = "PARABENS MANO"
        copy_board[number][letter] = value
    else:
        msg = "VALOR ERRADO"
    return msg, copy_board

def inserting_data(board):
    print("exemplo de inserção: A1 1")
    value_and_cord = input('>').upper()
    
    letter_string = value_and_cord[0:1]
    letter_number = ALPHABET.index(letter_string)
    number = int(value_and_cord[1:2])-1

    value  = int(value_and_cord[3:4])
    
    msg, copy_board = append_value(letter_number, number, value, board)
    
    return msg, copy_board

def menu():
    while True:
        clear_screen()
        print("Olá, jogador! Escolha uma dificuldade")
        print("(E)ASY | (M)EDIUM | (H)ARD | (EX)TREME | (I)MPOSSIBLE")
        diff = input('>').upper()
        escolhas = ['E', 'M', 'H', 'EX', 'I']
        if diff not in escolhas:
            print('faça uma escolha existente!')
        else:
            if diff == 'I':
                print('BoA SoRtEeEeEeE...')
            elif diff == 'EX':
                print('Desafiador...')
            elif diff == 'H':
                print('Veremos se é bom assim...')
            elif diff == 'M':
                print('Jogador casual.')
            elif diff == 'E':
                print('Novo de mais para perder.')
            return diff

def clear_screen():
    command = 'cls' if platform.system().lower() == "windows" else 'clear'
    os.system(command)


diff = menu()
sleep(2)
sudoku_board = mount_board()
copy_board = copy.deepcopy(sudoku_board)
copy_board = remove_tips(2, copy_board)
finish = False
msg = ""
while finish == False: 
    clear_screen()
    show_board(copy_board)
    print(msg)
    msg, copy_board = inserting_data(sudoku_board)
    
    if copy_board == sudoku_board:
        clear_screen()
        show_board(copy_board)
        print("PARABENS MANOOOO VC GANHOU VIADOO")
        finish = True
