from graph import Graph
from data import read_due_dates, read_input, get_cmax, read_init_schedule
from algorithm import LCL, lexi_order_and_prec, Tabu, total_tardiness, check_prec
from pprint import pprint
from copy import deepcopy

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
node_dictionary = graph.graph_dict

# Least Cost Last Algorithm Schedule
V = deepcopy(node_dictionary)
LCL_schedule, Tmax = LCL(V, Cmax)
print('LCL Schedule: ', LCL_schedule)
print('LCL Max Tardiness: ', Tmax)

# Question 3 & 4 - Tabu Algorithm
# Obtain initial schedule for sinit.json
init_schedule = read_init_schedule('sinit.json')
jobs_in_init_order = [node_dictionary[job] for job in init_schedule]

# # Run Tabu Search
# # (i) K = 10
# print('1. K=10')
# solution, tabu_tardiness = Tabu(jobs_in_init_order, threshold=30, K=10, L=5)
# print('Tabu Schedule: ', solution)
# print('Tabu Total Tardiness: ', tabu_tardiness)
# print()

# (ii) K = 100
print('1. K=100')
solution, tabu_tardiness = Tabu(jobs_in_init_order, threshold=20, K=100, L=10)
print('Tabu Schedule: ', solution)
print('Tabu Total Tardiness: ', tabu_tardiness)
print()

# # (iii) K = 1000
# print('1. K=1000')
# solution, tabu_tardiness = Tabu(jobs_in_init_order, threshold=30, K=1000, L=5)
# print('Tabu Schedule: ', solution)
# print('Tabu Total Tardiness: ', tabu_tardiness)
# print()

# # (iv) LCL Total Tardiness
# print('4. LCL Total Tardiness: ',total_tardiness(LCL_schedule))

# test_schedule = ['onnx_8', 'onnx_7', 'muse_3', 'emboss_8', 'onnx_5', 'onnx_4', 'wave_5', 'emboss_6', 'emboss_5', 'wave_6']
# test = [node_dictionary[job] for job in test_schedule]
# _, swap_list = lexi_order_and_prec(test)
# print(swap_list)