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


## Recursive solution
def depthFirstTr(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstTr(graph, neighbor)


# Breadth First traversal
def breadthFirstTi(graph, source):
    queue = [source]
    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


breadthFirstTi(graph, "a")
