import heapq

# Graph 
graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('E', 12), ('F', 5)],
    'C': [('E', 10),('D',7)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)],
    'G': []
}

# Heuristic values
h = {
    'S': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (h[start], 0, start, [start]))  # (f, g, node, path)
    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in closed_set:
            continue
        closed_set.add(current)

        if current == goal:
            return path, g

        for neighbor, cost in graph[current]:
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + h[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')

path, total_cost = astar('S', 'G')
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", total_cost)