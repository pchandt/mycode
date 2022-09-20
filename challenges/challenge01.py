#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
     print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_name = input("Please enter your name!")

    # asking user for day of the week
    week_day = input("What day of the week is it?")

    # display the input back to the user
    print(f"Hello, {user_name}! Happy {week_day}!")

# this calls main
main()

