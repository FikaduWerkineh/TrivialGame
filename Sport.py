

def Spoort():
    questions = ("What is the National Sports of Brazil?: ",
                 "Who won the FIFA World Cup in 2018?: ",
                 "What is the 100m World Record of Usain Bolt?: ",
                 "What is the National Game of the USA?: ",
                 "Which Country Won the most FIFA World Cups?: ")
    options = (("A. Football", "B. Pato", "C. Capoeira", "D.  Oina"),
               ("A. Argentina", "B. France", "C. Italy", "D. Brazil"),
               ("A. 14.35 Sec", "B. 9.58 Sec", "C. 9.05 Sec", "D. 10.12 Sec"),
               ("A. Tennis", "B. Soccer", "C. Baseball", "D. Basket Ball"),
               ("A. Germany", "B. Argentina", "C.  Brazil", "D. France"))

    # def new_game():

    answers = ("C", "B", "B", "C", "C")
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
        # score = int(score / len(questions) * 100)
        print("you got " + str(score) + "/" + str(len(questions)) + " correct")
    return True






