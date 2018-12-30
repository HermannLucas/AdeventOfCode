import unittest
import Code

class TestDay6(unittest.TestCase):

    def setUp(self):
        self.sut = Code.day6()

    def test_read_instruction(self):

        problem = "Step C must be finished before step A can begin."
        expected_result = ("C", "A")

        self.assertEqual(next(self.sut.read_instructions(problem)), expected_result)

    def test_add_prerequisite(self):

        problem = "Step C must be finished before step A can begin."
        expected_result = {"A": ["C"]}

        self.sut.fill_prerequisites(problem)
        self.assertEqual(self.sut.prerequisites, expected_result)

    def test_example1(self):

        problem = "Step C must be finished before step A can begin., Step C must be finished before step F can begin., Step A must be finished before step B can begin., Step A must be finished before step D can begin., Step B must be finished before step E can begin., Step D must be finished before step E can begin., Step F must be finished before step E can begin."
        expected_result = "CABDFE"

        self.assertEqual(self.sut.problem1(problem), expected_result)

    def test_problem1(self):

        problem = "Step L must be finished before step T can begin., Step B must be finished before step I can begin., Step A must be finished before step T can begin., Step F must be finished before step T can begin., Step D must be finished before step J can begin., Step N must be finished before step R can begin., Step J must be finished before step U can begin., Step C must be finished before step Z can begin., Step V must be finished before step H can begin., Step W must be finished before step H can begin., Step H must be finished before step I can begin., Step R must be finished before step K can begin., Step M must be finished before step X can begin., Step T must be finished before step O can begin., Step Q must be finished before step P can begin., Step I must be finished before step E can begin., Step E must be finished before step Y can begin., Step K must be finished before step Y can begin., Step X must be finished before step O can begin., Step U must be finished before step G can begin., Step Z must be finished before step P can begin., Step O must be finished before step S can begin., Step S must be finished before step G can begin., Step Y must be finished before step G can begin., Step P must be finished before step G can begin., Step C must be finished before step P can begin., Step N must be finished before step K can begin., Step E must be finished before step U can begin., Step C must be finished before step T can begin., Step F must be finished before step I can begin., Step Q must be finished before step Y can begin., Step E must be finished before step S can begin., Step T must be finished before step P can begin., Step K must be finished before step O can begin., Step H must be finished before step Y can begin., Step Q must be finished before step G can begin., Step K must be finished before step P can begin., Step R must be finished before step O can begin., Step W must be finished before step T can begin., Step O must be finished before step P can begin., Step Q must be finished before step X can begin., Step D must be finished before step I can begin., Step R must be finished before step T can begin., Step I must be finished before step K can begin., Step I must be finished before step G can begin., Step K must be finished before step G can begin., Step N must be finished before step U can begin., Step A must be finished before step Y can begin., Step X must be finished before step Y can begin., Step N must be finished before step H can begin., Step R must be finished before step Z can begin., Step C must be finished before step Q can begin., Step F must be finished before step O can begin., Step B must be finished before step Z can begin., Step Z must be finished before step S can begin., Step U must be finished before step S can begin., Step A must be finished before step K can begin., Step B must be finished before step N can begin., Step T must be finished before step E can begin., Step A must be finished before step N can begin., Step F must be finished before step V can begin., Step D must be finished before step C can begin., Step M must be finished before step P can begin., Step D must be finished before step V can begin., Step V must be finished before step Q can begin., Step O must be finished before step Y can begin., Step W must be finished before step I can begin., Step E must be finished before step Z can begin., Step B must be finished before step R can begin., Step C must be finished before step X can begin., Step J must be finished before step T can begin., Step A must be finished before step W can begin., Step Q must be finished before step U can begin., Step I must be finished before step Z can begin., Step N must be finished before step P can begin., Step W must be finished before step U can begin., Step Y must be finished before step P can begin., Step J must be finished before step P can begin., Step F must be finished before step Q can begin., Step L must be finished before step M can begin., Step E must be finished before step G can begin., Step B must be finished before step P can begin., Step H must be finished before step X can begin., Step W must be finished before step S can begin., Step N must be finished before step Q can begin., Step J must be finished before step I can begin., Step L must be finished before step F can begin., Step S must be finished before step Y can begin., Step J must be finished before step X can begin., Step A must be finished before step H can begin., Step T must be finished before step U can begin., Step H must be finished before step Z can begin., Step W must be finished before step R can begin., Step X must be finished before step Z can begin., Step T must be finished before step Y can begin., Step H must be finished before step T can begin., Step K must be finished before step U can begin., Step H must be finished before step G can begin., Step U must be finished before step O can begin., Step W must be finished before step P can begin., Step A must be finished before step D can begin."
        expected_result = "ABDCJLFMNVQWHIRKTEUXOZSYPG"

        self.assertEqual(self.sut.problem1(problem), expected_result)


if __name__ == '__main__':
    unittest.main()
