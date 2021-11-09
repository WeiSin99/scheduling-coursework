"""
The Node object implementation.
"""


class Node:

    def __init__(self, name, successor, nodes_before, processing, due):
        """Initialisation of TreeNode object parameters.
        - name (str): eg. onnx_1, muse_1, emboss_1 etc.
        - value (int): node number (EG. 0 for Node 0, according to the incidence matrix)
        - nodes_after (list): a list of nodes containing the element's immediate successors.
        - processing (float): processing time for the filter
        - due (int): due date for the filter
        """
        self.name = name
        self.job_number = None
        self.successor = successor
        self.nodes_before = nodes_before
        self.processing = processing
        self.due = due
        self.n = 0
        self.end = False
        self.start = False 
    
    def edge(self, to_node):
        """Creates the edge between two nodes (vertices) and adds them as part of the graph.
        Args:
            to_node(Node): the end node for the edge"""
        self.nodes_after.append(to_node.name)
        to_node.nodes_before.append(self)

    def __repr__(self):
        return self.name

    def __str__(self):
        return str({"name": self.name, "job number": self.job_number, \
            "processing time": self.processing, "due date": self.due, \
            "nodes before": [node.name for node in self.nodes_before], \
            "successor": [node.name for node in self.successor], \
            "n": self.n, "end":self.end, "start":self.start})