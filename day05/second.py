with open("data", "r") as file_handle:
    lines = file_handle.read()

def parse_input(lines):
    lines = lines.split("\n")
    initial_seeds = lines[0].split(": ")[1].strip().split(" ")
    initial_seeds = [int(seed) for seed in initial_seeds]

    lines = "\n".join(lines[2:])

    maps = {}
    map_name = ""
    for map_section in lines.split("\n\n"):
        for line in map_section.splitlines():
            if line.endswith(":"):
                map_name = line[:-5]
                maps[map_name] = []
            else:
                destination_start, source_start, range_length = map(int, line.split(" "))
                values = {"source_start": source_start, "source_end": source_start + range_length - 1, "difference": destination_start - source_start}
                maps[map_name].append(values)
    return initial_seeds, maps

        

def main():
    initial_seeds, maps = parse_input(lines)
    locations = []
    end = "location"
    current = "seed"
    for seed in initial_seeds:
        while True:
            if current == end:
                locations.append(seed)
                current = "seed"
                break
            map_name = [map_name for map_name in maps.keys() if map_name.startswith(current)][0]
            current = map_name.split("-to-")[1]

            for map_range in maps[map_name]:
                if map_range["source_start"] <= seed <= map_range["source_end"]:
                    seed = seed + map_range["difference"]
                    break
    return min(locations)


if __name__ == "__main__":
    print(main())
