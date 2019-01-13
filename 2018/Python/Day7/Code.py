import re
from collections import deque

class Worker(object):

    def __init__(self, parent):
        self.parent = parent
        self.instruction = None

    def update(self):
        if self.instruction:
            self.instruction.update()
        else:
            if len(self.parent.ready_queue) > 0:
                self.add_instruction(self.parent.next_instruction())
                try:
                    self.instruction.update()
                except:
                    pass

    def add_instruction(self, name):
        self.instruction = Instruction(name, self)

    def done_instruction(self, name):
        self.instruction = None
        self.parent.work_done(name)

class Instruction(object):

    def __init__(self, name, parent):
        self.name = name
        # self.time = 60 + (ord(name) %64)
        self.time = 60 + (ord(name) - ord('a'))
        self.parent = parent

    def work(self):
        self.time -= 1

    def finished(self):
        self.parent.done_instruction(self.name)

    def update(self):
        self.work()
        if self.time == 0:
            self.finished()

class day6(object):

    def __init__(self):
        self.steps = set()
        self.prerequisites = {}
        self.dependants = {}

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

    def fill_dependants(self, instructions):
        for action, next in self.read_instructions(instructions):
            self.steps.add(action)
            self.steps.add(next)
            try:
                self.dependants[action].append(next)
            except:
                self.dependants[action] = [next]

    def problem2(self, instructions, workers):
        self.fill_prerequisites(instructions)
        instruction_count = len(self.steps)
        time = 1
        self.ready_queue = deque([step for step in self.steps if step not in self.prerequisites.keys()])
        self.done_list = []
        self.steps = sorted(list(self.steps))
        workers = [Worker(self) for _ in range(workers)]
        while len(self.done_list) < instruction_count:
            time += 1
            for worker in workers:
                worker.update()
        return time

    def work_done(self, instruction):
        self.done_list.append(instruction)
        try:
            del self.prerequisites[instruction]
        except:
            pass
        finally:
            self.update_ready_queue()

    def next_instruction(self):
        try:
            return self.ready_queue.popleft()
        except:
            return None

    def update_ready_queue(self):
        for instruction in self.prerequisites.keys():
            for prerequisite in self.prerequisites[instruction]:
                if prerequisite not in self.done_list:
                    continue
            self.ready_queue.append(instruction)

    # def add_action(self, slice, action)
    # def alternate_prob1(self, instructions):
    #     result = []
    #     for predecessor, action in self.read_instructions(instructions):
    #         if predecessor in result:
    #             try:
