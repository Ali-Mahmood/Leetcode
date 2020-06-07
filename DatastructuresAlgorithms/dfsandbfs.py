# taken from https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# initial graph to search
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# DFS - non recursive
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}


# DFS - recursive
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


dfs(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}


# BFS - non recursive
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}


