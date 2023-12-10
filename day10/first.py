import networkx as nx


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

with open("data", "r") as file_handle:
    lines = file_handle.readlines()

connection_map = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "7": [LEFT, DOWN],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "F": [DOWN, RIGHT],
    "S": [UP, DOWN, LEFT, RIGHT]
}


class Node:
    def __init__(self, value: str, coordinates: tuple):
        self.value = value
        self.connections = []
        self.visited = False
        self.distance = None
        self.openings = connection_map[value]
        self.coordinates = coordinates
    def __repr__(self) -> str:
        return self.value

def parse_line(lines):
    return [list(line.strip())for line in lines]

def sum_tuples(a, b):
    return tuple(map(sum, zip(a, b)))

def get_start(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                return Node("S", (row, col))
            
def check_opening_match(node1: Node, node2: Node, direction: tuple):
    negative_direction = tuple(map(lambda x: x * -1, direction))
    if direction in node1.openings and negative_direction in node2.openings:
        return True
    else:
        return False

def get_connections(grid, node: Node):
    connections = []
    for direction in connection_map[node.value]:
        new_location = sum_tuples(node.coordinates, direction)
        value = grid[new_location[0]][new_location[1]]
        if value == ".":
            continue
        try:
            neighbor = Node(value, new_location)
        except IndexError:
            continue
        if neighbor.value not in (".") and check_opening_match(node, neighbor, direction):
            connections.append(neighbor)
    return connections

def generate_graph(start, grid):
    graph = nx.Graph()
    visited = set()
    stack = []
    stack.append(start)
    current = start
    while stack:
        current = stack.pop()
        if current.coordinates in visited:
            continue
        connections = get_connections(grid, current)
        for connection in connections:
            if connection.coordinates in visited:
                continue
            graph.add_edge(current, connection)
            stack.append(connection)
            visited.add(current.coordinates)
            if current.value == start.value:
                continue
    return graph    

def main():

    grid = parse_line(lines)
    start = get_start(grid)

    graph = generate_graph(start, grid)
    score = (len(graph.nodes)) // 2
    return score
            

if __name__ == "__main__":
    print(main())
