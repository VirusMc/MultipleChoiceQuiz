import random as r

from question import Question


def fillValidQuestions():
    valid = []
    with open("./valid_questions.valid") as file:
        for f in file.readlines():
            valid.append(f.strip("\n"))
    return valid


def game(validQ):
    score: int = 0
    for q in range(questionCount):
        randomQuestionIndex = r.randint(0, len(validQ) - 1)

        success = Question().load(validQ[randomQuestionIndex]).ask()

        if success:
            score += 1

        validQ.remove(validQ[randomQuestionIndex])
    print("Punktezahl: " + str(score) + "/" + str(questionCount))
    input("Drücke Enter um das Spiel zu beenden!")


if __name__ == '__main__':
    print("Willkommen zum Multiple-Choice Quiz!\n")
    questionCount = int(input("Wie viele Fragen sollen gestellt werden? "))

    validQuestions = fillValidQuestions()

    if questionCount > len(validQuestions):
        print("So viele Fragen gibt es nicht.\nEs werden alle Fragen abgefragt!\n")
        questionCount = len(validQuestions)

    game(validQuestions)
