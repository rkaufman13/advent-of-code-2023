# Python3 program to find all the reachable nodes
# for every node present in arr[0..n-1]
from collections import deque, Counter
from utils import file_parsing



def addEdge(v, w):
	
	global visited, adj
	adj[v].append(w)
	adj[w].append(v)

def BFS(componentNum, src):
	
	global visited, adj
	
	# Mark all the vertices as not visited
	# Create a queue for BFS
	#a = visited
	queue = deque()

	queue.append(src)

	# Assign Component Number
	visited[src] = 1

	# Vector to store all the reachable 
	# nodes from 'src'
	reachableNodes = []
	#print("0:",visited)

	while (len(queue) > 0):
		
		# Dequeue a vertex from queue
		u = queue.popleft()

		reachableNodes.append(u)

		# Get all adjacent vertices of the dequeued
		# vertex u. If a adjacent has not been visited,
		# then mark it visited and enqueue it
		for itr in adj[u]:
			if (visited[itr] == 0):
				
				# Assign Component Number to all the
				# reachable nodes
				visited[itr] = 1
				counts = Counter(visited)
				queue.append(itr)

	return reachableNodes

# Display all the Reachable Nodes 
# from a node 'n'
def displayReachableNodes(m):
	
	for i in m:
		print(i, end = " ")

	print()

def findReachableNodes(arr, n):
	
	global V, adj, visited, longest_path
	
	# Get the number of nodes in the graph

	# Map to store list of reachable Nodes for a
	# given node.
	a = []

	# Initialize component Number with 0
	componentNum = 0

	# For each node in arr[] find reachable
	# Nodes
	for i in range(n):
		u = arr[i]

		# Visit all the nodes of the component
		if (visited[u] == 0):
			componentNum += 1

			# Store the reachable Nodes corresponding
			# to the node 'i'
			a = BFS(componentNum, u)

		# At this point, we have all reachable nodes
		# from u, print them by doing a look up in map m.
		print("Reachable Nodes from ", u, " are")
		displayReachableNodes(a)
		return a


# This code is contributed by mohit kumar 29

def find_path(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a
        # new path and push it into the queue
        for adjacent in graph[node]:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)



right_symbols = ['-','L','F', 'S']
left_symbols = ['-','7','J','S']
up_symbols = ['|','L','J','S']
down_symbols = ['|','7','F','S']


def look_left(col_index, row_index, data):
	if col_index>0:
		left_symbol = data[row_index][col_index-1]
		if left_symbol in right_symbols: #in other words, if "J" is our current symbol, we want to know if the one to the left of it is "facing" right
					addEdge((row_index*len(data[0])+col_index),row_index*len(data[0])+col_index-1)


def look_right(col_index, row_index, data):
	if col_index<len(data)-1:
		right_symbol = data[row_index][col_index+1]
		if right_symbol in left_symbols:
			addEdge((row_index * len(data[0]) + col_index), row_index * len(data[0]) + col_index + 1)

def look_down(col_index, row_index, data):
	if row_index<(len(data)-1):
		lower_symbol = data[row_index+1][col_index]
		if lower_symbol in up_symbols:
			addEdge((row_index * len(data[0]) + col_index), row_index * len(data[0]) + col_index + len(data[0]))


def look_up(col_index, row_index, data):
	if row_index>0:
		upper_symbol = data[row_index-1][col_index]
		if upper_symbol in down_symbols:
			addEdge((row_index * len(data[0]) + col_index), row_index * len(data[0]) + col_index - len(data[0]))

def part_one():
	global adj
	global visited
	global longest_path
	longest_path= 0

	path = "input/full_data.txt"
	data = file_parsing.open_and_read_file(path)
	for i in range(len(data)):
		data[i] = data[i].replace("\n","")

	V = (len(data) * len(data[0]))

	adj = [[] for i in range(V + 1)]
	visited = [0 for i in range(V + 1)]

	for row_index, line in enumerate(data):
		for col_index, character in enumerate(line):
			if character == "S":
				start = (row_index * len(data[0]) + col_index)
			if character in left_symbols:
				look_left(col_index, row_index, data)
			if character in right_symbols:
				look_right(col_index, row_index, data)
			if character in up_symbols:
				look_up(col_index, row_index, data)
			if character in down_symbols:
				look_down(col_index, row_index, data)
	for index, edges in enumerate(adj):
		adj[index] = list(set(edges))


	reachable_nodes = findReachableNodes([start],1)
	length = 0
	print(len(reachable_nodes)/2)
	# for reachable_node in reachable_nodes:
	# 	path_steps = find_path(adj, start, reachable_node)
	# 	if len(path_steps)>length:
	# 		length = len(path_steps)
	# print(length-1)
	# print(reachable_nodes[-1])
	# path_steps = find_path(adj, start, reachable_nodes[-1])
	# print(len(path_steps)-1)

part_one()