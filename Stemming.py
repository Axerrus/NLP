a = ["porter", "pomme", "portez", "fermer", "paumer", "chevaux", "maux", "michel", "cheveux", "meubles"]


class Stemming:

    def __init__(self, nom):
        self.nom = list(nom)
        self.filtre1 = ["er", "e", "es", "ons", "ont", "ez"]
        self.filtre2 = ["aux"]
        self.filtre3 = ["s", "x"]
        self.stem = self.nom

    def stemming(self):

        # -----STEMMING-----

        for word in self.nom:
            i = self.nom.index(word)

            # Step 1
            for end in self.filtre1:
                if word[-len(end):] == end:
                    self.stem[i] = (word[:-len(end)])

            # Step 2
            for end in self.filtre2:
                if word[-len(end):] == end:
                    self.stem[i] = (word[:-len(end)])

            # Step 3
            for end in self.filtre3:
                if word[-len(end)] == end:
                    self.stem[i] = (word[:-len(end)])


test = Stemming(a)
test.stemming()
print(test.stem)
