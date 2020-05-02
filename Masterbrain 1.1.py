import random, os, sys

CLEAR = '\033[0m'             # reset to the defaults

print('\033[30;47m      __  ______   _____________________  ____  ____  ___    _____   __ ')
print('\033[30;47m     /  |/  /   | / ___/_  __/ ____/ __ \/ __ )/ __ \/   |  /  _/ | / / ')
print('\033[30;47m    / /|_/ / /| | \__ \ / / / __/ / /_/ / __  / /_/ / /| |  / //  |/ /  ')
print('\033[30;47m   / /  / / ___ |___/ // / / /___/ _, _/ /_/ / _, _/ ___ |_/ // /|  /   ')
print('\033[30;47m  /_/  /_/_/  |_/____//_/ /_____/_/ |_/_____/_/ |_/_/  |_/___/_/ |_/    ')
print('\033[30;47m                                                                        ')

print('\033[97;41m    R    ''\033[97;42m    G    ''\033[97;43m    Y    ''\033[97;44m    B    ''\033[97;45m    M    ''\033[97;46m    C    ''\033[30;47m    W    ''\033[97;105m    P   ',CLEAR)

s = '\033[49m '           # Black
r = f'\033[41m    {s}'    # Red
g = f'\033[42m    {s}'    # Green
y = f'\033[43m    {s}'    # Yellow
b = f'\033[44m    {s}'    # Blue
m = f'\033[45m    {s}'    # Magenta
c = f'\033[46m    {s}'    # Cyan
w = f'\033[47m    {s}'    # Grey
p = f'\033[105m    {s}'   # Light Magenta

def RunAgain():
    os.system('cls')
    Masterbrian()

def Masterbrian():
    code = []
    colors  = ['r', 'g' ,'y' ,'b' ,'m' ,'c' ,'w', 'p']
    post1 = random.choice(colors)
    post2 = random.choice(colors)
    post3 = random.choice(colors)
    post4 = random.choice(colors)
    code.append(post1)
    code.append(post2)
    code.append(post3)
    code.append(post4)

    i = 1
    while True:
        diffPost = []
        guessList = []
        guess = input(f'\nGuess {i}/8? >> ')
        guess = f"{''.join(x.lower() if x != ' ' else '' for x in guess)}"
        for x in guess:
            guessList.append(x)
            if x in code:
                diffPost.append(x)

        samePost = set(enumerate(guessList)).intersection(set(enumerate(code)))

        if len(diffPost) >= len(samePost):
            diffPost = len(diffPost) - len(samePost)

        g1, g2, g3, g4 = eval(guessList[0]),eval(guessList[1]),eval(guessList[2]),eval(guessList[3])
        c1, c2, c3, c4 = eval(code[0]),eval(code[1]),eval(code[2]),eval(code[3])

        print(g1, g2, g3, g4, '\t\t\t',r * len(samePost), w * diffPost, CLEAR)

        if len(samePost) == 4:
            again = input("You cracked the code and earned the title of Masterbrain! Would you like to play again? Y/N >>  ")
            if again.lower() == 'y':
                RunAgain()
            else:
                exit()
        i += 1
        if i >= 9:
            print("You almost cracked the code! Here's the correct sequence:")
            print(c1, c2, c3, c4, CLEAR)
            again = input('Would you like to play again? Y/N >>  ')
            if again.lower() == 'y':
                RunAgain()
            else:
                exit()

Masterbrian()
