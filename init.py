from graph import Graph
from data import read_due_dates, read_input, get_cmax
from algorithm import LCL
from pprint import pprint

# Question 1 - Job Processing Times
# Values taken from running gettimes.py
p = {"vii":19.1064, "emboss":1.9528, "blur":6.0336, "wave":15.0447, "muse":10.9786, "night":22.9632, "onnx":5.6957}
Cmax = get_cmax('input.json', p)

# Question 2 - Least Cost Last Algorithm
# Obtain the data required to build the DAG
# (i) Incidence List
incidence_list = read_input('input.json')
# (ii) Due Dates
due_dates = read_due_dates('input.json')

# Build the DAG
graph = Graph()
graph.build_graph(incidence_list)
graph.assign_due_dates(due_dates)
graph.assign_processing_time(p)
graph.assign_n()
V = graph.graph_dict

# Get the schedule following Least Cost Last Algorithm
S, Tmax = LCL(V, Cmax)
print(Tmax)
print(S)


