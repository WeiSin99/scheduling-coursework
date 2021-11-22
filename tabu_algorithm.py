"""
Consists of the main implementation of the Tabu Search algorithm and some other helper functions.
"""

import copy

def Tabu(initial_solution, threshold, K, L):
    """
    Obtains a schedule that minimises the total tardiness based on the Tabu Search algorithm.
    Uncomment print statements to see intermediate results.

    Args:
    (i) initial_solution (list)
        - The initial schedule candidate at k=0. A list of node objects representing jobs in the schedule.
    (ii) threshold (int)
        - The upper bound for a worse solution to be accepted
    (iii) K (int)
        - The number of iteration to be run
    (iv) L (int)
        - The maximum length of tabu list

    Returns:
    (i) best_solution (list): the best schedule that minimises the total tardiness
        - Each element is a node object (Node)
    (ii) g_best (float): the total tardiness obtained from best_solution
    """
    # Initialise
    tabu_list = []
    g_best = float("inf")
    accepted_solution = initial_solution
    best_solution = None
    # Iterate K times
    for k in range(1,K+1):
        # print(f'k={k}')
        # Obtain all potential candidates that follows job's precedence for this iteration
        potential_schedule, swap_list = lexi_order_and_prec(accepted_solution)
        # For each of these candidates (schedule)
        for i, schedule in enumerate(potential_schedule):
            g_xk = total_tardiness(accepted_solution)
            g_y =  total_tardiness(schedule)
            delta = g_xk - g_y
            swap = swap_list[i]
            swap_reverse = (swap[1], swap[0])
            tabu = swap in tabu_list or swap_reverse in tabu_list
            # If schedule has the best cost
            if g_y < g_best:
                # print('Tabu List:', tabu_list)
                # print(f'Better solution found. g_y = {g_y} < g_best = {g_best}')
                # print('swap jobs', swap)

                # Accept the solution and replace it as the best solution
                accepted_solution = schedule
                best_solution = schedule
                g_best = g_y

                # Even if it is in the tabu list, allow swap (aspiration criteria)
                if tabu:
                    # Remove the pair from tabu list
                    try:
                        tabu_list.remove(swap)
                    except ValueError:
                        tabu_list.remove(swap_reverse)
                # Append the pair to the end of the tabu list (as though it just arrived)
                tabu_list.append(swap)

                # If tabu_list size L has been exceeded, pop the node at the start of the list
                if len(tabu_list) > L:
                    tabu_list.pop(0)

                # print('Tabu List updated:', tabu_list)
                break

            # Else if, schedule cost is within threshold
            elif (delta > -threshold and not tabu):
                # Accept the solution, and
                accepted_solution = schedule
                # Update tabu list
                tabu_list.append(swap)

                # If tabu_list size L has been exceeded, pop the node at the start of the list
                if len(tabu_list) > L:
                    tabu_list.pop(0)

                # print(f'Solution within threshold found. Accept Solution. g_y = {g_y}, g_x = {g_xk}, delta = {delta} < threshold (={threshold})')
                # print('swap jobs', swap)
                # print('Tabu List updated:', tabu_list)
                break

            # Otherwise, job not accepted.  
            # print('swap not accepted')

    return best_solution, g_best

def check_prec(schedule):
    """
    Checks if a given schedule is acceptable following the order of precedence.
    
    Args:
        schedule (list): a list of jobs (node object) listed according to the schedule.
    
    Returns:
        (boolean): true if schedule follows order of precendence. False otherwise.
    """
    # Check first node.
    # First node in the schedule must be the start node of the graph
    if not schedule[0].start:
        return False

    # Check intermediate nodes.
    # Track jobs that have been executed. Dictates the subsequent allowable jobs.
    executed_list = [schedule[0]]
    for node in schedule[1:-1]:
        # If all predecessors (node.nodes_before) have been executed, current job is allowed.
        if all(before in executed_list for before in node.nodes_before):
            executed_list.append(node)
        # Otherwise, job cannot be executed.
        else:
            return False

    # Check end node.
    # Last node must be the end node of the graph.
    if not schedule[-1].end:
        return False

    # If all above conditions hold true, the schedule follows order of precednece.
    return True

def lexi_order_and_prec(schedule):
    """
    Returns the possible schedule candidates sorted in lexicographical order (according to their job numbers).
    Explores only adjacent pairs.

    Args:
        schedule (list): a list of jobs (node object) listed according to the schedule.
    
    Returns:
        candidate_list(list): a list of potential candidate schedules (list), sorted by lexicographical order.
        swap_list(list): a list of job pairs (list) swapped corresponding to the schedules in candidate_list.

    """
    # Initialise
    candidate_list = list()
    swap_list = list()
    remaining_swap_list = list()
    remaining_candidate_list = list()

    # Iterate across all adjacent job pairs in a schedule
    for i in range(len(schedule)-1): 
        # Swap the pairs
        candidate = copy.deepcopy(schedule)
        temp = candidate [i]
        candidate[i] = candidate[i+1]
        candidate[i+1] = temp
        
        # Check if this schedule follows the order of precedence.
        if check_prec(candidate):
            # If the next job's job number is smaller than the current's (eg: (5, 2)), swap and save in the main list
            # This already follows lexicographical order
            if schedule[i].job_number > schedule[i+1].job_number:
                candidate_list.append(candidate)
                swap_list.append((schedule[i].job_number, schedule[i+1].job_number))
        
            # Otherwise, save it aside in remaining_candidate_list 
            else:
                remaining_swap_list.append((schedule[i].job_number, schedule[i+1].job_number))
                remaining_candidate_list.append(candidate)
    
    # For the remaining candidates whose next job's job number was larger than its own (eg: (2,5)), 
    if remaining_candidate_list != []:
        # Lexicographical order follows the reverse for the remaining_candidate_list
        remaining_candidate_list.reverse()
        remaining_swap_list.reverse()

        # Append this with the main lists
        candidate_list += remaining_candidate_list
        swap_list += remaining_swap_list

    return candidate_list, swap_list

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
