class spreadsheet_checksum(object):

    def difference_line(self, line):

        line = sorted(line)

        return line[-1] - line[0]

    def get_checksum(self, problem, part):

        total = 0

        if part == 1 :
            for line in problem:

                total += self.difference_line(line)

            return total

        elif part == 2:

            for line in problem:
                total += self.evenly_divsible_line(line)

            return total
        else:
            return "what ?"


    def evenly_divsible_line(self, line):

        while len(line) > 1:

            value = line.pop()

            for element in line:
                if element > value:

                    if element % value == 0:
                        print(element // value)
                        return element // value

                else:

                    if value % element == 0:
                        print(value // element)
                        return value // element
