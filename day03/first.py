with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def check_near_symbol(line_idx, char_idx):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if line_idx + x < 0 or line_idx + x >= len(lines):
                continue
            check_character = lines[line_idx + x][char_idx + y]
            if check_character != '.' and not check_character.isdigit() and not check_character.isspace():
                return True
    return False

def main():
    score = 0
    near_symbol = False
    for line_idx, line in enumerate(lines):
        current_number = []
        for char_idx, character in enumerate(line):
            if character.isdigit():
                current_number.append(character)
                if not near_symbol:
                    near_symbol = check_near_symbol(line_idx, char_idx)
            elif not character.isdigit() and current_number:
                if near_symbol:
                    score += int("".join(current_number))
                current_number = []
                near_symbol = False
    return score

if __name__ == "__main__":
    print(main())
