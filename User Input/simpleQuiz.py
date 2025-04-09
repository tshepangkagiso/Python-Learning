# Create a program that generates a simple quiz. Ask the user multiple-choice questions, keep track of their score, and display the final result.



def simpleQuiz():
    resultCount = 0

    print('\n 1) What is a variable? \n A) Storage \n B) Container \n C) Math problem \n D) Nothing ')
    question1 = input('Answer: ')
    if question1.lower() == 'b':
        resultCount = resultCount + 1

    print('\n 2) What does a loop do in programming? \n A) Jumps around \n B) Stores data \n C) Repeats actions \n D) Ends code ')
    question2 = input('Answer: ')
    if question2.lower() == 'c':
        resultCount = resultCount + 1

    print('\n 3) What is an if statement used for? \n A) Looping \n B) Decision making \n C) Drawing \n D) Saving files ')
    question3 = input('Answer: ')
    if question3.lower() == 'b':
        resultCount = resultCount + 1

    print('\n 4) What does a function do? \n A) Makes decisions \n B) Repeats code \n C) Organizes code into reusable blocks \n D) Deletes files ')
    question4 = input('Answer: ')
    if question4.lower() == 'c':
        resultCount = resultCount + 1


    if resultCount < 2:
        print(f'You failed, score: {(resultCount/4)*100}%')
    elif resultCount >= 2:
        print(f'You passed, score: {(resultCount/4)*100}%')


simpleQuiz()