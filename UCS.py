import heapq

DIRECTIONS = [
    ('N', (0, -1)),
    ('S', (0, 1)),
    ('E', (1, 0)),
    ('W', (-1, 0))
]

def ucs(start_state):
    heap = []
    heapq.heappush(heap, (0, start_state, []))  # roomba
    visited = set()

    nodes_generated = 1
    nodes_expanded = 0

    while heap:
        cost, state, path = heapq.heappop(heap)

        if is_goal(state):
            print_solution(path, nodes_generated, nodes_expanded)
            return

        if state in visited:
            continue

        visited.add(state)
        nodes_expanded += 1

        for action, new_state in expand(state):
            if new_state not in visited:
                heapq.heappush(heap, (cost + 1, new_state, path + [action]))
                nodes_generated += 1

def is_goal(state):
    _, dirt = state
    return len(dirt) == 0

def expand(state):
    (x, y), dirt = state
    children = []

    for action, (dx, dy) in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            children.append((action, ((new_x, new_y), dirt)))

    if (x, y) in dirt:
        new_dirt = frozenset(dirt - {(x, y)})
        children.append(('V', ((x, y), new_dirt)))

    return children

def is_valid(x, y):
    return 0 <= x < cols and 0 <= y < rows and grid[y][x] != '#'

def print_solution(path, nodes_generated, nodes_expanded):
    for action in path:
        print(action)
    print(f"{nodes_generated} nodes generated")
    print(f"{nodes_expanded} nodes expanded")

grid = []
cols = 0
rows = 0