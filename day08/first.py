START_NODE = 'AAA'
END_NODE = 'ZZZ'

with open("data", "r") as file_handle:
    lines = file_handle.readlines()

class Node:
    def __init__(self, node, instruction_L, instruction_R):
        self.node = node
        self.L = instruction_L
        self.R = instruction_R

    def __eq__(self, other):
        return self.node == other.node

def parse_lines(lines: list):
    network = {}
    instructions = list(lines[0].strip())
    for line in lines[2:]:
        node, children = line.split(" = ")
        instruction_L, instruction_R = children.split(", ")
        network[node] = (Node(node, instruction_L[1:], instruction_R[:-2]))    
    return instructions, network

def main():
    instructions, network = parse_lines(lines)
    current_node = network[START_NODE]
    goal_node = network[END_NODE]
    step_counter = 0

    while not current_node == goal_node:
        for instruction in instructions:
            step_counter += 1
            current_node = network[getattr(current_node, instruction)]
    return step_counter


if __name__ == "__main__":
    print(main())
