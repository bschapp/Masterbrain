# Masterbrain, Version 1.1
# Created by Brian Schapp, 2 MAY 2020
# Prototype, digital Mastermind board game

import random, os, sys

# Formatting codes used for the pegs and red/white squares
CLEAR = '\033[0m'         # reset to default formating
s = '\033[49m '           # Black background, herein used as a spacer
r = f'\033[41m    {s}'    # Red
g = f'\033[42m    {s}'    # Green
y = f'\033[43m    {s}'    # Yellow
b = f'\033[44m    {s}'    # Blue
m = f'\033[45m    {s}'    # Magenta
c = f'\033[46m    {s}'    # Cyan
w = f'\033[47m    {s}'    # Grey
p = f'\033[105m    {s}'   # Light Magenta

def Instructions():
    print('''\nThis game follows the standard Mastermind instructions.\n
    A sequence containing 4 colors ('pegs') is randomly generated and hidden from the
    player. Colors may repeat.\n
    The object is to guess the sequence. Enter your guess using the letter that represents each
    peg (provided at the top of the window).\n
    Your guess will be displayed. To the right of your guess will be displayed red
    and white squares.\n
    A white square indicates that a peg you chose is in the sequence but is not in the correct
    position. One white square will be displayed for each peg meeting this condition.\n
    A red square indicates that a peg is both in the sequence and in the correct position.
    One red square will be displayed for each peg meeting this condition.\n
    Note that the position of the squares is NOT indicative of the position of the peg.
    All red squares are displayed first, followed by all white squares.\n
    You have ten chances to guess the correct sequence. Good luck.''')

def TitleBlock():
    # Title block, peg colors and corresponding letters displayed at the top of
        # each game
    print('\033[30;47m'
    '''|    __  ______   _____________________  ____  ____  ___    _____   __|
|   /  |/  /   | / ___/_  __/ ____/ __ \/ __ )/ __ \/   |  /  _/ | / /|
|  / /|_/ / /| | \__ \ / / / __/ / /_/ / __  / /_/ / /| |  / //  |/ / |
| / /  / / ___ |___/ // / / /___/ _, _/ /_/ / _, _/ ___ |_/ // /|  /  |
|/_/  /_/_/  |_/____//_/ /_____/_/ |_/_____/_/ |_/_/  |_/___/_/ |_/   |
|                                                                     |\n'''
'\033[97;41m    R    \033[97;42m    G    \033[97;43m    Y    '
'\033[97;44m    B    \033[97;45m    M    \033[97;46m    C    '
'\033[30;47m    W    \033[97;105m    P  ', CLEAR)
    welcome = input('\nWelcome to Masterbrain! \n\nWould you like to read the '
    'instructions? Y/N >> ')
    if welcome.lower() == 'y':
        Instructions()
        pass
    input("\nEnter your guesses below. In place of a guess, enter...\n"
    '\t"restart" to start a new game\n'
    '\t"exit" to exit the game\n'
    '\t"show" to reveal the code\n'
    'Press "Enter" to continue to the game now. Have fun!')

def RunAgain():
    # Clears the screen and re-starts the game from the beginning
    os.system('cls')
    Masterbrian()

def Masterbrain():
    TitleBlock()
    code = ['r','r','g','y']
    colors  = ['r', 'g' ,'y' ,'b' ,'m' ,'c' ,'w', 'p']
    post1 = random.choice(colors)
    post2 = random.choice(colors)
    post3 = random.choice(colors)
    post4 = random.choice(colors)
    code.append(post1)
    code.append(post2)
    code.append(post3)
    code.append(post4)
    # Randomly generates four letters (pegs) and adds them to 'code' list

    i = 1
    while True:
        try:
            diffPost = []
            guessList = []
            p1, p2 = eval(code[0]),eval(code[1])
            p3, p4 = eval(code[2]), eval(code[3])
            guess = input(f'\nGuess {i}/10? >> ')

            if guess.lower() == 'restart':
                RunAgain()
            elif guess.lower() == 'show':
                print('\nThe correct sequence is \n',p1, p2, p3, p4, CLEAR,
                'As a result of your impatience, the game will now end.')
                exit()
            elif guess.lower() == 'exit':
                print('Thank you for playing! Goodbye!')
                exit()

            guess = f"{''.join(x.lower() if x != ' ' else '' for x in guess)}"
            for x in guess:
                guessList.append(x)
                if x in code:
                    diffPost.append(x)

            samePost = set(enumerate(guessList)).intersection(set(enumerate(code)))

            if len(diffPost) >= len(samePost):
                diffPost = len(diffPost) - len(samePost)

            g1, g2 = eval(guessList[0]),eval(guessList[1])
            g3, g4 = eval(guessList[2]),eval(guessList[3])

            print(g1,g2,g3,g4,'\t\t\t', r * len(samePost), w * diffPost, CLEAR)

            if len(samePost) == 4:
                again = input("You cracked the code and earned the title of "
                "Masterbrain! Would you like to play again? Y/N >>  ")
                if again.lower() == 'y':
                    RunAgain()
                else:
                    exit()
            i += 1

            if i >= 11:
                print("You almost cracked the code! Here's the correct sequence:")
                print(p1, p2, p3, p4, CLEAR)
                again = input('Would you like to play again? Y/N >>  ')
                if again.lower() == 'y':
                    RunAgain()
                else:
                    exit()
        except NameError:
            print(f"\n'{guess.upper()}' is not a valid sequence! Please try again.")
        except IndexError:
            print("\nThat's not the right number of pegs! A valid guess has 4 pegs.")

Masterbrain()
