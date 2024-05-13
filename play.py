from random import randint
from games.tictactoe import tctct

def main():
    parameters = {'rows' : input('Choose how many rows the board will have: '),
    'columns' : input('Choose how many columns the board will have: '),
    'gamemode' : input('Choose PC/pc to play against the machine or PVP/pvp to play against a local player: ')}

    for label, value in parameters.items():
        if label == 'gamemode':
            string = value.upper().replace(' ', '')
            while string not in ['PC', 'PVP']:
                parameters[label] = input(f'Wrong data type on {label} type\nTry Again: ')
        while not value.isnumeric() and label != 'gamemode':
            parameters[label] = input(f'Wrong data type on {label} type\nTry Again: ')
        if label != 'gamemode':
            parameters[label] = int(value)

    gamemode = parameters['gamemode'].upper().replace(' ', '')
    space = 7

    if gamemode == 'PVP':
        marks = {'player1' : input("Choose Player 1's symbol: "),
                    'player2' : input("Choose Player 2's symbol: ")}
        for label, value in marks.items():
            while len(value) > space:
                marks[label] = (f'Choose a shorter symbol (max. {space} chars): ')        
    
    length = (space, 1)
    title_length = 40
    board_pad = ( title_length -  (((length[0] + 1) * parameters['columns']) + 1) ) // 2

    print('''
 _______    ______        ______        
/_  __(_)__/_  __/__ ____/_  __/__  ___ 
 / / / / __// / / _ `/ __// / / _ \/ -_)
/_/ /_/\__//_/  \_,_/\__//_/  \___/\__/ ''')
    print((' ' * 11) + 'by github/frncscp')
    

    def init():
        global game
        game = tctct(rows = parameters['rows'],
                    columns = parameters['columns'],
                    pad = board_pad,
                    marks = marks if gamemode == 'PVP' else ['human', 'pc'])
        game.display_board()

    init()

    def user_turn(mark):
        option = input('Choose a place to put your mark: ')
        turn = game.choose(option, mark)
        while turn is None:
            option = input('Invalid Option. Check that your option is a number and is available to choose: ')
            turn = game.choose(option, mark)
        game.display_board()

    def pc_turn(mark):
        print("PC's turn", end="\r")
        option = str(randint(1, game.rows*game.columns))
        turn = game.choose(option, mark)
        while turn is None:
            option = str(randint(1, game.rows*game.columns))
            turn = game.choose(option, mark)
        game.display_board()
    

    def separator():
        print('.' * title_length)

    play_again = True

    while play_again:

        if gamemode == 'PC':
            while not game.check_win():
                separator()
                user_turn('human')
                separator()
                if not game.check_win():
                    pc_turn('pc')
                else:
                    break  

        elif gamemode == 'PVP':
            while not game.check_win():
                separator()
                user_turn(marks['player1'])
                separator()
                if not game.check_win():
                    user_turn(marks['player2'])
                else:
                    break  

        print(f'The {game.check_win()} player won!')

        again = input('if you want to play again, press Enter, any other key will close the program.')

        if again != '':
            break
        else: 
            init()
        
if __name__ == '__main__':
    main()