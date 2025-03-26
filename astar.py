import pygame
import heapq

# Define the grid size and colors
GRID_SIZE = 20
WIDTH, HEIGHT = 600, 600
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding")

# Define the Node class
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g = float('inf')  # Cost from start to node
        self.h = float('inf')  # Heuristic (estimated cost to goal)
        self.f = float('inf')  # Total cost (g + h)
        self.parent = None
        self.is_obstacle = False

    def __lt__(self, other):
        return self.f < other.f

# Create the grid
def create_grid():
    return [[Node(row, col) for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]

# Draw the grid
def draw_grid(grid, start, end, open_set, closed_set):
    screen.fill(WHITE)

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            node = grid[row][col]
            rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)

            if node.is_obstacle:
                pygame.draw.rect(screen, BLACK, rect)
            elif node == start:
                pygame.draw.rect(screen, GREEN, rect)
            elif node == end:
                pygame.draw.rect(screen, RED, rect)
            elif node in open_set:
                pygame.draw.rect(screen, YELLOW, rect)
            elif node in closed_set:
                pygame.draw.rect(screen, BLUE, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    pygame.display.update()

# A* Algorithm
def a_star(grid, start, end):
    open_set = []
    closed_set = set()

    start.g = 0
    start.h = abs(start.row - end.row) + abs(start.col - end.col)
    start.f = start.g + start.h

    heapq.heappush(open_set, start)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node)

        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        for neighbor in get_neighbors(current_node, grid):
            if neighbor in closed_set or neighbor.is_obstacle:
                continue

            tentative_g = current_node.g + 1

            if tentative_g < neighbor.g:
                neighbor.parent = current_node
                neighbor.g = tentative_g
                neighbor.h = abs(neighbor.row - end.row) + abs(neighbor.col - end.col)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return []

# Get neighbors of a node
def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        row, col = node.row + direction[0], node.col + direction[1]
        if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
            neighbors.append(grid[row][col])
    return neighbors

# Main function
def main():
    grid = create_grid()
    start = None
    end = None
    running = True
    path = []
    is_drawing_obstacles = False

    while running:
        draw_grid(grid, start, end, path, set())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // GRID_SIZE, pos[0] // GRID_SIZE
                node = grid[row][col]

                if start is None:
                    start = node
                    start.is_obstacle = False
                elif end is None:
                    end = node
                    end.is_obstacle = False
                elif event.button == 1:  # Left click to set obstacles
                    node.is_obstacle = True
                elif event.button == 3:  # Right click to remove obstacles
                    node.is_obstacle = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    path = a_star(grid, start, end)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
