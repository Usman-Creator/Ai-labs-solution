graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'C': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['L'],
    'J': [],
    'K': ['N', 'M'],
    'L': [],
    'M': [],
    'N': []
}

# Breadth-First Search function
def bfs(graph, start, goal):
    if start == goal:
            print("Goal node", goal, "found!")
            return
    # Create a queue for BFS
    queue = []
    # Keep track of visited nodes
    visited = []
    
    # Add the starting node to the queue and mark as visited
    queue.append(start)
    
    while queue:
        if (len(queue) == 0 ):
            print("Goal Not Found")
            return
        # Remove the first element from the queue
        node = queue.pop(0)
        print("Visiting:", node)
        visited.append(node)
        
        # If we find the goal, stop the search
        if node == goal:
            print("Goal node", goal, "found!")
            return
        
        # Add neighbors to the queue if not visited
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
  

# Call the function
bfs(graph, 'A', 'G')