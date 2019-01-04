Travelling Salesman
===================

Multiple search algorithm implementations to solve the Travelling Salesman problem including:

- A Star
- Hill Climbing
- Simulated Annealing 

The *Test_Problems/* directory contains 10 test instances for each number of cities ranging from 1 to 16 as well as a 36 city instance.


## a_star.py

This program implements the A-star search algorithm with the *nearest neighbour* heuristic to solve the Travelling Salesman Problem. 

### Usage

```python a_star.py <num_city> <num_instance>```

## hill_climbing.py

This program implements multiple variations of the local search hill climbing algorithm to solve the Travelling Salesman Problem. 

### Usage

```python hill_climbing.py <num_city> <num_instance> <version_number>```

Where ```<version_number>``` is one of *A*, *B* or *C* corresponding to the following versions:

*A*: Hill Climbing 

*B*: Hill Climbing + Sideway Moves

*C*: Hill Climbing + Sideway Moves + Random Restarts

## simulated_annealing.py

This program implements the local search simulated annealing algorithm to solve the Travelling Salesman Problem.

### Usage

```python simulated_annealing.py <num_city> <num_instance> <scheduler_version>```

Where ```<scheduler_version>``` must be one of: *log*, *exp* or *linear* indicating a logarithmic, exponential or linear scheduling algorithm respectively. 







