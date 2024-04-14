"""Birthday Paradox Simulation, by Thanh Tran
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random


def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []

    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print('''Birthday Paradox, by Thanh Tran

The Birthday Paradox show us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        number_days = int(response)
        break  # User has entered a valid amount.

print()

# Generate and display the birthdays:
print('Here are', number_days, 'birthdays:')
birthdays = get_birthdays(number_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')

    month_name = MONTHS[birthday.month - 1]
    date_text = '{} {}'.format(month_name, birthday.day)
    print(date_text, end='')

print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100.100 simulations:
print('Generating', number_days, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\' run another 100,000 simulations.')
sim_match = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(number_days)
    if get_match(birthdays) is not None:
        sim_match = sim_match + 1

print('100,000 simulations run.')

# Display simulation results:
probability = round(sim_match / 100_000 * 100, 2)
print('Out of 100,000 simulations of', number_days, 'people, there was a')
print('matching birthday in that group', sim_match, 'times. This means')
print('that', number_days, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
