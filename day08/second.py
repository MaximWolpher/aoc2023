from math import lcm

START_NODE = 'A'
END_NODE = 'Z'

with open("data", "r") as file_handle:
    lines = file_handle.readlines()

class Node:
    def __init__(self, node, instruction_L, instruction_R):
        self.node = node
        self.L = instruction_L
        self.R = instruction_R

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
    all_starts = [node for node in network.keys() if node[-1] == START_NODE]
    all_steps = []
    for start in all_starts:
        current_node = network[start]
        step_counter = 0
        while not current_node.node[-1] == END_NODE:
            for instruction in instructions:
                current_node = network[getattr(current_node, instruction)]
                step_counter += 1
        all_steps.append(step_counter)
    return lcm(*all_steps)

if __name__ == "__main__":
    print(main())
