import collections

# BFS algorithm
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited and enqueue its neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == '__main__':
    # Define the graph as an adjacency list
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

    print("Following is Breadth First Traversal:")
    bfs(graph, 0)
