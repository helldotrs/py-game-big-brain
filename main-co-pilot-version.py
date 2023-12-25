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
# for graphic version COLORS_HEX  = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#800080', '#FFA500', '#FFC0CB', '#A52A2A']

# main loop #co-pilot wrote all the following without me in single tab.. will it work??
"""
it did not work:
$ py main-co-pilot-version.py 
Traceback (most recent call last):
  File "/[snip]]/main-co-pilot-version.py", line 17, in <module>
    solution.append(random.choice(COLORS))
                    ^^^^^^
NameError: name 'random' is not defined
"""
"""
fixed previous error by adding import random at top of file. Now it executes but co-pilot has no idea what the code was intended to do, and I got no idea what co-pilot intended to achieve.
The error at the end is me ending the program with ctrl-c:
$ py main-co-pilot-version.py 
['purple']
Enter the solution, one color at a time
Enter color 1: red
Incorrect!
Score: 0
Previous solution: ['red']
Current solution: ['red']
Solution: ['purple']
Press enter to continue...
['purple', 'yellow']
Enter the solution, one color at a time
Enter color 1: purple
Enter color 2: yellow
Correct!
Score: 1
Previous solution: ['purple', 'yellow']
Current solution: ['purple', 'yellow']
Solution: ['purple', 'yellow']
Press enter to continue...
['purple', 'yellow', 'green']
Enter the solution, one color at a time
Enter color 1: purple
Enter color 2: yellow
Enter color 3: green
Correct!
Score: 2
Previous solution: ['purple', 'yellow', 'green']
Current solution: ['purple', 'yellow', 'green']
Solution: ['purple', 'yellow', 'green']
Press enter to continue...
['purple', 'yellow', 'green', 'green']
Enter the solution, one color at a time
Enter color 1: 
Enter color 2: purple
Enter color 3: yellow
Enter color 4: green
Incorrect!
Score: 2
Previous solution: ['', 'purple', 'yellow', 'green']
Current solution: ['', 'purple', 'yellow', 'green']
Solution: ['purple', 'yellow', 'green', 'green']
Press enter to continue...
['purple', 'yellow', 'green', 'green', 'orange']
Enter the solution, one color at a time
Enter color 1: Traceback (most recent call last):
  File "/[snip]/main-co-pilot-version.py", line 33, in <module>
    try_current.append(input('Enter color ' + str(i+1) + ': '))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EOFError
"""
while round_count < ROUND_MAX:
    # generate a new solution
    solution.append(random.choice(COLORS))
    # show the solution
    print(solution)
    # wait for the player to enter a solution
    print('Enter the solution, one color at a time')
    try_current = []
    for i in range(len(solution)):
        try_current.append(input('Enter color ' + str(i+1) + ': '))
    # check the player's solution
    if try_current == solution:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    # increment the round counter
    round_count += 1
    # save the player's solution
    try_previous = try_current
    # show the player's score
    print('Score: ' + str(score))
    # show the player's previous solution
    print('Previous solution: ' + str(try_previous))
    # show the player's current solution
    print('Current solution: ' + str(try_current))
    # show the solution
    print('Solution: ' + str(solution))
    # wait for the player to press enter
    input('Press enter to continue...')