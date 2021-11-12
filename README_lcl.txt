Code Execution Instructions

Run the following command to execute the code:

1. cd into the project directory with: `cd scheduling-coursework`
2. Run the tabu search algorithm with the following commands: `python3 lcl_init.py`

Consists of two main parts:

1. lcl_algorithm.py
  Consists of the main implementation of Least Cost Last (LCL) rule and some other helper functions
  1. LCL - Implementation of Least Cost Last (LCL) Rule.
  2. get_cmax - Obtain Cmax by summing up all processing times
  3. total_tardiness - Computes the total tardiness for a given schedule
  4. total_completion_time - Computes the total completion time for a given schedule

2. lcl_init.py
  Runs the LCL algorithm implemented in lcl_algorithm.py
  1. Build the directed acyclic graph (DAG) by using the information from data/input.json
  2. Run the LCL algorithm to obtain solutions that minimize the maximum tardiness
