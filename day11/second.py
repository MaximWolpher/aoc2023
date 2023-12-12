import numpy as np

with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def parse_lines(lines):
    return np.array([list(line.strip()) for line in lines])

def find_gaps(grid):
    rows, cols = [], []
    for col in range(grid.shape[1]):
        if np.all(grid[:,col] == "."):
            cols.append(col)

    for row in range(grid.shape[0]):
        if np.all(grid[row,:] == "."):
            rows.append(row)

    return rows, cols

def expand(galaxies, gap_rows, gap_cols, expand_factor=2):
    for idx in range(len(galaxies)):
        galaxies[idx][0] += len(np.where(gap_rows < galaxies[idx][0])[0]) * (expand_factor - 1)
        galaxies[idx][1] += len(np.where(gap_cols < galaxies[idx][1])[0]) * (expand_factor - 1)
    return galaxies

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
    gap_rows, gap_cols = find_gaps(grid)
    galaxies = all_galaxies(grid)
    galaxies = expand(galaxies, gap_rows, gap_cols, 1000000)
    for galaxy_pair in combinations(galaxies):
        distance = manhattan(galaxy_pair[0], galaxy_pair[1])
        score += distance
    return score
            

if __name__ == "__main__":
    print(main())
