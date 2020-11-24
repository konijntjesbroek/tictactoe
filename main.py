'''
Tic Tac Toe 
Author: Arlo Gittings
Created: 2020-11-23
Purpose:
    Play a pointless game
'''

play_game = True

def draw_board(board):
    '''
        draw_board(list)
        purpose:
            display a row and column grid
        expects:
            board: <2d list> a list of all the available gridsquares
        returns:
            nothing
        exceptions:
            None
    '''
    print()
    
    for i, row in enumerate(board):
        for col, cell in enumerate(row):
            print(f' {cell} ', end='')
            if col != len(row) - 1:
                print('|', end='')
        if i != len(board) - 1:
            print('\n'+ ('--- ' * len(row)))
    print('\n\n')
            
def create_board(row, col):
    '''
        create_board(int, int)
        expects:
            row: <int> number of rows
            col: <int> number of columns
        returns:
            result: <2d list> empty list of row, col wide
        exceptions:
            none at this time
    '''
    result = []
    for r in range(row):
        hold = []
        for c in range(col):
            cell = (r * col) + c + 1
            hold.append(cell)
        result.append(hold)
    return result
            
def player_turn(board, marker):
    square_played = 0 
    taken = ('x', 'o')
    while square_played < 1 or square_played > 9:
        square_played = int(input(f"{marker}, pick a square: "))
        row = (square_played - 1) // len(board)
        col = (square_played - 1) % len(board)
        if board[row][col] in taken:
            print('That square is taken!')
            square_played = 0 
    board[row][col] = marker
    marker = 'x' if marker == 'o' else 'o'
    return board, marker

def chicken_dinner(board):
    result = False
    taken = ('x', 'o')
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            result = board[i][0]
            break
        elif board[0][i] == board[1][i] == board[2][i]:
            result = board[0][i]
            break
    if not result:
        if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
            result = board[1][1]
        else:
            for row in board:
                for cell in row:
                    if cell not in taken:
                        break
            if cell in taken:
                result = 'draw'
    
    return result

def play_again():
    result = False
    keep_going = ['y', 'yes']
    check_it = input('\n\nWould you like to play again?\nyes to continue, anything else to stop: ').strip().lower()
    if check_it in keep_going:
        result = True
    return result

while play_game == True:
    print()
    board = create_board(3, 3)
    marker = 'x'
    winner = False
    
    while not winner:
        draw_board(board)
        board, marker = player_turn(board, marker)
        winner = chicken_dinner(board)
    draw_board(board) 
    print(f'{winner} game')
    
    play_game = play_again()