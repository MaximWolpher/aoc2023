with open("data", "r") as file_handle:
    lines = file_handle.read().splitlines()

def parse_game(line):
    draw_results = []
    game, draws = line.split(": ")
    game_id = int(game.split(" ")[1])
    draws = draws.split("; ")
    for draw in draws:
        color_map = {}
        colors = draw.split(", ")
        for color in colors:
            count, color_name = color.split(" ")
            color_map[color_name] = int(count)
        draw_results.append(color_map)

    return game_id, draw_results

def main():
    score = 0
    
    for line in lines:
        impossible = False
        game_id, draw_results = parse_game(line)
        for draw in draw_results:
            if draw.get("red") and draw["red"] > 12:
                impossible = True
                break
            elif draw.get("blue") and draw["blue"] > 14:
                impossible = True
                break
            elif draw.get("green") and draw["green"] > 13:
                impossible = True
                break
        if not impossible:
            score += game_id
    return score

if __name__ == "__main__":
    print(main())
    
