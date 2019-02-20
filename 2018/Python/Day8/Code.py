class Node(object):

    def __init__(self, childCount, metadataCount):
        self.childCount = childCount
        self.metadataCount = metadataCount
        self.childs = []
        self.metadata = []

class Day8(object):

    def __init__(self):
        self.root = None

    def create_Tree(self, input):
        index = 0
        root = Node(input[0], input[1])
        
