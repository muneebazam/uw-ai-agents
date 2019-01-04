# An algorithm to solve the Travelling Salesman Problem using A* Search

# import statements
from collections import namedtuple
from numpy import inf
import heapq
import math
import sys
import time

# A Node is what we consider a 'vertex' in the graph 
# Stores the letter and the G(n) value for that city
Node = namedtuple('Node', 'city Gn')

# function which is given a node and list of cities and 
# generates all the neighbors for that specific city
def generate_neighbours(cityList, node):
    
    neighbours = []
    pathSoFar = set(node.city)
    
    for city in cityList:
        if city in pathSoFar:
            continue
        else:
            neighbours.append(node.city + city)
            
    # if no unvisited neighbours we are done, return to A
    if len(neighbours) == 0:
        neighbours.append(node.city + 'A')
    
    return neighbours


# function called once to read in the .txt file and create graph
def generate_graph(path):
    graph = {}
    with open(path) as file:
        for line in file:
            line = line.split()
            if len(line) == 3:
                graph[line[0]] = (int(line[1]), int(line[2]))
    return graph


# function which generates the heuristic value [h(n)]
# The heuristic being used is nearest neighbour O(n^2)
def generate_heuristic(graph, city, cityList, visited):
    minDist = inf;
    for c in cityList:
        if c in visited or city[-1] == c:
            continue
        else:
            dist = distance(graph, city[-1], c)
            if dist < minDist:
                minDist = dist;
            else:
                continue
    # a minDist of inf means we have visited every city
    # so return the distance to the start city A
    if minDist == inf:
        return distance(graph, city[-1], 'A')
    else:
        return minDist;


# function which calculates the euclidian distance between two cities
def distance(graph, city1, city2):
    c1 = graph[city1]
    c2 = graph[city2]
    return math.sqrt(((c1[1]-c2[1])**2) + ((c1[0]-c2[0])**2))


# function which checks if we have completed our tour
def goal(node):
    return len(node.city) > 1 and node.city[-1] == 'A'


# main a_star algorithm
def a_star(graph, cityList):

    # initialize necessary variables 
    visited_nodes = 0
    frontier = []
    visited = set()
    heapq.heappush(frontier, (0.0, Node('A', 0.0)))

    # continously loops until our frontier is empty (nothing left to explore)
    while len(frontier) > 0:
            
        # 'take' the node with the lowest f(n) value
        # and add it to our visited set
        current = heapq.heappop(frontier)
        currentFn = current[0]
        currentNode = current[1]
        visited.add(currentNode.city[-1])
        
        # if we have reached the goal (tour is complete)
        # then print the number of visited nodes and exit
        if goal(currentNode):
            #print(visited_nodes)
            return (currentNode.city, currentFn) 
        else:
            # generate the neighbours for our current city and add any
            # unvisited neighbors to the frontier
            neighbours = generate_neighbours(cityList, currentNode)
            for city in neighbours:
                visited_nodes += 1
                if city in frontier:
                    continue
                else:
                    newGn = currentNode.Gn + distance(graph, currentNode.city[-1], city[-1])
                    # replace 'generate_heuristic(graph, city, cityList, visited)' with 0 for h(n) = 0
                    newFn = newGn + generate_heuristic(graph, city, cityList, visited)
                    heapq.heappush(frontier, (newFn, Node(city, newGn)))
    
    return (least_cost_node.city, least_cost_f)

# function that is called to start the A* TSP algorithm
# requires the number of cities and instance number for
# the problem verion you are trying to solve
def a_star_tsp(numCities, numInstance):
    
    # create path to folder tsp_problems/<numCities>-City/instance_<numInstance>.txt
    path = "Test_Problems/" + str(numCities) + "-City/instance_"+ str(numInstance) + ".txt"

    # generate the graph
    cityMap = generate_graph(path)

    # generate the list of cities
    cityList = sorted(list(cityMap.keys()))

    # start the timer
    startTime = time.time()

    # run main A* TSP algorithm
    result = a_star(cityMap, cityList)

    # stop the timer
    endTime = time.time()

    # print our results and exit
    # print (endTime - startTime)
    print "Path: " + result[0] + ", Cost: " + str(result[1])
    return result

a_star_tsp(sys.argv[1], sys.argv[2])

