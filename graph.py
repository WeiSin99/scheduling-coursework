"""
The Graph module contains methods required to build a Directed Acrylic Graph that describes the workflow.
"""
from node import Node


class Graph:

    def __init__(self):
        """
        Initialisation of Graph class object parameters.
        - graph_dict (dict): dictionary to all nodes within the graph, with:
            key = node.name (str),
            value = node (object)
        """
        self.graph_dict = {} 

    def build_graph(self,incidence_list):
        """
        Takes an incidence matrix and builds the DAG.
        
        Args:
            incidence_list (list):
            - len(n), where n = number of edges
            - each element: a list of incidence pairs [from_node's name (str), to_node's name (str)]
        """
        for index,pair in enumerate(incidence_list):
            from_node = pair[0]
            to_node = pair[1]
            # Check if the "from node" is created
            if from_node not in self.graph_dict:
                # If not, create the node 
                Node1 = Node(from_node,[],[],None,None)
                Node1.job_number=index
                # Add node to the graph
                self.graph_dict[from_node] = Node1
            else:
                Node1 = self.graph_dict[from_node]

            # Check if the "to node" is created
            if to_node not in self.graph_dict:
                # If not, create the node 
                Node2 = Node(to_node,[],[],None,None)
                # Add node to the graph
                self.graph_dict[to_node] = Node2
            else:
                Node2 = self.graph_dict[to_node]

            # Link the two nodes
            Node1.successor.append(Node2)
            Node2.nodes_before.append(Node1)
        
        # Assign node.n - the number of successors each node has.
        self.assign_n()
        # Identify the start and end nodes in the graph.
        self.find_start_end()
        
    def assign_due_dates(self, due_dates):
        """
        Assign due dates to each node object in the graph. 
        Obtained via node.due (int).

        Args: 
            due_dates (dict): a dictionary of due dates with key = job name (str), value = due date (int).
        """
        for name, node in self.graph_dict.items():
            node.due = due_dates[name]
    
    def assign_processing_time(self,processing_time):
        """
        Assign processing time to each node object in the graph.
        Obtained via node.processing (float).

        Args:
            processing_time (dict): a dictionary of processing times with key = job name (str), value = processing_time (float).
        """
        for name, node in self.graph_dict.items():
            name_without_index = name.split('_')[0]
            node.processing = processing_time[name_without_index]

    def assign_n(self):
        """
        Assign the number of successors belonging to a particular node to each node object (node.n). 
        Obtained via node.n (int).
        EG. if a node has 3 successors, n = 3.
        """
        for node in self.graph_dict.values():
            node.n = len(node.successor)
            if node.n == 0:
                node.end = True

    def find_start_end(self):
        """
        Identify and assign the start and end nodes of the graph.
        """
        for node in self.graph_dict.values():
            if node.nodes_before == []:
                node.start = True

            if node.n == 0:
                node.end = True
                node.job_number = len(self.graph_dict) -1

