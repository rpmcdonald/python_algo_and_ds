offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def is_legal_pos(grid, pos):
    i, j = pos
    num_rows = len(grid)
    num_cols = len(grid[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and grid[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path
