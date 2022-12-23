from Sport import *
from Movie import *
from General_Knowledge import *

def Astronemy():
    questions = ("In which spectral region is it possible for astronomers to observethrough clouds?: ",
                 "In kilometers, the earth's average distance from the sun is roughlwhich of the following distances?: ",
                 "Which of the following planets has the lowest density?: ",
                 "Which one of the following planets has no moons?: ",
                 "The atmosphere of Venus contains mostly?: ",

                 )
    options = (("A. visual", "B. radio", "C. ultraviolet", "D. X-ray"),
               ("A. 250 million", "B. 91 million", "C.  150 million", "D. 350 million"),
               ("A. Saturn", "B. Mars", "C. Mercury", "D. Venus"),
               ("A. Mars", "B. Neptune", "C. Venus", "D. Jupiter"),
               ("A. oxygen", "B. carbon dioxide", "C. nitrogen", "D. water"))

    answers = ("D", "C", "A", "C", "B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("-----------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D) ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is correct answer")
        question_num += 1

        print("----------------")
        print("RESULTS")
        print("----------------")

        print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
        print()

        print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
        print()

        # score = int(score / len(questions)* 100)
        # print(f" your score is:{score}%")
        print("you got " + str(score) + "/" + str(len(questions)) + " correct")
        # print("your score is: {score}")
    return True


