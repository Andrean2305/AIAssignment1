from collections import deque

def is_valid_move(maze, row, col, direction):
    # Check if the cell is within the bounds of the maze and is a valid move.
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        if direction == "UP" and "DOWN" not in maze[row][col]:
            return True
        elif direction == "DOWN" and "UP" not in maze[row][col]:
            return True
        elif direction == "LEFT" and "RIGHT" not in maze[row][col]:
            return True
        elif direction == "RIGHT" and "LEFT" not in maze[row][col]:
            return True
    return False

def find_path(maze, start, goal):
    # Initialize the BFS queue with the starting position.
    queue = deque([start])
    # Create a dictionary to store the parent of each cell.
    parent = {}

    while queue:
        row, col = queue.popleft()

        # If the goal is reached, reconstruct the path.
        if (row, col) == goal:
            path = [(row, col)]
            while (row, col) != start:
                row, col = parent[(row, col)]
                path.append((row, col))
            path.reverse()
            return path

        # Explore neighboring cells.
        for dr, dc, direction in [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]:
            new_row, new_col = row + dr, col + dc

            if is_valid_move(maze, new_row, new_col, direction) and (new_row, new_col) not in parent:
                queue.append((new_row, new_col))
                parent[(new_row, new_col)] = (row, col)

    return None  # No path found.

# Define the maze as a list of lists with directions.
maze = [[["LEFT", "RIGHT", "UP"], ["LEFT", "UP"], ["UP"], ["UP"], ["LEFT", "UP", "RIGHT"]],
        [["LEFT", "RIGHT"], ["LEFT", "RIGHT"], ["LEFT", "DOWN", "UP"], ["RIGHT"], ["LEFT", "RIGHT"]],
        [["LEFT", "RIGHT"], ["LEFT", "RIGHT"], ["LEFT", "UP", "DOWN"], ["DOWN"], ["RIGHT"]],
        [["LEFT"], [], ["UP", "RIGHT", "DOWN"], ["LEFT", "UP", "DOWN"], ["RIGHT"]],
        [["LEFT", "RIGHT", "DOWN"], ["LEFT", "DOWN"], ["UP", "DOWN"], ["UP", "DOWN"], ["DOWN", "RIGHT"]]]

start = (0, 0)
goal = (2, 1)

start = eval(input("GIVE THE START [IT SHOULD BE 0,0 IF BASED ON THE QUESTION SO JUST INPUT 0,0]: "))
goal = eval(input("GIVE THE GOAL [IT SHOULD BE 2,1 IF BASED ON THE QUESTION SO JUST INPUT 2,1]: "))
goal = (goal[1],goal[0])

path = find_path(maze, start, goal)

if path:
    print("Path found:")
    for row, col in path:
        print(f"({col}, {row})")
else:
    print("No path found.")

