"""
The Decision Tree module contains any method required to
develop this Machine Learning model in a eager, supervised
learning fashion.
"""
from node import Node


class Graph:

    def __init__(self):
        """Initialisation of Graph class object parameters.
        graph_dict (dict): dictionary with key = node.name (str) and value = node (object).
        """
        self.graph_dict = {} # all nodes in the graph


    def build_graph(self,incidence_list):
        """Takes the incidence matrix and builds the DAG.
        
        Args:
            incidence_list: 
            - a list of len(n), where n = number of edges
            - each element: a list of [from_node's name (str), to_node's name (str)]
        """
        for pair in incidence_list:
            from_node = pair[0]
            to_node = pair[1]
            # Check if the "from node" is created
            if from_node not in self.graph_dict:
                # If not, create the node 
                Node1 = Node(from_node,[],[],None,None)
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
            Node1.successor.append(Node2.name)
            Node2.nodes_before.append(Node1.name)
        
    def assign_due_dates(self, due_dates):
        """
        Assign due dates to each node in the graph

        Args:
            due_dates:
            - a dictionary with key value pair of { indexed_job_name: due_date }
        """
        for name, node in self.graph_dict.items():
            node.due = due_dates[name]
    
    def assign_processing_time(self,processing_time):
        """
        Assign processing time to each node in the graph

        Args:
            processing_time:
            - a dictionary with key value pair of { job_name: processing_time }
        """
        for name, node in self.graph_dict.items():
            name_without_index = name.split('_')[0]
            node.processing = processing_time[name_without_index]

    def no_of_successors(self):
        """Returns a dictionary of the number of successors n corresponding to a node

        Returns:
            n(dict): key = node name ; value = number of successors corresponding to the node
        """
        n = dict()
        for node in self.graph_dict.values():
            n[node.name] = len(node.successor)

        return n
