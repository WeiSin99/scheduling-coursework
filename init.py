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
print()

# Question 3 & 4 - Tabu Algorithm
# Obtain initial schedule for sinit.json
init_schedule = read_init_schedule('sinit.json')
jobs_in_init_order = [node_dictionary[job] for job in init_schedule]

# # Run Tabu Search
# (i) K = 10
print('1. K=10')
solution_10, tabu_tardiness_10 = Tabu(jobs_in_init_order, threshold=30, K=10, L=5)
print('Tabu Schedule: ', solution_10)
print('Tabu Total Tardiness: ', tabu_tardiness_10)
print()

# (ii) K = 100
print('2. K=100')
solution_100, tabu_tardiness_100 = Tabu(jobs_in_init_order, threshold=30, K=100, L=5)
print('Tabu Schedule: ', solution_100)
print('Tabu Total Tardiness: ', tabu_tardiness_100)
print()

# (iii) K = 1000
print('3. K=1000')
solution_1000, tabu_tardiness_1000 = Tabu(jobs_in_init_order, threshold=30, K=1000, L=5)
print('Tabu Schedule: ', solution_1000)
print('Tabu Total Tardiness: ', tabu_tardiness_1000)
print()

# # (iv) Extra: Finding best Tabu Search Parameters for best schedule
# # Initialise variables to store best parameters and performance outcome.
# min_tardiness = float("inf")
# threshold_best = None
# L_best = None
# schedule_best = None
# i = 3
# for i in range (30):
#     for l in range (5,7):
#         solution_1000, tabu_tardiness_1000 = Tabu(jobs_in_init_order, threshold=i, K=1000, L=l)
#         if tabu_tardiness_1000 < min_tardiness:
#             min_tardiness = tabu_tardiness_1000
#             schedule_best = solution_1000
#             threshold_best = i
#             L_best = l

# print (f'Parameter Optimisation for K = 1000: (i) Best Threshold = {threshold_best}, (ii) Best L = {L_best}') # Threshold = 3, L = 6
# print ('Best Schedule: ', schedule_best) 
# print ('Min tardiness: ', min_tardiness) # Min Tardiness = 2498.5

# (v) LCL Total Tardiness
print('5. LCL Total Tardiness: ',total_tardiness(LCL_schedule))



