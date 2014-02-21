#*-* coding: utf-8 *-*
def make_board():
    """Create a Tic-tac-toe board"""
    board = [[' ' for i in range(3)] for i in range(3)]
    return board


def print_board(board):
    """print the board"""
    lines = len(board) - 1
    counter = 0

    print '\n'
    for l in board:
        print " %s | %s | %s " % tuple(l)
        if counter < lines:
            counter += 1
            print "------------"
    print '\n'


def move_allowed(move, board):
    """Check if a move is allowed"""
    if not ',' in move:
        print '\nERRO: O formato da joaga deve ser linha,coluna. Ex: 2,0'
        return False

    try:
        line, col = [int(x) for x in move.split(',')]
    except ValueError:
        print '\nERRO: O valor da linha/coluna deve ser um numero'
        return False

    if line >= len(board) or col >= len(board):
        print '\nERRO: O valor da linha/coluna deve estar entre 0 e 2'
        return False

    if board[line][col] != ' ':
        print u'\nERRO: Esse lugar já está marcado'
        print_board(board)
        return False
    return True


def get_line_col(move):
    """Return the line,col given a move string"""
    return [int(x) for x in move.split(',')]


def status(board, simbols):
    """Return the winner player ou False if there's no winner"""
    size = len(board)
    for s in simbols:

        # check for line wineer
        result = []
        for line in board:
            result = [col for col in line if col == s]
            if len(result) == size:
                return s

        # check for collumn winner
        result = []
        for col in range(size):
            result = [l[col] for l in board if l[col] == s]
            if len(result) == size:
                return s

        #check diagonals
        result = []
        for x in range(size):
            if board[x][x] == s:
                result.append(s)
        if len(result) == size:
            return s

        result = []
        col_max = len(board) - 1
        for x in range(size):
            if board[x][col_max - x] == s:
                result.append(s)
        if len(result) == size:
            return s
    return False


def moves_left(board):
    """Return how many moves are left"""
    result = len(board) * len(board)
    for l in board:
        result = result - len([c for c in l if c != ' '])
    return result


def make_move(move, board, player):
    line, col = get_line_col(move)
    board[line][col] = player
    return board


def start_game():
    """Start the game itself"""
    allowed_chars = ('*', '#')
    simbol = False

    #user have to choose whos starting
    while simbol not in allowed_chars:
        simbol = raw_input('Escolha quem vai começar %s ou %s: ' %
                           allowed_chars)

    #init and show empty board
    active = simbol
    board = make_board()
    print_board(board)

    #until the game finish
    while True:
        #get move
        move = raw_input('"%s" - Qual sua jogada (linha, coluna): ' %
                        (active, ))

        #is this move allowed?
        if not move_allowed(move, board):
            continue

        #do the move and print the board
        board = make_move(move, board, active)
        print_board(board)

        #the game is end?
        result = status(board, allowed_chars)
        if result:
            print 'O vencedor é: %s' % (result, )
            break

        #change the active player, alternate between "#" and "*"
        if active == allowed_chars[0]:
            active = allowed_chars[1]
        else:
            active = allowed_chars[0]

        #there's no move left? Game is tie!
        if not moves_left(board):
            print 'Jogo empatado!'
            break

#entry point
if __name__ == '__main__':
    while True:
        start_game()
        awser = False
        while awser not in ['s', 'n']:
            awser = raw_input('Jogar novamente (S/N)? ').lower()
        if awser == 'n':
            break
