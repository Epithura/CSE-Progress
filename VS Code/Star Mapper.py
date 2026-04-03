import math
grid1=[]
grid=[]
for i in range(10):
    a=input("")
    row = list(a)  # Take a row as input
    grid1.append(row)
for i in range(10):
    sublist=[char for char in grid1[i]]    
    grid.append(sublist)
def parse_grid(grid):
    """Parses the grid to find star positions."""
    star_positions = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "#":
                star_positions.append((r, c))
    return star_positions

def expand_universe(grid, star_positions):
    """Expands the grid by doubling empty rows and columns."""
    rows = len(grid)
    cols = len(grid[0])
    
    # Identify empty rows and columns
    empty_rows = {r for r in range(rows) if '#' not in grid[r]}
    empty_cols = {c for c in range(cols) if all(grid[r][c] == '.' for r in range(rows))}
    
    # Adjust positions with expansion
    expanded_positions = []
    for r, c in star_positions:
        new_r = r + sum(1 for er in empty_rows if er < r)  # Adjust for empty rows
        new_c = c + sum(1 for ec in empty_cols if ec < c)  # Adjust for empty columns
        expanded_positions.append((new_r, new_c))
    
    return expanded_positions

def manhattan_distance(p1, p2):
    """Computes Manhattan distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_distances(expanded_positions):
    """Finds the shortest and longest Manhattan distances between all pairs."""
    min_dist = float('inf')
    max_dist = float('-inf')
    
    for i in range(len(expanded_positions)):
        for j in range(i + 1, len(expanded_positions)):
            dist = manhattan_distance(expanded_positions[i], expanded_positions[j])
            min_dist = min(min_dist, dist)
            max_dist = max(max_dist, dist)
    
    return min_dist, max_dist
# Process input
star_positions = parse_grid(grid)
expanded_positions = expand_universe(grid, star_positions)
min_distance, max_distance = find_distances(expanded_positions)
print(math.floor(min_distance), math.floor(max_distance),end="")
