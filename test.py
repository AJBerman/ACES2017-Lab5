from question import Question
import numpy as np
with file("testbank.txt") as f:
    text = "\n".join(f.readlines()).split("\n\n \n\n")
    questions = [Question(t) for t in text]
    questions = np.random.choice(questions, replace=False, size=25)
    score = 0
    for question in questions:
        question.showQuestion()
        temp = "T"
        while not question.isValid(temp):
            temp = raw_input("Please enter an answer (e.g. A, B, etc.):")
            if not question.isValid(temp):
                print "Not a valid answer. please try again!"
                question.showQuestion()
        if question.isCorrect(temp):
            score += 1
            print "You got it right!"
        else:
            print "Sorry, wrong answer."
    print "Thanks for taking our test! Your score was " + str(score)