
with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def parse_input(lines):
    times, distances  = [list(map(int, ' '.join(line.split(":")[1].strip().split()).split())) for line in lines]
    return times, distances

def calculate_charge(time, distance):
    counter = 0
    for charge in range((time // 2) + 1):
        final_distance = (time - charge) * charge
        if final_distance > distance:
            counter += 1
    counter *= 2
    if time % 2 == 0:
        counter -= 1
    return counter

def main():
    times, distances = parse_input(lines)
    score = 1
    for race in range(len(times)):
        time = times[race]
        distance = distances[race]
        counter = calculate_charge(time, distance)
        score *= counter
    return score

if __name__ == "__main__":
    print(main())
