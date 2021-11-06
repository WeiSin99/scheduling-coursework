import json
from functools import reduce

def read_input():
    """Reads the json file."""
    with open('input.json') as f:
        data = json.load(f)
        data = data['workflow_0']['edge_set']

    return data

def read_due_dates():
    """Reads the json file."""
    with open('input.json') as f:
        data = json.load(f)
        data = data['workflow_0']['due_dates']

    return data

def get_cmax(processing_times):
    with open('input.json') as f:
        data = json.load(f)
        data = data['workflow_0']['due_dates']
    jobs_without_index = [job.split('_')[0] for job in data.keys()]
    cmax = reduce(lambda p,job: p + processing_times[job], jobs_without_index, 0)

    return cmax