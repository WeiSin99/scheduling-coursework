"""
Consists of all methods relating to processing data to/from .csv and/or .json files.
"""

import json
import csv

def read_input(filename):
    """Read incidence matrices from data/input.json.
    Args:
        - filename (str): filepath to file containing the incidence matrices.
    
    Returns:
        - data (list): a list with each element being a list of incidence pairs [from_job name (str), to_job name (str)].
    """
    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']['edge_set']

    return data

def read_due_dates(filename):
    """Read due dates from data/input.json.
    Args:
        - filename (str): filepath to file containing the due date.
    
    Returns:
        - data (dict): the dictionary of due dates with key = job name (str), value = due date (int)
    """

    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']['due_dates']

    return data

def read_init_schedule(filename):
    """Read the initial schedule from data/tabu/sinit.json.
    Args:
        - filename (str): filepath to file containing the initial schedule.
    
    Returns:
        - data (list): a list of job names (str) listed according to the schedule.
    """
    with open(filename) as f:
        data = json.load(f)
        data = data['workflow_0']

    return data

def write_schedule_to_csv(filename, schedule):
    """Convert schedules to csv format for processing.
    Args:
        - filename (str): filepath to save the converted .csv schedule.
        - schedule (list): a list of jobs (node object) listed according to the schedule.
    
    """

    job_numbers = [job.job_number for job in schedule]

    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(job_numbers)
