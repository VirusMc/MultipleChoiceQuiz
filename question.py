import json
import os
from enum import Enum
import random as r
from typing import List


class Category(Enum):
    NONE = 0
    CASUAL = 1
    HISTORY = 2
    SCIENCE = 3


class Question:

    def __init__(self, name: str = "", question: str = "", answers=None, correctAnswer: str = "",
                 category: Category = Category.NONE):

        if answers is None:
            answers = [""]
        self.name = name
        self.question = question
        self.answers = answers
        if correctAnswer in answers:
            self.correctAnswer = correctAnswer
        else:
            raise NameError(correctAnswer + " nicht in den Antwortmöglichkeiten enthalten!!!")
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "question": self.question,
            "answers": self.answers,
            "correctAnswer": self.correctAnswer,
            "category": self.category.value
        }

    def from_dict(self, dictionary: dict):
        self.name = dictionary["name"]
        self.question = dictionary["question"]
        self.answers = dictionary["answers"]
        if dictionary["correctAnswer"] in self.answers:
            self.correctAnswer = dictionary["correctAnswer"]
        else:
            raise NameError("Antwort nicht in den Antwortmöglichkeiten enthalten!!!")
        self.category = Category(dictionary["category"])

    def save(self, fileName: str = "question"):
        filePath = os.path.join(os.getcwd(), "./questions/")
        fileUrl = filePath + fileName + ".json"
        if not os.path.exists(filePath):
            os.mkdir(filePath)
        json.dump(self.to_dict(), open(fileUrl, "w", encoding="utf-8"))

    def load(self, fileName: str = "question"):
        fileUrl = "./questions/" + fileName + ".json"
        self.from_dict(json.load(open(fileUrl, encoding="utf-8")))
        return self

    def ask(self):
        print("---" + self.name + "---")
        print(self.question)
        r.shuffle(self.answers)
        for a in range(len(self.answers)):
            answer = self.answers[a]
            print(str(a + 1) + " - " + answer)
        inp = int(input("Welche Nummer ist die richtige Antwort?\n"))

        if (inp - 1) == self.answers.index(self.correctAnswer):
            print("Richtig\n")
            return True
        else:
            print("Leider Falsch :(\n")
            return False
