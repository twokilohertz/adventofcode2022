# Advent of Code 2022, Day 2

def part_one(buffer: str):
    rps_games: list[str] = buffer.split("\n")

    total: int = 0
    for game in rps_games:
        moves: list[str] = game.split(" ")
        score: int = 0

        # Increase score for move chosen
        match moves[1]:
            case "X":
                score = score + 1
            case "Y":
                score = score + 2
            case "Z":
                score = score + 3
            case _:
                pass
        
        # Win case
        if moves[0] == "C" and moves[1] == "X":
            score = score + 6
            total = total + score
            continue
        if moves[0] == "B" and moves[1] == "Z":
            score = score + 6
            total = total + score
            continue
        if moves[0] == "A" and moves[1] == "Y":
            score = score + 6
            total = total + score
            continue

        # Draw case (ugly!)
        if (moves[0] == "A" and moves[1] == "X") or (moves[0] == "B" and moves[1] == "Y") or (moves[0] == "C" and moves[1] == "Z"):
            score = score + 3

        total = total + score

    print("Part one: " + str(total))

def part_two(buffer: str):
    rps_games: list[str] = buffer.split("\n")

    total: int = 0
    for game in rps_games:
        moves: list[str] = game.split(" ")
        score: int = 0

        # lose, draw or win
        match moves[1]:
            case "X":
                if moves[0] == "A":
                    score = score + 3
                if moves[0] == "B":
                    score = score + 1
                if moves[0] == "C":
                    score = score + 2
            case "Y":
                score = score + 3

                if moves[0] == "A":
                    score = score + 1
                if moves[0] == "B":
                    score = score + 2
                if moves[0] == "C":
                    score = score + 3
            case "Z":
                score = score + 6

                if moves[0] == "A":
                    score = score + 2
                if moves[0] == "B":
                    score = score + 3
                if moves[0] == "C":
                    score = score + 1
            case _:
                pass

        total = total + score

    print("Part two: " + str(total))

if __name__ == "__main__":
    file = open("/home/adam/devel/adventofcode2022/day2/input.txt", "r")
    buffer: str = file.read()
    file.close()

    part_one(buffer)
    part_two(buffer)
