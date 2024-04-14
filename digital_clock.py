"""Digital Clock, by Thanh Tran
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
Tags: tiny, artistic"""

import sys, time
import sevseg  # Imports our sevseg.py program.

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the current time from the computer's clock:
        current_time = time.localtime()

        # % 12 so we use a 12-hour clock, not 24:
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12-hour clocks show 12:00, not 00:00.

        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

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
        print()
        print('Press Ctrl-C to quit.')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break

except KeyboardInterrupt:
    print('Digital Clock, by Thanh Tran')
    sys.exit()  # When Ctrl-C is pressed, end the program.
