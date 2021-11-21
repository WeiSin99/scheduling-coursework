Code Execution Instructions

Run the following command to execute the code:

1. cd into the project directory with: `cd scheduling-coursework`
2. Run the tabu search algorithm with the following commands: `python3 tabu_init.py`
3. To see intermediate results printed in the terminal, uncomment the print statements in the Tabu() method in tabu_algorithm.py.

Consists of two main parts:

1. tabu_algorithm.py
  Consists of the main implementation of tabu search algorithm and some other helper functions
  1. Tabu - Implementation of tabu search algorithm
  2. check_prec - Checks if a given schedule is acceptable following the order of precedence
  3. lexi_order_and_prec - Returns the possible schedule candidates for tabu search sorted in lexicographical order (according to their job numbers)
  4. total_tardiness - Computes the total tardiness for a given schedule.

2. tabu_init.py
  Runs the tabu search algorithm implemented in tabu_algorithm.py
  1. Build the directed acyclic graph (DAG) by using the information from data/input.json
  2. Set L = 5 and threshold = 30
  3. Set the initial solution to be the schedule given in data/sinit.json which is based on topological order
  4. Run the tabu search algorithm for K = 10, 100, and 1000 to obtain solutions that minimize the total tardiness
  5. EXTRA: Hyperparameter tuning to identify more optimal parameters (threshold and tabu list length(L)) and a better schedule.
