import re

class day6(object):

    def __init__(self):
        self.steps = set()
        self.prerequisites = {}

    def read_instructions(self, instructions):
        for instruction in instructions.split(", "):
            match = re.match(r'Step (.*) must be finished before step (.*) can begin.', instruction)
            yield (match.group(1), match.group(2))

    def fill_prerequisites(self, instructions):
        for require, action in self.read_instructions(instructions):
            self.steps.add(action)
            self.steps.add(require)
            try:
                self.prerequisites[action].append(require)
            except:
                self.prerequisites[action] = [require]

    def is_available(self, step_list, step):
        for prerequisite in self.prerequisites[step]:
            if prerequisite not in step_list:
                return False
        return True

    def problem1(self, instructions):
        self.fill_prerequisites(instructions)
        step_list = []
        self.steps = sorted(list(self.steps))
        while self.steps:
            for step in self.steps:
                if step not in self.prerequisites.keys() or self.is_available(step_list, step):
                    step_list.append(step)
                    self.steps.remove(step)
                    break
        return "".join(step_list)
