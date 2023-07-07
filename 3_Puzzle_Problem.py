# function to get the position of a block value in the puzzle
def get_position(puzzle, value):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == value:
                return (i, j)

# function to get the Manhattan distance heuristic value for a given puzzle
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                goal_pos = get_position(goal, puzzle[i][j])
                distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return distance

#function to get the neighbors of a given puzzle state
def get_neighbors(puzzle):
    neighbors = []
    zero_pos = get_position(puzzle, 0)
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_pos = (zero_pos[0] + dx, zero_pos[1] + dy)
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[zero_pos[0]][zero_pos[1]] = puzzle[new_pos[0]][new_pos[1]]
            new_puzzle[new_pos[0]][new_pos[1]] = 0
            neighbors.append(new_puzzle)
    return neighbors

initial = []
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
for i in range(3):
    s=[]
    for j in range(3):
        k = int(input())
        s.append(k)
    initial.append(s)

# A* search algorithm
queue = [(manhattan_distance(initial), initial)]
visited = set()
came_from = {}
cost_so_far = {str(initial): 0}

while queue:
    queue.sort()
    _, current = queue.pop(0)
    if current == goal:
        break
    visited.add(str(current))

    for neighbor in get_neighbors(current):
        new_cost = cost_so_far[str(current)] + 1
        if str(neighbor) not in cost_so_far or new_cost < cost_so_far[str(neighbor)]:
            cost_so_far[str(neighbor)] = new_cost
            priority = new_cost + manhattan_distance(neighbor)
            queue.append((priority, neighbor))
            if str(neighbor) not in visited:
                came_from[str(neighbor)] = current

# Backtrack to get the path from initial to goal
current = goal
path = [current]
while current != initial:
    current = came_from[str(current)]
    path.append(current)
path.reverse()

# Print the results
for i, state in enumerate(path):
    print(f"Step {i}:")
    for row in state:
        print(row)
    print('\n')
