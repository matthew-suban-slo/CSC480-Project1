from collections import deque

DIRECTIONS = [
    ('N', (0, -1)),
    ('S', (0, 1)),
    ('E', (1, 0)),
    ('W', (-1, 0))
]

def dfs(start_state):
    stack = deque()
    stack.append((start_state, []))
    visited = set()

    nodes_generated = 1 # roomba
    nodes_expanded = 0

    while stack:
        state, path = stack.pop()

        if is_goal(state):
            print_solution(path, nodes_generated, nodes_expanded)
            return
        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1

        for action, new_state in expand(state):
            if new_state not in visited:
                stack.append((new_state, path + [action]))
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

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 DFS.py [world-file]")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    grid = [list(line) for line in lines]

    cols = len(grid[0])
    rows = len(grid)

    start_pos = None
    dirt = set()
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '@':
                start_pos = (x, y)
            if grid[y][x] == '*':
                dirt.add((x, y))

    start_state = (start_pos, frozenset(dirt))

    dfs(start_state)