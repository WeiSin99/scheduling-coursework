import copy

def LCL(V, Cmax):
    """
    Function returns the a schedule following the Least Cost Last (LCL) Rule.
    
    Args: 
    (i) V (dict)
        - key: node name (str), 
        - value: the node object (Node)
    (ii) Cmax (float)
        - the maximum completion time in the schedule (i.e. sum of all processing times in the system)

    Returns: 
    (i) S (list): the schedule assigned following LCL rule
        - Each element in S is the name (str) of the job.
    (ii) Tmax (float): the maximum tardiness
    """
    # Initialise
    # Create an empty schedule
    S = [0]*(len(V)) 
    # Total processing times of all jobs already in the schedule S
    p_assigned = 0 
    # Keep track of Tmax
    Tmax = 0
    for k in range(len(V)-1,-1,-1):
        # print (f'For k = {k}, jobs with n = 0:')
        # At each iteration, 
        Tj_min_node = None # Used to store node with minimum tardiness
        Tj_min = Cmax # Used to track the minimum tardiness
        for node in V.values():
            # Find the node that has no immediate successors (nj = 0)
            if node.n == 0:
                # Calculate Tardiness
                Cj = Cmax - p_assigned
                Tj = max(0, Cj - node.due)

                # print(f'Job: {node.name}, Tj: {Tj}')

                # Find the node that yields the minimum tardiness
                if Tj<Tj_min:
                    Tj_min = Tj
                    Tj_min_node = node
        
        # Add the node with the minimum tardiness as the kth job
        S[k] = Tj_min_node
        if Tj_min > Tmax:
            Tmax = Tj_min
        # print(f'Minimum Tardiness Job Selected: {Tj_min_node.name} with Tj: {Tj_min}')
        # print ('Schedule S = ', S)
        # print()

        # Sum up its processing time for the next k
        p_assigned += Tj_min_node.processing

        # For all jobs that have Tj_min_node as its immediate successor
        for successor in Tj_min_node.nodes_before:
            # Reduce their n value
            V[successor.name].n -= 1
        
        # Remove Tj_min_node from n
        del V[Tj_min_node.name]
    
    return S, Tmax

def Tabu(initial_solution, threshold, K, L):
    """
    """
    tabu_list = []
    g_best = float("inf")
    accepted_solution = initial_solution
    best_solution = None
    for k in range(0,K):
        # print()
        # print(f'k={k}')
        # all potential schedules that follows job's precedence in this iteration
        potential_schedule, swap_list = lexi_order_and_prec(accepted_solution)
        # print(swap_list)
        for i, schedule in enumerate(potential_schedule):
            g_xk = total_tardiness(accepted_solution)
            g_y =  total_tardiness(schedule)
            delta = g_xk - g_y

            swap = swap_list[i]
            swap_reverse = (swap[1], swap[0])
            tabu = swap in tabu_list or swap_reverse in tabu_list
            # print (f'checking current pair: {swap, swap_reverse}')
            if g_y < g_best:
                # print(f'Better solution found! g_y = {g_y} < g_best = {g_best}')
                # print('swap jobs', swap)
                accepted_solution = schedule
                best_solution = schedule
                g_best = g_y
                # print('best solution:')
                # print(best_solution)
                # add swap to the end of tabu list
                if tabu:
                    # print('found in Tabu list. Moved pair to end of list')
                    try:
                        tabu_list.remove(swap)
                    except ValueError:
                        tabu_list.remove(swap_reverse)
                tabu_list.append(swap)

                if len(tabu_list) > L:
                    tabu_list.pop(0)

                # print('Tabu List updated:', tabu_list)

                break

            elif (delta > -threshold and not tabu):
                # print(f'Solution within threshold found. Accept Solution. g_y = {g_y}, g_x = {g_xk}, delta = {delta} < threshold (={threshold})')
                # print('swap jobs', swap)
                accepted_solution = schedule
                # update tabu list
                tabu_list.append(swap)

                if len(tabu_list) > L:
                    tabu_list.pop(0)

                # print('Tabu List updated:', tabu_list)
                # print('Accepted Schedule')
                # print(accepted_solution)
                break
                
            # print('swap not accepted')

    return best_solution, g_best

def check_prec(schedule):
    """Checks if a given schedule is acceptable following the order of precedence"""
    # Check start node
    if not schedule[0].start:
        return False

    # Check intermediate nodes.
    # Keep track of jobs that have been executed. Dictates the subsequent allowable jobs.
    executed_list = [schedule[0]]
    for node in schedule[1:-1]:
        # if node not even in acceptable list, reject
        if all(before in executed_list for before in node.nodes_before):
            executed_list.append(node)
        else:
            return False

    # Check end node
    if not schedule[-1].end:
        return False

    # If all the above conditions hold true, the schedule follows order of precednece.
    return True

def lexi_order_and_prec(schedule):
    """Returns the possible schedule candidates sorted in lexicographical order (according to their job numbers)."""
    # Initialise
    candidate_list = list()
    swap_list = list()
    remaining_swap_list = list()
    remaining_candidate_list = list()

    for i in range(len(schedule)-1): 
        candidate = copy.deepcopy(schedule)
        temp = candidate [i]
        candidate[i] = candidate[i+1]
        candidate[i+1] = temp
        
        # Append only if this schedule follows the order of precedence
        if check_prec(candidate):
            # If the next job's job number is smaller than the current's, swap and save in the main list
            # This already follows lexicographical order
            if schedule[i].job_number > schedule[i+1].job_number:
                candidate_list.append(candidate)
                swap_list.append((schedule[i].job_number, schedule[i+1].job_number))
        
            # Otherwise, save it separately in remaining_candidate_list
            else:
                remaining_swap_list.append((schedule[i].job_number, schedule[i+1].job_number))
                remaining_candidate_list.append(candidate)
    
    # For the remaining candidates whose next job's job number was larger than its own, 
    if remaining_candidate_list != []:
        # Lexicographical order follows the reverse for the remaining_candidate_list
        remaining_candidate_list.reverse()
        remaining_swap_list.reverse()

        # Append now into the main list
        candidate_list += remaining_candidate_list
        swap_list += remaining_swap_list

    return candidate_list, swap_list

def total_tardiness(schedule):
    """Computes the total tardiness for a given schedule."""
    Cj = 0
    Tardiness = 0
    for job in schedule:
        Cj += job.processing
        Tj = max(0, job.due - Cj)
        Tardiness += Tj
    
    return Tardiness

def total_completion_time(schedule):
    """ Computes the total completion time for a given schedule."""
    Cj = 0
    sum_Cj = 0
    for job in schedule:
        Cj += job.processing
        sum_Cj += Cj
    
    return sum_Cj
    

    

