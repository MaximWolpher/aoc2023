with open("data", "r") as file_handle:
    lines = file_handle.readlines()

def parse_line(line):
    return list(map(int, line.split()))

def diff(sequence: list):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

def main():
    score = 0
    for line in lines:
        sequence = parse_line(line)
        ends = [sequence[0]]
        while any(sequence):
            sequence = diff(sequence)
            ends.append(sequence[0])
        val = 0
        for x in range(1, len(ends) + 1):
            val = ends[-x] - val
        score += val
    return score
            

if __name__ == "__main__":
    print(main())
