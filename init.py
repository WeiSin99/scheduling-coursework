from graph import Graph
from data import read_due_dates, read_input, get_cmax

# Question 1 - Job Processing Times
# Values taken from running gettimes.py
p = {"vii":19.1064, "emboss":1.9528, "blur":6.0336, "wave":15.0447, "muse":10.9786, "night":22.9632, "onnx":5.6957}
Cmax = get_cmax(p)

# Question 2 - Least Cost Last Algorithm
incidence_list = read_input()
due_dates = read_due_dates()

graph = Graph()
graph.build_graph(incidence_list)
graph.assign_due_dates(due_dates)
graph.assign_processing_time(p)
n = graph.no_of_successors()
V = graph.graph_dict

# Initialise
S = [0]*(len(n)) # Schedule
p_assigned = 0 # Total processing times of all jobs already in the schedule S
for k in range(len(n)-1,-1,-1):
    # At each iteration, 
    Tj_min_node = None # Used to store node with minimum tardiness
    Tj_min = Cmax # Used to track the minimum tardiness
    for node_name, value in n.items():
        # Find the node that has no immediate successors (nj = 0)
        if value == 0:
            # Calculate Tardiness
            Cj = Cmax - p_assigned
            Tj = max(0, Cj - V[node_name].due)

            # Find the node that yields the minimum tardiness
            if Tj<Tj_min:
                Tj_min = Tj
                Tj_min_node = node_name
    
    # Add the node with the minimum tardiness as the kth job
    S[k] = Tj_min_node
    # Sum up its processing time for the next k
    p_assigned += V[Tj_min_node].processing

    # For all jobs that have Tj_min_node as its immediate successor
    for nodes in V[Tj_min_node].nodes_before:
        # Reduce their n value
        n[nodes] -= 1
    
    # Remove Tj_min_node from n
    del n[Tj_min_node]

print(S)


