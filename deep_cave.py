"""Deep Cave, by Thanh Tran
An animation of a deep cave that goes forever into the earth.
Tags: tiny, beginner, scrolling, artistic"""

import random, sys, time

# Set up the constants:
WIDTH = 70  # (!) Try changing this to 10 or 30.
PAUSE_AMOUNT = 0.05  # (!) Try changing this to 0 or 1.0.

print('Deep Cave, by Thanh Tran')
print('Press Ctrl-C to stop.')
time.sleep(2)

left_width = 20
gap_width = 10

while True:
    # Display the tunnel segment:
    right_width = WIDTH - gap_width - left_width
    print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

    # adjust the left side width:
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_width > 1:
        left_width = left_width - 1  # Decrease left side width.
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        left_width = left_width + 1  # Increase left side width.
    else:
        pass  # Do nothing; no change in left side width.
