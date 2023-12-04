with open("data", "r") as file_handle:
    lines = file_handle.readlines()

card_tracker = {}

def calculate_matches(line):
    winning_numbers, ticket = line.split(": ")[1].strip().split(" | ")
    winning_numbers = [int(number) for number in winning_numbers.split(" ") if number != ""]
    ticket = [int(number) for number in ticket.split(" ") if number != ""]
    matches = len(set(winning_numbers) & set(ticket))
    return matches

def dive_deep(card_id, matches):
    if matches[card_id] > 0:
        for i in range(matches[card_id] ):
            card_tracker[card_id + 1 + i] = card_tracker.get(card_id + 1 + i, 0) + 1
            dive_deep(card_id + 1 + i, matches)

def main():
    matches = [calculate_matches(line) for line in lines]
    for card_id in range(len(lines)):
        dive_deep(card_id, matches)
    return sum(card_tracker.values()) + len(lines)

if __name__ == "__main__":
    print(main())
