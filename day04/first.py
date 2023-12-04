with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def calculate_matches(line):
    winning_numbers, ticket = line.split(": ")[1].strip().split(" | ")
    winning_numbers = [int(number) for number in winning_numbers.split(" ") if number != ""]
    ticket = [int(number) for number in ticket.split(" ") if number != ""]
    matches = len(set(winning_numbers) & set(ticket))
    return matches

def main():
    score = 0
    for line in lines:
        matches = calculate_matches(line)
        if matches > 0:
            score += 2**(matches-1)
    return score

if __name__ == "__main__":
    print(main())
