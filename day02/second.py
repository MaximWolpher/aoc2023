with open("data", "r") as file_handle:
    lines = file_handle.read().splitlines()

def parse_game(line):
    color_map = {"red": [], "green": [], "blue": []}
    _, draws = line.split(": ")
    draws = draws.split("; ")
    for draw in draws:
        colors = draw.split(", ")
        for color in colors:
            count, color_name = color.split(" ")
            color_map[color_name].append(int(count))

    return color_map

def main():
    score = 0
    for line in lines:
        power = 1
        color_map = parse_game(line)
        for _, draws in color_map.items():
            power *= max(draws)
        score += power
    return score

if __name__ == "__main__":
    print(main())
    
