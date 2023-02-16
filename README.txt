PROJECT NAME
=========================================================================================
Solving Traveling Salesman Problem with Branch and Bound - DFS (BnB-DFS) and Stochastic Local Search (SLS)

DESCRIPTION
=========================================================================================
This program is developed with the python language and intended to solve the infamous Traveling Salesman Problem by implementing BnB-DFS and SLS in python.

For the BnB-DFS approach, a total of three functions are created: heuristic function, initialization function and function for executing BnB-DFS. 

For the SLS approach, a total of five functions are created: nearest neighborhood function, calculating tour length, 2-Opt route swap, 2-Opt improvement and last but not least SLS execution function.

INSTALLATION
=========================================================================================
Before running the code, download PyPy by going to https://www.pypy.org/download.html.

Prior to executing the code, following modules are required:
1) math
2) random
3) time

FUNCTIONS
=========================================================================================
BnB-DFS
————————————————————————————————————————————————————
heuristic(unvisited, node_to_expand, distance_matrix, current_cost) 
bnb(n, d_matrix) ## n: length of the route
dfs(d_matrix, current_cost, d, current_path, visited) ## d: depth of the tree

SLS ————————————————————————————————————————————————————
GreedySearch(d_matrix)
CheckTourLength(d_matrix, route)
opt2_RouteSwap(route, node1, node2)
opt2_Improvement(route, cost, d_matrix)
SLS(n, d_matrix) ## n: length of matrix

USAGE
=========================================================================================
BnB-DFS
————————————————————————————————————————————————————
REQUIRES:: 
n (number of nodes), symmetric distance matrix with 0 diagonal 

To use PyPy, put the .py file into the same folder where the “pypy” file is. Navigate to this folder in the terminal and run ./pypy “name of .py file”.

In order to use the distance text file that is included in the ZIP file, the user must change the path of the matrix to the location where the user has saved the distance matrix text file.

IMPLEMENTATION:
i.e.
d_matrix= [[0,1,2,3],[1,0,3,4],[2,3,0,5],[3,4,5,0]]
bnb(4, d_matrix)

One sample matrix is included in our source code.


SLS 
————————————————————————————————————————————————————
REQUIRES:
n (number of nodes), symmetric distance matrix with 0 diagonal 

To use PyPy, put the .py file into the same folder where the “pypy” file is. Navigate to this folder in the terminal and run ./pypy “name of .py file”.

In order to use the distance text file that is included in the ZIP file, the user must change the path of the matrix to the location where the user has saved the distance matrix text file.

IMPLEMENTATION:
i.e. 
d_matrix= [[0,1,2,3],[1,0,3,4],[2,3,0,5],[3,4,5,0]]
route, cost = GreedySearch(d_matrix) 
opt2_Improvement(route, cost, d_matrix)

One sample matrix is included in our source code.


AUTHORS
=========================================================================================
* Uniss Tan - utan@uci.edu
* John Kim - johnjk14@uci.edu
* Ji Young Noh - jiyn@uci.edu
