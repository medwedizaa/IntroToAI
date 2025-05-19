class Node:
    def __Init__(self, nodes, value):
        self.nodes = nodes
        self.value = value

    def compute_node_value(self):
        s = 0
        for i in self.nodes:
            s = s + i.value
        return s