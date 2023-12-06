with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def parse_input(lines):
    time, distance  = [int(''.join(line.split(":")[1].strip().split())) for line in lines]
    return time, distance

def calculate_charge(time, distance):
    counter = 0
    for charge in range((time // 2) + 1):
        final_distance = (time - charge) * charge
        if final_distance <= distance:
            counter += 1
        else:
            break
    counter *= 2
    if time % 2 == 0:
        counter -= 1
    return time - counter


def main():
    time, distance = parse_input(lines)
    score = calculate_charge(time, distance)
    return score

if __name__ == "__main__":
    print(main())
