class day2(object):

    def __init__(self):
        self.double = 0
        self.triple = 0


    def count_letters(self, input):
        letters = {}
        for letter in input:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        return(letters)

    def problem1(self, input):
        self.double = self.triple = 0

        for line in input.split(", "):
            letters = self.count_letters(line).values()
            if 2 in letters:
                self.double += 1
            if 3 in letters:
                self.triple += 1

        return self.double * self.triple

    def compare_ids(self, id, ref):
        return sum([1 if letter != ref[index] else 0 for index, letter in enumerate(id)])

    def problem2(self, input):
        input = input.split(", ")
        while True:
            id = input.pop(0)
            for element in input:
                if self.compare_ids(id, element) == 1:
                    return "".join([a if a == b else "" for a, b in zip(id, element)])
