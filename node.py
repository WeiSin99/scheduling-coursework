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
        self.successor = successor
        self.nodes_before = nodes_before
        self.processing = processing
        self.due = due
    
    def edge(self, to_node):
        """Creates the edge between two nodes (vertices) and adds them as part of the graph.
        Args:
            to_node(Node): the end node for the edge"""
        self.nodes_after.append(to_node.name)
        to_node.nodes_before.append(self)

    def __repr__(self):
        return str({"name": self.name, "successor": self.successor})

    def __str__(self):
        return str({"name": self.name, "successor": self.successor})

    def __dir__(self):
        return {"name": self.name, "successor": self.successor}
