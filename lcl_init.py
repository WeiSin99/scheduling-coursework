from graph import Graph
from data import read_due_dates, read_input, write_schedule_to_csv
from lcl_algorithm import LCL, total_tardiness, get_cmax
from copy import deepcopy

# Job Processing Times
# Values taken from running gettimes.py
p = {"vii":21.1218, "emboss":1.9645, "blur":6.0954, "wave":17.5761, "muse":13.2213, "night":25.7214, "onnx":5.8572}
Cmax = get_cmax('data/input.json', p)

# Obtain the data required to build the DAG
# (i) Incidence List
incidence_list = read_input('data/input.json')
# (ii) Due Dates
due_dates = read_due_dates('data/input.json')

source_file = open('lcl_log.txt', 'w')

# Build the DAG
graph = Graph()
graph.build_graph(incidence_list)
graph.assign_due_dates(due_dates)
graph.assign_processing_time(p)
node_dictionary = graph.graph_dict

# Least Cost Last Algorithm
V = deepcopy(node_dictionary)
LCL_schedule, Tmax = LCL(V, Cmax)
# LCL Schedule
print('LCL Schedule: ', LCL_schedule, file = source_file)
# Convert to csv
write_schedule_to_csv('data/lcl/lcl.csv', LCL_schedule)
# Max Tardiness
print('LCL Max Tardiness: ', Tmax, file = source_file)
# LCL Total Tardiness
print('LCL Total Tardiness: ',total_tardiness(LCL_schedule), file = source_file)

source_file.close()
