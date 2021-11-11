import json
from functools import reduce

def read_input(filename):
    """Reads the json file and obtains the list of incidence matrices.
    Args:
        - filename (str): filepath
    
    Returns:
        - data [type]: the incidence matrix
    """
    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']['edge_set']

    return data

def read_due_dates(filename):
    """Reads the json file and obtains the due dates.
    Args:
        - filename (str): filepath
    
    Returns:
        - data [type]: the list of due dates
    """

    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']['due_dates']

    return data

def get_cmax(filename, processing_times):
    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']['due_dates']
    jobs_without_index = [job.split('_')[0] for job in data.keys()]
    cmax = reduce(lambda p,job: p + processing_times[job], jobs_without_index, 0)

    return cmax

def read_init_schedule(filename):
    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']

    return data
