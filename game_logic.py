def adjust_grid(positions, grid_width, grid_height):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbours(position, grid_width, grid_height)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))
        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbours(position, grid_width, grid_height)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions


def get_neighbours(pos, grid_width, grid_height):
    x, y = pos
    neighbors = []

    for dx in [-1, 0, 1]:
        nx = x + dx
        if nx < 0 or nx >= grid_width:
            continue

        for dy in [-1, 0, 1]:
            ny = y + dy
            if ny < 0 or ny >= grid_height:
                continue

            if dx == 0 and dy == 0:
                continue

            neighbors.append((nx, ny))

    return neighbors