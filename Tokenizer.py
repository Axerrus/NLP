from collections import Counter
import json
import re


class Tokenizer:

    def __init__(self, phrase):
        self.phrase = phrase
        self.divide = []
        self.matrix = []

    def separate(self):
        with open("./stopword.json") as f:
            stopwords = json.load(f)

        self.divide = re.split("[.,?:;'() ]", self.phrase.lower())

        for word in stopwords:
            for word2 in self.divide:
                if word == word2 or word2 == '':
                    self.divide.remove(word2)

    def count_word(self):
        lil_matrix = []
        occurences = Counter(self.divide)
        for word in occurences.keys():
            lil_matrix.append(occurences[word])
        self.matrix.append(lil_matrix)

    def show(self):
        print(self.divide)
        print(self.matrix)


ph = "Mais pourqoui voulez-vous faire cela ? Je n'est jamais voulu faire parti de cette experience ni de cette interaction (test parathese). Je veux manger un tacos, mais, je n'est pas d'argent. On verra bien si le père Noel exist. Je veux manger japonais."
ph1 = Tokenizer(ph)
ph1.separate()
ph1.count_word()
ph1.show()
