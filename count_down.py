"""Countdown, by Thanh Tran
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
Tags: tiny, artistic"""

import sys, time
import sevseg  # Imports our sevseg.py program.

# (!) Change this to any number of seconds:
seconds_left = 30

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 30)

        # Get the hours/minutes/seconds from secondsLeft:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # So 7265 // 3600 is 2 hours:
        hours = str(seconds_left // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        minutes = str((seconds_left % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(seconds_left % 60)

        # Get the digit strings from the sevseg module:
        h_digits = sevseg.getSevSegStr(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = sevseg.getSevSegStr(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = sevseg.getSevSegStr(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        # Display the digits:
        print(h_top_row + '     ' + m_top_row + '     ' + s_top_row)
        print(h_middle_row + '  *  ' + m_middle_row + '  *  ' + s_middle_row)
        print(h_bottom_row + '  *  ' + m_bottom_row + '  *  ' + s_bottom_row)

        if seconds_left == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        seconds_left -= 1

except KeyboardInterrupt:
    print('Countdown, by Thanh Tran')
    sys.exit()  # When Ctrl-C is pressed, end the program.)
