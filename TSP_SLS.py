import math
import random
import time

def GreedySearch(d_matrix):
    n = len(d_matrix)
    unvisited = list(range(0,n))
    current_node = random.randrange(n)
    route = [current_node]
    unvisited.remove(current_node)
    cost = 0
    while unvisited:
        x = math.inf
        index = current_node
        for i in unvisited:
            if d_matrix[current_node][i] < x:
                x = d_matrix[current_node][i]
                index = i
        route.append(index)
        unvisited.remove(index)
        cost += d_matrix[current_node][index]
        current_node = index
    cost += d_matrix[current_node][route[0]]
    route.append(route[0])
    return route, cost

def CheckTourLength(d_matrix, route):
    n = len(route)
    cost = 0
    for i in range(n):
        if i == n-1:
            cost += d_matrix[route[i]][route[0]]
        else:
            cost += d_matrix[route[i]][route[i+1]]
    return cost

def opt2_RouteSwap(route, node1, node2):
    new_route = []
    for i in route[0:node1+1]:
        new_route.append(i)
    for j in route[node2: node1:-1]:
        new_route.append(j)
    for k in route[node2+1:]:
        new_route.append(k)
    return new_route


def opt2_Improvement(route, cost, d_matrix, st):
    n = len(d_matrix)
    best_solution = route
    best_cost = cost
    no_change = 0
    explored_pairs = []
    et = time.time()
    iterations = 0

    while True:
        et = time.time()
        if no_change >= n**3 or (et-st) > 599:
            break
        if len(explored_pairs) == ((n-1)*n):
            route, cost = GreedySearch(d_matrix)
            explored_pairs = []

        node1 = random.randrange(n)
        node2 = random.randrange(n)
        while node1 == node2 or ((node1,node2) in explored_pairs) or ((node2,node1) in explored_pairs):
            et = time.time()
            if (et-st) > 599:
                break
            node1 = random.randrange(n)
            node2 = random.randrange(n)
        if (et-st) > 599:
            break
        new_route = opt2_RouteSwap(route, min(node1,node2), max(node1,node2))
        new_route_len = CheckTourLength(d_matrix, new_route)
        explored_pairs.append((node1,node2))
        explored_pairs.append((node2,node1))

        if new_route_len < best_cost:
            best_cost = new_route_len
            best_solution = new_route
            no_change = 0
            explored_pairs = []
        else:
            no_change += 1
        iterations += 1
    print("iterations: ", iterations)
    return best_solution, best_cost


def SLS(n, d_matrix):
    st = time.time()
    start_route, start_cost = GreedySearch(d_matrix)
    return opt2_Improvement(start_route, start_cost, d_matrix, st)

m6 = [[0.0000,9.1000,9.2000,9.3000,9.4000],
      [9.1000,0.0000,9.5000,9.6000,9.8000],
      [9.2000,9.5000,0.0000,9.8000,9.8000],
      [9.3000,9.6000,9.8000,0.0000,9.7000],
      [9.4000,9.8000,9.8000,9.7000,0.0000]]

st = time.time()
x = SLS(5,m6)
et = time.time()
elapsed_time = et - st
print("route: ", x[0], "cost: ", x[1])
print('Execution time:', elapsed_time, 'seconds \n')
