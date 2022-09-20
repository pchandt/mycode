#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - challenge"""

def main():
    # create a list called wordbank
    wordbank= ["indentation", "spaces"]

    # create a list called tlgstudents
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4) # this adds 4 to the list
    print(wordbank)

    # collect a number between 0 and 18 from the user and convert it to integer
    num = int(input("Please enter a number between 0 and 18: "))

    # slice one of the element from the list tlgstudents using int value of num and save it as student_name
    student_name = tlgstudents[num] 
    print(student_name)

    # print a statement including elements of tlgstudents list and the student_name string
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    
main()
