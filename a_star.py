from helpers import get_path, offsets, is_legal_pos
from data_structures import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(grid, start, goal):
    p_q = PriorityQueue()
    p_q.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not p_q.is_empty():
        current_cell = p_q.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(grid, neighbour) and neighbour not in predecessors:
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(neighbour, goal)
                p_q.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
    return None