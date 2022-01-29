from collections import Counter
import json
import re


class Tokenizer:

    def __init__(self, text):
        self.text = text
        self.divide = []
        self.matrix = []
        self.phrase = []

    def separate_sentence(self):
        self.phrase = re.split("[.?!]", self.text.lower())
        for sentence in self.phrase:
            if sentence == "":
                self.phrase.remove(sentence)

    def separate(self):
        with open("./stopword.json") as f:
            stopwords = json.load(f)
        for sentence in self.phrase:
            self.divide.append(re.split("[,:;'() ]", sentence))

        for i in range(len(self.divide)):
            for words in stopwords:
                for word in self.divide[i]:
                    if word == words or word == "":
                        self.divide[i].remove(word)

    def count_word(self):
        lil_matrix = []
        repeat_list = []
        for i in range(len(self.divide)):
            repeat = Counter(self.divide[i])
            repeat_list.append(repeat)

        for repeat_word in repeat_list:
            for word in repeat_word:
                lil_matrix.append(repeat_word[word])
            self.matrix.append(lil_matrix)
            lil_matrix = []

    def show(self):
        print(self.divide)
        print(self.matrix)


ph = "Test test test, inutile donc indispensable. Oui mais non (ou peut-être)? Ceci me surprend veuillez arrêtez cette supercherie, je vous en remercie."
ph1 = Tokenizer(ph)
ph1.separate_sentence()
ph1.separate()
ph1.count_word()
ph1.show()
