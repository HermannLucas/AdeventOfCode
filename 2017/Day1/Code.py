class circular_sum(object):

    def calculate(self, problem):

        total = 0

        problem.append(problem[0])
        problem.reverse()

        while len(problem) > 1:

            value = problem.pop()
            if value == problem[-1]:

                total += value

        return total

    def calculate_second(self, problem):

        first_half = problem[:len(problem)//2]
        second_half = problem[len(problem)//2:]

        return sum([element * 2 for \
                    element, second_element \
                    in zip(first_half, second_half) \
                    if element == second_element])
