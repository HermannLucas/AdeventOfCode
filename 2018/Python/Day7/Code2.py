from collections import defaultdict, deque
import re

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.depth = defaultdict(int)
        self.events = []
        self.queue = []
        self.time = 0
        self.worker = 0

    def addWorkers(self, workers):
        self.workers = workers

    def addEdge(self, instruction, next):
        self.edges[instruction].append(next)
        self.depth[next] += 1

    def add_task(self, task):
        self.queue.append(task)

    def sortEdges(self):
        for key in self.edges:
            self.edges[key] = sorted(self.edges[key])

    def start_work(self):
        while len(self.events) < self.workers and self.queue:
            task = min(self.queue)
            self.queue = [edge for edge in self.queue if edge != task]
            print("Starting {} at {}.".format(task, self.time))
            self.events.append((self.time + 60 + ord(task) % 64, task))

    def initialiseQueue(self):
        for instruction in self.edges.keys():
            if not self.depth[instruction]:
                print(instruction)
                self.add_task(instruction)


class Day7:

    def __init__(self):
        self.graph = Graph()

    def read_instructions(self, instructions):
        for instruction in instructions.split(", "):
            match = re.match(r'Step (.*) must be finished before step (.*) can begin.', instruction)
            yield (match.group(1), match.group(2))

    def problem2(self, instructions, workers):
        self.graph.addWorkers(workers)
        for instruction, next in self.read_instructions(instructions):
            self.graph.addEdge(instruction, next)

        self.graph.sortEdges()
        self.graph.initialiseQueue()
        self.graph.start_work()

        while self.graph.events or self.graph.queue:
            self.graph.time, instruction = min(self.graph.events)
            print("Time: {}, instruction: {}".format(self.graph.time, instruction))
            self.graph.events = [event for event in self.graph.events if event != (self.graph.time, instruction)]
            for subinstruction in self.graph.edges[instruction]:
                self.graph.depth[subinstruction] -= 1
                if not self.graph.depth[subinstruction]:
                    self.graph.add_task(subinstruction)
            self.graph.start_work()

        return self.graph.time
