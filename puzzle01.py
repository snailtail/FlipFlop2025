"""
FlipFlop 2025 Puzzle 1
"""


def setup(path = "input01.dat"):
    with open(path) as f:
        return [line.strip() for line in f.readlines()]
    

def solve(data: list[str], part2: bool = False, part3: bool = False):
    count = 0
    for row in data:
        rowsum = 0
        rowsum += row.count("ba")
        rowsum += row.count("ne")
        rowsum += row.count("na")
        if part3:
            if "ne" in row:
                continue
            else:
                count += rowsum
        elif part2:
            if rowsum % 2 == 0:
                count += rowsum

        else:
            count += rowsum
    return count

if __name__ == "__main__":

    data = setup("input01.dat")
    print("Part 1:", solve(data))
    print("Part 2:", solve(data,part2=True))
    print("Part 3:", solve(data,part3=True))