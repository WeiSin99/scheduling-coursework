# Image Processing Workflow - Introduction
Serverless workflow jobs are serverless function calls - a type of software service that runs in the cloud. These are increasingly used, for example, in batch processing of images, videos and data. A scheduling problem arises when functions execute together while being hosted inside the same environment (e.g., a virtual machine) and we want to sequence their executions in order to optimize some performance metrics, such as minimizing the maximum lateness. 

For this coursework, the functions considered perform image processing (eg. filters that mix the content of an image with the style of another image). The inputs and outputs of the filters create precedences in their executions that can be described by means of a directed acyclic graph (DAG), which captures the workflow characteristics. 

The aims of this project is to obtain an optimal algorithm for minimising tardiness subject to precendences on a single machine. These include the use of the (i) Least Cost Last Algorithm and (ii) Tabu Search Algorithm.

## Project layout
Structure of repository:
`````
scheduling-coursework
├── data
│ ├── lcl
│   ├── lcl.csv
│   └── lcl.json
│ ├── tabu
│   ├── sinit.csv
│   ├── sinit.json
│   ├── tabu_10.csv
│   ├── tabu_10.json
│   ├── tabu_100.csv
│   ├── tabu_100.json
│   ├── tabu_1000.csv
│   ├── tabu_1000.json
│   ├── tabu_optimal.csv
│   └── tabu_optimal.json
│ └── input.json
├── convert.py
├── data.py
├── graph.py
├── lcl_algorithm.py
├── lcl_init.py
├── node.py
├── README_lcl.txt
├── README_tabu.txt
├── README.md
├── tabu_algorithm.py
└── tabu_init.py
`````

The project's codebase consists of:
1. data.py <br>
    All methods relating to processing data to/from .csv and/or .json files.
    1. Read incidence matrices from data/input.json.
    2. Read due dates from data/input.json.
    3. Read the initial schedule from data/tabu/sinit.json.
    4. Convert schedules to csv format for processing.

2. node.py<br>
    The Node object implementation. Nodes are used to represent jobs in the workflow. 
    These are implemented in graph.py to build the Directed Acrylic Graph (DAG).

3. graph.py<br>
    The Graph module contains methods required to build a Directed Acrylic Graph that describes the workflow.
    1. Takes an incidence matrix and builds the DAG. 
    2. Methods to assign node attributes for nodes with the Graph (eg. processing times, due dates, number of successors, identifying start and end nodes).

4. lcl_algorithm.py and lcl_init.py<br>
    Please refer to README_lcl.txt for more information.

5. tabu_algorithm.py and tabu_init.py<br>
    Please refer to README_tabu.txt for more information.

For more details on each method, please refer to their respective docstrings found in each file.

## Authors

* **Alicia Jiayun Law** - *ajl115@ic.ac.uk*
* **Loo Wei Sin** - *wl2121@ic.ac.uk*

## License
[MIT License](https://choosealicense.com/licenses/mit/)
