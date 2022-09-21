#!/usr/bin/env python3
"""Alternate solution of list - challenge"""

import random

def main():
    # create a list called wordbank
    wordbank= ["indentation", "spaces"] 

    # create a list called tlgstudents
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]


    # add 4 to the list wordbank
    wordbank.append(4)

    # ask user to input a number between 0 and 18 and save this as the variable num
    num = input("Please enter a number between 0 and 18: ")

    # if input a digit, convert input to integer and use it to slice one of the elements from the list tlgstudents
    # save the returned name as student_name
    if num.isdigit():
        student_name = tlgstudents[int(num)]

    # if input is not a digit, use choice() function to grab a random name and save it as student_name
    else:
        student_name = random.choice(tlgstudents)

    # print the statement using elements from tlgstudents and student_name
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent." )


main()

