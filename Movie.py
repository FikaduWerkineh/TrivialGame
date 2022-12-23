



def Moviei():
    questions = (
        "In which Hollywood movie did the actor Bill Paxton portray the role of Fred Haise? : ",
        "In 2016, Game of Thrones resurrected which famous and popular character? : ",
        "Who actually drew the sketch of Rose in Titanic?: ",
        "What is the highest-grossing movie of all time?: ",
        "The code in The Matrix comes from what food recipes?: "
    )

    options = (("A. Apollo 11", "B. Matrix", "C. Gladiator", "D. Solo"),
               ("A. Jon Snow", "B. Bad Snow", "C. Oliver Snow", "D. Wiliam Snow"),
               ("A. Leonardo DiCaprio", "B. Billy Zane", "C. James Cameron", "D.  Kathy Bates"),
               ("A. Titanic", "B. Avatar", "C. Avengers: Endgame", "D. Star Wars: The Force Awakens"),
               ("A. Sushi recipes", "B. Dumpling recipes ", "C. Stir-fry recipes", "D. Pad thai recipes"))

    answers = ("A", "A", "C", "A", "D")
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
        # score = int(score / len(questions)* 100)
        print("you got " + str(score) + "/" + str(len(questions)) + " correct")
    return 1