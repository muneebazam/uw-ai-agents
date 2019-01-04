# An algorithm to solve the Travelling Salesman Problem using Simulated Annealing

# import statements
from collections import namedtuple
from random import shuffle
from numpy import inf
import heapq
import math
import sys
import random
import time

# A Node is what we consider a 'vertex' in the graph 
Node = namedtuple('Node', 'city Gn')

def convertToSingleChar(x):
	 return {
		  'AA': 'a',
		  'AB': 'b',
		  'AC': 'c',
		  'AD': 'd',
		  'AE': 'e',
		  'AF': 'f',
		  'AG': 'g',
		  'AH': 'h',
		  'AI': 'i',
		  'AJ': 'j'
	 }[x]

def convertToOriginalChar(path):
	 path_len = len(path)
	 converted_path = ""
	 i = 0
	 for i in range(0, path_len):
		  if (ord(path[i]) > 96):
				converted_path += str('A' + chr(ord(path[i]) - 32))
		  else:
				converted_path += path[i]
	 return converted_path


# function which calculates the euclidian distance between two cities
def distance(graph, city1, city2):
	 c1 = graph[city1]
	 c2 = graph[city2]
	 return math.sqrt(((c1[1]-c2[1])**2) + ((c1[0]-c2[0])**2))


def generate_graph(path):
	 graph = {}
	 with open(path) as file:
		  for line in file:
				line = line.split()
				if len(line) == 3:
					 if (len(line[0]) > 1):
						  graph[convertToSingleChar(line[0])] = (int(line[1]), int(line[2]))
					 else:
						  graph[line[0]] = (int(line[1]), int(line[2]))
	 return graph


def calculate_tour_cost(graph, path):
	 path_len = len(path) - 1
	 tour_cost = 0
	 i = 0
	 while i < path_len:
		  tour_cost += distance(graph, path[i], path[i+1])
		  i += 1
	 return tour_cost


def swap(path, i, j):
	 lst = list(path)
	 lst[i], lst[j] = lst[j], lst[i]
	 return ''.join(lst)


def get_random_neighbour(graph, path):
    i = list(range(len(path)))
    city1 = random.choice(i)
    i.remove(city1)
    city2 = random.choice(i)
    newpath = swap(path, city1, city2)
    return newpath


def get_best_neighbour(graph, path):
	 best_path = None
	 lowest_cost = inf
	 new_path = ""
	 length = len(path)
	 cost = 0

	 for i in range(0, length):
		  for j in range(0, length):
				new_path = swap(path, i, j)
				cost = calculate_tour_cost(graph, "A" + new_path + "A")
				if (cost < lowest_cost):
					 lowest_cost = cost
					 best_path = new_path
	 return best_path


def generate_initial_path(numCities):
	 path = []
	 i = 1
	 while i < numCities:
		  if (i > 25):
				path.append((chr(71 + i)))
		  else:
				path.append((chr(65 + i)))
		  i += 1
	 shuffle(path)
	 return "A" + ''.join(path) + "A"


# simulated annealing 
def simulated_annealing(graph, path, schedule):

    new_path = ""
    X = 100000
    T = 0
    E = 0
    P = 0

    if (schedule == "log"):
    	T = math.log(X)
    elif (schedule == "exp"):
    	T = math.exp(-X)
    else:
    	T = X
    
    while T > 1:

        new_path = "A" + get_random_neighbour(graph, path[1:-1]) + "A"
        E = calculate_tour_cost(graph, path) - calculate_tour_cost(graph, new_path)
        if (E > 0):
            path = new_path
        else:
            if random.random() < P:
                path = new_path
        X -= 1
        if (schedule == "log"):
    		T = math.log(X)
    	elif (schedule == "exp"):
    		T = math.exp(-X)
    	else:
    		T = X

    print(convertToOriginalChar(path))
    print(calculate_tour_cost(graph, path))
    return path

def tsp_solver(numCities, numInstance, version):

	file_path = "Test_Problems/" + str(numCities) + "-City/instance_"+ str(numInstance) + ".txt"

	graph = generate_graph(file_path)
	path = generate_initial_path(numCities)

	if (version == 'log'):
		print("Running Simulated Annealing with Log Scheduling:")
		path = simulated_annealing(graph, path, version)
	elif (version == 'exp'):
		print("Running Simulated Annealing with Exp Scheduling:")
		path = simulated_annealing(graph, path, version)
	elif (version == 'linear'):
		print("Running Simulated Annealing with Linear Scheduling:")
		path = simulated_annealing(graph, path, version)
	else:
		print("ERROR: Invalid Version Number.")

	return path

tsp_solver(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
