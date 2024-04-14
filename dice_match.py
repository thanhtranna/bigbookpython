"""Dice Math, by Thanh Tran
A flash card addition game where you sum the total on random dice rolls.
Tags: large, artistic, game, math"""

import random, time

# Set up the constants:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom.

# The duration is in seconds:
QUIZ_DURATION = 30  # (!) Try changing this to 10 or 60.
MIN_DICE = 2  # (!) Try changing this to 1 or 5.
MAX_DICE = 6  # (!) Try changing this to 14.

# (!) Try changing these to different numbers:
REWARD = 4  # (!) Points awarded for correct answers.
PENALTY = 1  # (!) Points removed for incorrect answers.
# (!) Try setting PENALTY to a negative number to give points for
# wrong answers!

# The program hangs if all the dice can't fit on the screen:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, by Thanh Tran

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

# Keep track of how many answers were correct and incorrect:
correct_answers = 0
incorrect_answers = 0
start_time = time.time()

while time.time() < start_time + QUIZ_DURATION:  # Main game loop.
    # Come up with the dice to display:
    sum_answer = 0
    dice_faces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0] contains the list of strings of the die face:
        dice_faces.append(die[0])
        # die[1] contains the integer number of pips on the face:
        sum_answer += die[1]

    # Contains (x, y) tuples of the top-left corner of each die.
    top_left_dice_corners = []

    # Figure out where dice should go:
    for i in range(len(dice_faces)):
        while True:
            # Find a random place on the canvas to put the die:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Get the x, y coordinates for all four corners:
            #      left
            #      v
            # top > +-------+ ^
            #      | O     | |
            #      |   O   | DICE_HEIGHT (5)
            #      |     O | |
            #      +-------+ v
            #      <------->
            #      DICE_WIDTH (9)

            top_left_x = left
            top_left_y = top
            top_right_x = left + DICE_WIDTH
            top_right_y = top
            bottom_left_x = left
            bottom_left_y = top + DICE_HEIGHT
            bottom_right_x = left + DICE_WIDTH
            bottom_right_y = top + DICE_HEIGHT

            # Check if this die overlaps with previous dice.
            overlaps = False
            for prev_die_left, prev_die_top in top_left_dice_corners:
                prev_die_right = prev_die_left + DICE_WIDTH
                prev_die_bottom = prev_die_top + DICE_HEIGHT
                # Check each corner of this die to see if it is inside
                # the area the previous die:
                for cornerX, cornerY in ((top_left_x, top_left_y),
                                         (top_right_x, top_right_y),
                                         (bottom_left_x, bottom_left_y),
                                         (bottom_right_x, bottom_right_y)):
                    if (prev_die_left <= cornerX < prev_die_right
                            and prev_die_top <= cornerY < prev_die_bottom):
                        overlaps = True

            if not overlaps:
                # It doesn't overlap, so we can put it here:
                top_left_dice_corners.append((left, top))
                break

    # Draw the dice on the canvas:

    # Keys are (x, y) tuples of ints, values the character at that
    # position on the canvas:
    canvas = {}
    # Loop over each die:
    for i, (die_left, die_top) in enumerate(top_left_dice_corners):
        # Loop over each character in the die's face:
        die_face = dice_faces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # Copy this character to the correct place on the canvas:
                canvasX = die_left + dx
                canvasY = die_top + dy
                # Note that in dieFace, a list of strings, the x and y
                # are swapped:
                canvas[(canvasX, canvasY)] = die_face[dy][dx]

    # Display the canvas on the screen:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # Print a newline.

    # Let the player enter their answer:
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sum_answer:
        correct_answers += 1
    else:
        print('Incorrect, the answer is', sum_answer)
        time.sleep(2)
        correct_answers += 1

# Display the final score:
score = (correct_answers * REWARD) - (incorrect_answers * PENALTY)
print('Correct:  ', correct_answers)
print('Incorrect:', incorrect_answers)
print('Score:    ', score)
