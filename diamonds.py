r"""Diamonds, by Thanh Tran
Draws diamonds of various sizes.
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
Tags: tiny, beginner, artistic"""


def main():
    print('Diamonds, by Thanh Tran')

    # Display diamonds of sizes 0 through 6:
    for diamondSize in range(0, 6):
        display_outline_diamond(diamondSize)
        print()  # Print a newline.
        display_filled_diamond(diamondSize)
        print()  # Print a newline.


def display_outline_diamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/', end='')  # Left side of diamond.
        print(' ' * (i * 2), end='')  # Interior of diamond.
        print('\\')  # Right side of diamond.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * i, end='')  # Left side space.
        print('\\', end='')  # Left side of diamond.
        print(' ' * ((size - i - 1) * 2), end='')  # Interior of diamond.
        print('/')  # Right side of diamond.


def display_filled_diamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/' * (i + 1), end='')  # Left half of diamond.
        print('\\' * (i + 1))  # Right half of diamond.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * i, end='')  # Left side space.
        print('\\' * (size - i), end='')  # Left side of diamond.
        print('/' * (size - i))  # Right side of diamond.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
