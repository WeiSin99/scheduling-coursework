"""
The Node object implementation. Nodes are used to represent jobs in the workflow. 
These are implemented in graph.py to build the Directed Acrylic Graph (DAG).
"""
class Node:

    def __init__(self, name, successor, nodes_before, processing, due):
        """Initialisation of Node object parameters.
        - name (str): eg. onnx_1, muse_1, emboss_1 etc
        - job number (int): node number following python-like format (appendix A.1)
        - successor (list): a list of the current node's immediate successors (node objects)
        - n (int): the number of immediate successors the current node has = len(successor)
        - nodes_before (list): a list of the current node's immediate predecessors (node objects)
        - processing (float): processing time for the current node
        - due (int): due date for the current node
        - end (bool): true if the current node is the end node in the DAG.
        - start (bool): true if the current node is the start node in the DAG.
        """
        self.name = name
        self.job_number = None
        self.successor = successor
        self.n = 0
        self.nodes_before = nodes_before
        self.processing = processing
        self.due = due
        self.end = False
        self.start = False 

    def __repr__(self):
        return self.name

    def __str__(self):
        return str({"name": self.name, "job number": self.job_number, \
            "processing time": self.processing, "due date": self.due, \
            "nodes before": [node.name for node in self.nodes_before], \
            "successor": [node.name for node in self.successor], \
            "n": self.n, "end":self.end, "start":self.start})
