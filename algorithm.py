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
        print (f'For k = {k}, jobs with n = 0:')
        # At each iteration, 
        Tj_min_node = None # Used to store node with minimum tardiness
        Tj_min = Cmax # Used to track the minimum tardiness
        for node in V.values():
            # Find the node that has no immediate successors (nj = 0)
            if node.n == 0:
                # Calculate Tardiness
                Cj = Cmax - p_assigned
                Tj = max(0, Cj - node.due)

                print(f'Job: {node.name}, Tj: {Tj}')

                # Find the node that yields the minimum tardiness
                if Tj<Tj_min:
                    Tj_min = Tj
                    Tj_min_node = node
                
                # # If there is a tie, assign the job with the longest processing time (break with SPT)
                # elif Tj == Tj_min:
                #     if node.processing > Tj_min_node.processing:
                #         Tj_min_node = node
        
        # Add the node with the minimum tardiness as the kth job
        S[k] = Tj_min_node.name
        if Tj_min > Tmax:
            Tmax = Tj_min
        print(f'Minimum Tardiness Job Selected: {Tj_min_node.name} with Tj: {Tj_min}')
        print ('Schedule S = ', S)
        print()

        # Sum up its processing time for the next k
        p_assigned += Tj_min_node.processing

        # For all jobs that have Tj_min_node as its immediate successor
        for successor in Tj_min_node.nodes_before:
            # Reduce their n value
            V[successor.name].n -= 1
        
        # Remove Tj_min_node from n
        del V[Tj_min_node.name]
    
    return S, Tmax