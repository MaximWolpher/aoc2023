import numpy as np

with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def parse_lines(lines):
    return np.array([list(line.strip()) for line in lines])

def expand(grid):
    new_grid_col = grid[:,0].reshape(-1,1)
    for col in range(1, grid.shape[1]):
        new_grid_col = np.concatenate((new_grid_col, grid[:,col].reshape(-1,1)), axis=1)
        if np.all(grid[:,col] == "."):
            new_grid_col = np.concatenate((new_grid_col, np.array(['.' for _ in range(grid.shape[0])]).reshape(-1,1)), axis=1)

    new_grid_row = new_grid_col[0,:].reshape(1,-1)
    for row in range(1, new_grid_col.shape[0]):
        new_grid_row = np.concatenate((new_grid_row, new_grid_col[row, :].reshape(1,-1)), axis=0)
        if np.all(new_grid_col[row,:] == "."):
            new_grid_row = np.concatenate((new_grid_row, np.array(['.' for _ in range(new_grid_col.shape[1])]).reshape(1,-1)), axis=0)

    return new_grid_row

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def all_galaxies(grid):
    return np.argwhere(grid == "#")

def combinations(x):
    idx = np.stack(np.triu_indices(len(x), k=1), axis=-1)
    return x[idx]

def main():
    score = 0
    grid = parse_lines(lines)
    grid = expand(grid)
    galaxies = all_galaxies(grid)
    for galaxy_pair in combinations(galaxies):
        distance = manhattan(galaxy_pair[0], galaxy_pair[1])
        score += distance
    return score
            

if __name__ == "__main__":
    print(main())
