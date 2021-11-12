from graph import Graph
from data import read_due_dates, read_input, read_init_schedule, write_schedule_to_csv
from tabu_algorithm import Tabu
from copy import deepcopy

# Job Processing Times (from running gettimes.py)
p = {"vii":21.1218, "emboss":1.9645, "blur":6.0954, "wave":17.5761, "muse":13.2213, "night":25.7214, "onnx":5.8572}

# Obtain the data required to build the DAG
# (i) Incidence List
incidence_list = read_input('data/input.json')
# (ii) Due Dates
due_dates = read_due_dates('data/input.json')

# Build the DAG
graph = Graph()
graph.build_graph(incidence_list)
graph.assign_due_dates(due_dates)
graph.assign_processing_time(p)
node_dictionary = graph.graph_dict

# Initial schedule (sinit.json)
init_schedule = read_init_schedule('data/tabu/sinit.json')
jobs_in_init_order = [node_dictionary[job] for job in init_schedule]

# Run Tabu Search
# (i) K = 10
print('1. K=10')
solution_10, tabu_tardiness_10 = Tabu(jobs_in_init_order, threshold=30, K=10, L=5)
print('Tabu Schedule: ', solution_10)
print('Tabu Total Tardiness: ', tabu_tardiness_10)
write_schedule_to_csv('data/tabu/tabu_10.csv', solution_10)
print()

# (ii) K = 100
print('2. K=100')
solution_100, tabu_tardiness_100 = Tabu(jobs_in_init_order, threshold=30, K=100, L=5)
print('Tabu Schedule: ', solution_100)
print('Tabu Total Tardiness: ', tabu_tardiness_100)
write_schedule_to_csv('data/tabu/tabu_100.csv', solution_100)
print()

# (iii) K = 1000
print('3. K=1000')
solution_1000, tabu_tardiness_1000 = Tabu(jobs_in_init_order, threshold=30, K=1000, L=5)
print('Tabu Schedule: ', solution_1000)
print('Tabu Total Tardiness: ', tabu_tardiness_1000)
write_schedule_to_csv('data/tabu/tabu_1000.csv', solution_1000)
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
