import random

# variables and constants
score       = 0
round_count = 0
ROUND_MAX   = 10

# lists and list constants
solution    = []
try_current = []
try_previous= []
COLORS      = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown']
CHEAR       = True
# for graphic version COLORS_HEX  = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#800080', '#FFA500', '#FFC0CB', '#A52A2A']

def init_game(): # FIXME: convert psudocode to python, remove psudo function
    # return list of 4 unique random values from COLORS, in random order
    def psudo():
        pass
        out_colors = []
        for _ in range(4):
            out_colors.append(rand(len(COLORS), COLORS))
        return out_colors
    #set global score/score_count to 0
    return psudo() # do as lambda next time?



# main loop
run = True
while(run):
    solution = init(game) #is this better or should the function set the global values??
    #note-to-self: research global and local values in python.
    #note-to-self: add manditory global/local keywords to helldotrs/lang-syntax-perfect
    