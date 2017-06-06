from random import shuffle
class Question():
    def __init__(self,qstring):
        lines = qstring.replace("\n\n","\n").split("\n")
        self.query = ", ".join(lines[0].split(", ")[1:])
        self.correct = ",".join(lines[1].split(",")[1:])
        self.wrong = set()
        for line in lines[2:]:
            self.wrong.add(",".join(line.split(",")[1:]))
            #print "|" + line + "|"
    def showQuestion(self):
        self.choices = list(self.wrong)
        self.choices.append(self.correct)
        shuffle(self.choices)
        print self.query
        for index, answer in enumerate(self.choices):
            print chr(65+index) + ". " + answer
    def isValid(self,ans):
        try:
            idx = ord(ans.upper())-65
            return idx in range(5)
        except TypeError:
            return False
    def isCorrect(self,ans):
        idx = ord(ans.upper())-65
        return self.choices[idx] == self.correct