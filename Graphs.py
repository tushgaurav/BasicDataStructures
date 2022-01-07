graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

# Depth First traversal

## Iterative solution
def depthFirstTi(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


depthFirstTi(graph, "a")
