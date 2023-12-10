# Python3 program to find all the reachable nodes
# for every node present in arr[0..n-1]
from collections import deque

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
				queue.append(itr)

	return reachableNodes

# Display all the Reachable Nodes 
# from a node 'n'
def displayReachableNodes(m):
	
	for i in m:
		print(i, end = " ")

	print()

def findReachableNodes(arr, n):
	
	global V, adj, visited
	
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

# Driver code
if __name__ == '__main__':
	
	V = 7
	adj = [[] for i in range(V + 1)]
	visited = [0 for i in range(V + 1)]
	addEdge(1, 2)
	addEdge(2, 3)
	addEdge(3, 4)
	addEdge(3, 1)
	addEdge(5, 6)
	addEdge(5, 7)

	# For every ith element in the arr
	# find all reachable nodes from query[i]
	arr = [ 2, 4, 5 ] 

	# Find number of elements in Set
	n = len(arr)

	findReachableNodes(arr, n)

# This code is contributed by mohit kumar 29
