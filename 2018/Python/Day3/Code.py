import re

class day3(object):

    def __init__(self):
        self.used_cells = {}
        self.ids = []

    def read_claim(self, claim):
        return re.match(r'#(.*) @ (.*),(.*): (.*)x(.*)', claim)

    def add_claim(self, claim):
        pattern = self.read_claim(claim)
        self.ids.append(pattern.group(1))
        for y in range(int(pattern.group(3)), int(pattern.group(3)) + int(pattern.group(5))):
            for x in range(int(pattern.group(2)), int(pattern.group(2)) + int(pattern.group(4))):
                if (x,y) in self.used_cells.keys():
                    self.used_cells[(x, y)][0] += 1
                    self.used_cells[(x, y)][1].append(pattern.group(1))
                else:
                    self.used_cells[(x, y)] = [1, [pattern.group(1)]]

    def problem1(self, claims):
        for claim in claims.split(", "):
            self.add_claim(claim)
        return sum([1 for cell in self.used_cells.values() if cell[0] > 1])

    def is_overlap(self, id):
        for cell in self.used_cells.values():
            if id in cell[1] and len(cell[1]) > 1:
                return True
        return False

    def problem2(self, claims):
        self.problem1(claims)
        for id in self.ids:
            if not self.is_overlap(id):
                return id
