# Advent of Code 2022, Day 1

file = open("/home/adam/devel/adventofcode2022/day1/input.txt", "r")
buffer: str = file.read()
file.close()

split_numbers: list[str] = buffer.split("\n\n")
elves: list[int] = []
for numbers in split_numbers:
    total: int = 0
    calories: list[str] = numbers.split("\n")
    for value in calories:
        total = total + int(value)
    elves.append(total)

elves.sort(reverse=True)
print("Part one: " + str(elves[0]))

# part two
print("Part two: " + str(elves[0] + elves[1] + elves[2]))
