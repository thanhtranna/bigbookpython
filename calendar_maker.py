"""Calendar Maker, by Thanh Tran
Create monthly calendars, saved to a text file and fit for printing.
Tags: short"""

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar maker, by Thanh Tran')

# Store year entered by user
year = 0

# Store month entered by user
month = 0

while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2024.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def get_calendar_for(year: int, month: int):
    calendar_text = ''  # cal_text will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calendar_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
    calendar_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separate weeks:
    week_separator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blank_row = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    current_date = datetime.date(year, month, 1)

    # Roll back current_date until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        calendar_text += week_separator

        # dayNumberRow is the row with the day number labels:
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)  # Go to next day.
        day_number_row += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calendar_text += day_number_row
        for i in range(3):  # (!) Try changing the 4 to a 5 or 10.
            calendar_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calendar_text += week_separator
    return calendar_text


cal_text = get_calendar_for(year, month)
print(cal_text)  # Display the calendar.

# Save the calendar to a text file:
calendar_filename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendar_filename, 'w') as fileObj:
    fileObj.write(cal_text)

print('Saved to ' + calendar_filename)
