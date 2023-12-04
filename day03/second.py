with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def check_near_gear(line_idx, char_idx):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if line_idx + x < 0 or line_idx + x >= len(lines):
                continue
            check_character = lines[line_idx + x][char_idx + y]
            if check_character == '*':
                # Index of the gear
                return f"{(line_idx + x) * len(lines[0]) + char_idx + y}"
    return False

def calculate_gear_ratio(gear_map):
    score = 0
    for gear_list in gear_map.values():
        if len(gear_list) == 2:
            score += gear_list[0] * gear_list[1]
    return score

def main():
    near_symbol = False
    gear_map = {}
    for line_idx, line in enumerate(lines):
        current_number = []
        for char_idx, character in enumerate(line):
            if character.isdigit():
                current_number.append(character)
                if not near_symbol:
                    near_symbol = check_near_gear(line_idx, char_idx)
            elif not character.isdigit() and current_number:
                if near_symbol:
                    if not gear_map.get(near_symbol):
                        gear_map[near_symbol] = []
                    gear_map[near_symbol].append(int("".join(current_number)))
                current_number = []
                near_symbol = False
    score = calculate_gear_ratio(gear_map)
    return score

if __name__ == "__main__":
    print(main())
