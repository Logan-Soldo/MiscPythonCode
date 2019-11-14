import reversi
import string
LETTERS = string.ascii_lowercase

"""
Write something about this program here.
"""

def indexify(position):
    """
    Write something here
    """
    row = str(position[0])
    row = string.ascii_lowercase.index(row)
    column = int(position[1:])
    position=(row,column-1)
    return position

def deindexify(row, col):
    """
    Write something here
    """
    
    row = chr(row+97)
    col = (col + 1)
   
    
    return row+str(col)
    
def initialize(board):
    """
    Write something here
    """
    
    center=int((board.length/2))
    
    board.place(center-1,center-1,reversi.Piece("white"))
    board.place(center,center,reversi.Piece('white'))
    board.place(center,center-1,reversi.Piece("black"))
    board.place(center-1,center,reversi.Piece("black"))
    
def count_pieces(board):
    """
    Write something here
    """
    black=0
    white=0
    
    for x in range(board.length):
        for y in range(board.length):
            if reversi.Piece.is_black == True:
                black += 1
            if reversi.Piece.is_white == True:
                white += 1
    
    print(black,white)
    return black,white

def get_all_streaks(board, row, col, piece_arg):
    """
    Write something here
    """
    streaks = {'e': None, 'w': None, 'n': None, 's': None, \
               'ne': None, 'nw': None, 'se': None, 'sw': None}
    
    color = piece_arg.color()
    other_color = 'white' if color == 'black' else 'black'
    # north
    L = []
    c = col
    for r in range(row-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['n'] = sorted(L)

#    # east
    L = []
    c = col
    r = row
    for c in range(col+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['e'] = sorted(L)
 
#    # south
    L = []
    c = col
    r = row
    for r in range(row+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['s'] = sorted(L)

#    # west
    L = []
    c = col
    r = row
    for c in range(col-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['w'] = sorted(L)

#    # northeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row-1,-1,-1):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['ne'] = sorted(L)
        
#    # southeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row+1,board.length):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['se'] = sorted(L)
                
#    # southwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row+1,board.length):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['sw'] = sorted(L)
    
#    # northwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row-1,-1,-1):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['nw'] = sorted(L)
            
    return streaks

def get_all_capturing_cells(board, piece):
    """
    Write something here
    """
    pass

def get_hint(board, piece):
    """
    Write something here
    """
    pass
    
def place_and_flip(board, row, col, piece):
    """
    Write something here
    """
    #"Can't place {:s} at '{:s}',"
    #" already occupied. Type 'hint' to get suggestions."
    #" it's not a capture. Type 'hint' to get suggestions."
    #" invalid position. Type 'hint' to get suggestions."
    pass

def is_game_finished(board):
    """
    Write something here
    """
    pass
            
def get_winner(board):
    """
    Write something here
    """
    pass
    
def choose_color():
    """
    Write something here
    """
    
    while True:
        color=input("Choose the color: ")
        if color.lower() == "black":
            print("You are '{:s}' and your opponent is '{:s}'.".format("black",'white'))
            return ('black','white')
        elif color.lower() == "white":
            print("You are '{:s}' and your opponent is '{:s}'.".format('white','black'))
            return ('white','black')
    
        else:
            print("Wrong color, type only 'black' or 'white', try again.")

        
            

def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    """
    
    banner = """
     _____                         _ 
    |  __ \                       (_)
    | |__) |_____   _____ _ __ ___ _ 
    |  _  // _ \ \ / / _ \ '__/ __| |
    | | \ \  __/\ V /  __/ |  \__ \ |
    |_|  \_\___| \_/ \___|_|  |___/_|
    
    Developed by The Students Inc.
    CSE231 Spring Semester 2018
    Michigan State University
    East Lansing, MI 48824, USA.
    """

    prompt = "[{:s}'s turn] :> "
    print(banner)
   
    # Choose the color here
    (my_color, opponent_color) = choose_color()
    
    # Take a board of size 8x8
    # Prompt for board size
    size = input("Input a board size: ")
    board = reversi.Board(int(size))
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'white' else opponent_color
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get a piece according to turn
            piece = reversi.Piece(turn)

            # Get the command from user using input
            command = input(prompt.format(turn)).lower()
            
            # Now decide on different commands
            if command == 'exit':
                break
            elif command == 'hint':
                print("\tHint: " + ", ".join(get_hint(board, piece)))
            elif command == 'pass':
                hint = get_hint(board, piece)
                if len(hint) == 0:
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
                    print("\tHanded over to \'{:s}\'.".format(turn))
                else:
                    print("\tCan't hand over to opponent, you have moves," + \
                          " type \'hint\'.")
            else:
               #     (row,col) = deindexify(0,1)
                    (row, col) = indexify(command)
                    place_and_flip(board, row, col, piece)
                    print("\t{:s} played {:s}.".format(turn, command))
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    winner = get_winner(board)
    if winner != 'draw':
        diff = abs(piece_count[0] - piece_count[1])
        print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
    else:
        print("This game ends in a draw.")
    # --- end of game play ---

def figure_1(board):
    """
    You can use this function to test your program
    """
    board.place(0,0,reversi.Piece('black'))
    board.place(0,3,reversi.Piece('black'))
    board.place(0,4,reversi.Piece('white'))
    board.place(0,5,reversi.Piece('white'))
    board.place(0,6,reversi.Piece('white'))
    board.place(1,1,reversi.Piece('white'))
    board.place(1,3,reversi.Piece('white'))
    board.place(1,5,reversi.Piece('white'))
    board.place(1,6,reversi.Piece('white'))
    board.place(1,7,reversi.Piece('white'))
    board.place(2,2,reversi.Piece('white'))
    board.place(2,3,reversi.Piece('black'))
    board.place(2,4,reversi.Piece('white'))
    board.place(2,5,reversi.Piece('white'))
    board.place(2,7,reversi.Piece('white'))
    board.place(3,0,reversi.Piece('black'))
    board.place(3,1,reversi.Piece('white'))
    board.place(3,2,reversi.Piece('white'))
    board.place(3,4,reversi.Piece('white'))
    board.place(3,5,reversi.Piece('white'))
    board.place(3,6,reversi.Piece('black'))
    board.place(3,7,reversi.Piece('black'))
    board.place(4,0,reversi.Piece('white'))
    board.place(4,2,reversi.Piece('white'))
    board.place(4,4,reversi.Piece('white'))
    board.place(5,0,reversi.Piece('black'))
    board.place(5,2,reversi.Piece('black'))
    board.place(5,3,reversi.Piece('white'))
    board.place(5,5,reversi.Piece('black'))
    board.place(6,0,reversi.Piece('black'))
    board.place(6,1,reversi.Piece('black'))
    board.place(6,3,reversi.Piece('white'))
    board.place(6,6,reversi.Piece('white'))
    board.place(7,1,reversi.Piece('black'))
    board.place(7,2,reversi.Piece('white'))
    board.place(7,3,reversi.Piece('black'))
    board.place(7,7,reversi.Piece('black'))
    
if __name__ == "__main__":
    game_play_human()
