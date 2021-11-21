"""
Consists of the main implementation of Least Cost Last (LCL) rule and some other helper functions
"""

import copy
import json
from functools import reduce

def LCL(V, Cmax):
    """
    Function returns the schedule following the Least Cost Last (LCL) Rule.
    Uncomment the print statements to see intermediate results printed in the terminal.
    
    Args: 
    (i) V (dict)
        A dictionary of all nodes in a graph.
        - key: node name (str), 
        - value: the node object (Node)
    (ii) Cmax (float)
        - the maximum completion time in the schedule (i.e. sum of all processing times)

    Returns: 
    (i) S (list): the schedule assigned following LCL rule
        - Each element in S is a node object.
    (ii) Tmax (float): the maximum tardiness found in schedule S.
    """
    # Initialise
    # Create an empty schedule
    S = [0]*(len(V)) 
    # Total processing times of all jobs already in the schedule S
    p_assigned = 0 
    # Keep track of Tmax
    Tmax = 0
    # At each iteration, 
    for k in range(len(V)-1,-1,-1):
        # print (f'For k = {k}, jobs with n = 0:')
        # Initialise
        Tj_min_node = None 
        Tj_min = Cmax 
        # Loop through every remaining node in the graph
        for node in V.values():
            # Find nodes that have no immediate successors (n = 0)
            if node.n == 0:
                # Calculate Tardiness, Tj
                Cj = Cmax - p_assigned
                Tj = max(0, Cj - node.due)

                # print(f'Job: {node.name}, Tj: {Tj}')

                # If current tardiness is smaller than Tj_min, replace it
                if Tj<Tj_min:
                    Tj_min = Tj
                    Tj_min_node = node
        
        # Add the node with the minimum tardiness as the kth job
        S[k] = Tj_min_node
        # Check if Tj_min has exceeded the current max tardiness. If yes, replace it
        if Tj_min > Tmax:
            Tmax = Tj_min
        # print(f'Minimum Tardiness Job Selected: {Tj_min_node.name} with Tj: {Tj_min}')
        # print ('Schedule S = ', S)
        # print()

        # Sum up its processing time for the next iteration.
        p_assigned += Tj_min_node.processing

        # For all jobs that have Tj_min_node as its immediate successor
        for successor in Tj_min_node.nodes_before:
            # Reduce their n value
            V[successor.name].n -= 1
        
        # Remove Tj_min_node from V
        del V[Tj_min_node.name]
    
    return S, Tmax

def get_cmax(filename, processing_times):
    """
    Obtain Cmax by summing up all processing times.
    
    Args:
        - filename (str): filepath to file containing the initial schedule.
        - processing_time (dict): a dictionary of processing times with key = job name (str), value = processing_time (float).
    
    Returns:
        - cmax (float): the maximum completion time for the last job in the schedule.

    """
    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']['due_dates']
    jobs_without_index = [job.split('_')[0] for job in data.keys()]
    # sum all the processing times in the system
    cmax = reduce(lambda p,job: p + processing_times[job], jobs_without_index, 0)

    return cmax

def total_tardiness(schedule):
    """
    Computes the total tardiness for a given schedule.
    
    Args:
        schedule (list): a list of jobs (node object) listed according to the schedule.
    
    Returns:
        tardiness (float): the total tardiness of all jobs in schedule.
    """
    Cj = 0
    tardiness = 0
    for job in schedule:
        Cj += job.processing
        Tj = max(0, job.due - Cj)
        tardiness += Tj
    
    return tardiness

def total_completion_time(schedule):
    """ 
    Computes the total completion time for a given schedule.
    
    Args:
        schedule (list): a list of jobs (node object) listed according to the schedule.
    
    Returns:
        sum_Cj (float): the total completion time of all jobs in schedule.
    """
    Cj = 0
    sum_Cj = 0
    for job in schedule:
        Cj += job.processing
        sum_Cj += Cj
    
    return sum_Cj
    

    

