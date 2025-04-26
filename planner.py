import sys
import DFS
import UCS

def load_world(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    cols = int(lines[0])
    rows = int(lines[1])
    grid = [list(line) for line in lines[2:]]

    start_pos = None
    dirt = set()
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '@':
                start_pos = (x, y)
            if grid[y][x] == '*':
                dirt.add((x, y))

    return grid, cols, rows, (start_pos, frozenset(dirt))

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 planner.py [algorithm] [world-file]")
        sys.exit(1)

    algorithm = sys.argv[1]
    filename = sys.argv[2]

    grid, cols, rows, start_state = load_world(filename)

    DFS.grid = grid
    DFS.cols = cols
    DFS.rows = rows
    UCS.grid = grid
    UCS.cols = cols
    UCS.rows = rows

    if algorithm == 'depth-first':
        DFS.dfs(start_state)
    elif algorithm == 'uniform-cost':
        UCS.ucs(start_state)
    else:
        print("Use 'depth-first' or 'uniform-cost'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
