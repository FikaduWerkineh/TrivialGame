
def General_Knowledge():

    questions = (
     "What is the currency of Qatar?: ",
     "What is the average weight of the human brain?: ",
     "Queen Elizabeth III has been reigning on the British Royal Kingdom as Queen for how many years?: ",
     "Which is the closest planet to earth?: ",
     "What native country is Brazil?: ",
    )

    options = (("A. Pound", "B. Euro", "C. Riyal", "D. Dolar"),
              ("A. 14 g", "B. 2.4 g", "C. 4 kg", "D. 1.4 kg"),
              ("A. 50", "B. 60", "C. 70", "D. 80"),
              ("A. Mars", "B. plto", "C. jupter", "D. satern"),
              ("A. South America", "B. North America", "C. East America", "D. West America"))


    answers = ("C", "C", "B", "C", "B")
    guesses = []
    score = 0
    question_num = 0
    # while True:
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
        score = int(score / len(questions) * 100)
        # print(f" your score is:{score}%")
        print("you got " + str(score) + "/" + str(len(questions)) + " correct")



