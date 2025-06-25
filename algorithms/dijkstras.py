"""
Chapter 7 Grokking - Dijkstras Alg

Straight forward script for learning purposes
"""

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


# walk back over path
def print_path(parents, end="fin"):
    path = []
    node = end
    while node:
        path.append(node)
        node = parents.get(node) # return None if does not exist

    path.reverse()
    print(" → ".join(path))


# find the lowest cost node
def find_lowest_cost_node(costs, processed):
    low = [float("inf"), None]

    for n in costs.keys():
        if n not in processed:
            if costs[n] < low[0]:
                low = [costs[n], n]
        
    return low[1]


# main func
def dijkstras(graph, costs, parents):
    processed = []

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print_path(parents)


if __name__ == "__main__":
    """
    Test start → b → fin
    """
    graph = {
        "start": {"a": 5, "b": 2},
        "a": {"c": 4, "d": 2},
        "b": {"a": 8, "d": 7, "fin": 4},
        "c": {},
        "d": {"fin": 1},
        "fin": {}
    }

    infinity = float("inf")
    costs = {
        "a": 5,
        "b": 2,
        "c": infinity,
        "d": infinity,
        "fin": infinity
    }


    parents = {
        "a": "start",
        "b": "start",
        "c": None,
        "d": None,
        "fin": None
    }


    dijkstras(graph, costs, parents)