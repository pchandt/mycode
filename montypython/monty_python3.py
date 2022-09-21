#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer != "Brian":
    # increase the round counter by 1
    round += 1     

    # ask user to input answer to the quiz
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    
    # this will make all user input starts with an uppercase
    answer = answer.capitalize() 
                                
    # logic to check if user gave correct answer
    if answer == "Brian": 
        print("Correct!")
    
    # logic to ensure round has not yet reached 3
    elif round == 3:
        print("Sorry, the answer was Brian.")
    
    # if answer was wrong
    else:           
        print("Sorry. Try again!")

