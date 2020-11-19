 #!/user/bin/python
#Created by Brian Schapp, 19 August 2020
import math, random, sys, os, itertools
import tkinter as tk
from tkinter import messagebox as mbx

root = tk.Tk()
root.geometry('300x600')
board = tk.Canvas(root, height=600, width=300, bg = 'peru')

# CODE GENERATION #############################################################
colors  = ['r', 'o' ,'y' ,'g' ,'b' ,'i' ,'p', 'w']
code = [random.choice(colors) for i in range(1,5)]
guess = []
print(code)
###############################################################################

# KEYS ########################################################################
a = 180
b = 10
c = 190
d = 20
i = 0
while i < 12:
    coord1 = a, b, c, d
    key1 = board.create_oval(coord1)
    coord2 = a + 20, b , c + 20, d
    key2 = board.create_oval(coord2)
    coord3 = a, b + 20, 190, d + 20
    key3 = board.create_oval(coord3)
    coord4 = a + 20, b + 20, c + 20, d + 20
    key4 = board.create_oval(coord4)
    b += 40
    d += 40
    i += 1
###############################################################################

# PEGS ########################################################################
i = tk.IntVar()
a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()
d = tk.IntVar()
i.set(0)
a.set(10)
b.set(10)
c.set(40)
d.set(40)

e = tk.IntVar()
f = tk.IntVar()
g = tk.IntVar()
h = tk.IntVar()
e.set(180)
f.set(10)
g.set(190)
h.set(20)


def peg(color):
    global guess, code
    guess.append(color[0])

    coord = [a.get(), b.get(), c.get(), d.get()]
    circleA = board.create_oval(coord, fill = color, tags = 'pegs')
    a.set(a.get() + 40)
    if a.get() > 130:
        a.set(10)
    c.set(c.get() + 40)
    if c.get() > 160:
        c.set(40)
        b.set(b.get() + 40)
        d.set(d.get() + 40)

    i.set(i.get() + 1)
    if i.get() == 4:
        for button in buttons:
            button['state'] = 'disabled'

        blackKey = 0
        whiteKey = 0

        j = 0
        while j < 4:
            if code[j] == guess[j]:
                blackKey += 1
            elif guess[j] in code and guess[j] != code[j]:
                whiteKey += 1
            j += 1
    # KEY POSISTIONING #
        for key in range(blackKey):
            if e.get() > 200:
                f.set(f.get() + 20)
                h.set(h.get() + 20)
                e.set(180)
            if g.get() > 210:
                g.set(190)
            coord1 = [e.get(), f.get(), g.get(), h.get()]
            key = board.create_oval(coord1, fill = 'black', tags = 'keys')
            e.set(e.get() + 20), g.set(g.get() + 20)

        for key in range(whiteKey):
            if e.get() > 200:
                f.set(f.get() + 20)
                h.set(h.get() + 20)
                e.set(180)
            if g.get() > 210:
                g.set(190)
            coord1 = [e.get(), f.get(), g.get(), h.get()]
            key = board.create_oval(coord1, fill = 'white', tags = 'keys')
            e.set(e.get() + 20), g.set(g.get() + 20)

        e.set(180), g.set(190)

        elif blackKey == 4:
            mbx.showinfo('Congratulations:',
            'Well done! You cracked the code and won the game. '
            'To play again, please exit and run the program again. Otherwise, '
            'click "quit" now. Thanks for playing!')
        if (blackKey + whiteKey) <= 2:
            f.set(f.get() + 40)

            h.set(h.get() + 40)
        elif (blackKey + whiteKey) >= 3:
            f.set(f.get() + 20)
            h.set(h.get() + 20)
    ####################
        guess = []
        for button in buttons:
            button['state'] = 'normal'
        i.set(0)
###############################################################################

# INSTRUCTIONS ################################################################
def help():
    mbx.showinfo('How to Play:',
    '''A sequence containing 4 colors ('pegs') is randomly generated
    and hidden from the player. Colors may repeat.

    The object is to guess the sequence. Enter your guess using
    the colored buttons at the bottom of the board.

    Your guess will be displayed on the board. To the right of
    your guess will be displayed black and white dots ('keys').

    A white key indicates that one peg you chose is in the
    sequence, but is not in the correct position.

    A black key indicates that one peg is both in the
    sequence and in the correct position.

    Note that the position of the keys is NOT indicative of
    the position of the peg. All black keys are displayed first,
    followed by all white keys.

    You have 12 chances to guess the correct sequence.''')
###############################################################################

# OTHER FUNCTIONS #############################################################
def quit():
    root.destroy()
###############################################################################

# BUTTON ARANGEMENT ###########################################################
red = tk.Button(board, bg = 'red', command = lambda: peg('red'))
orange = tk.Button(bg = 'orange', command = lambda: peg('orange'))
yellow = tk.Button(bg = 'yellow', command = lambda: peg('yellow'))
green = tk.Button(bg = 'green', command = lambda: peg('green'))
blue = tk.Button(bg = 'blue', command = lambda: peg('blue'))
indigo = tk.Button(bg = 'indigo', command = lambda: peg('indigo'))
violet = tk.Button(bg = 'plum', command = lambda: peg('plum'))
white = tk.Button(bg = 'white', command = lambda: peg('white'))

buttons = [red, orange, yellow, green, blue, indigo, violet, white]

help = tk.Button(root, text = 'Help', command = help)
help.place(x = 10, y = 550, width = 90, height = 30)

quit = tk.Button(root, text = 'Quit', command = quit)
quit.place(x = 200, y = 550, width = 90, height = 30)

red.place(x = 10, y = 500, width = 30, height = 30)
orange.place(x = 45, y = 500, width = 30, height = 30)
yellow.place(x = 80, y = 500, width = 30, height = 30)
green.place(x = 115, y = 500, width = 30, height = 30)
blue.place(x = 150, y = 500, width = 30, height = 30)
indigo.place(x = 185, y = 500, width = 30, height = 30)
violet.place(x = 220, y = 500, width = 30, height = 30)
white.place(x = 255, y = 500, width = 30, height = 30)
###############################################################################

board.pack()
root.mainloop()
