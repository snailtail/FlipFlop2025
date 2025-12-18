"""
FlipFlop 2025 Puzzle 4
"""

def setup(path="testinput04.dat"):
    
    with open(path) as f:
        return [tuple(int(x) for x in line.strip().split(",")) for line in f.readlines()]


def manhattan_distance(pos1: tuple[int,int], pos2: tuple[int,int]) -> int:
    x1,y1 = pos1
    x2, y2 = pos2
    xdist = abs(x1-x2)
    ydist = abs(y1-y2)
    return xdist+ydist


def diag_distance(pos1: tuple[int,int], pos2: tuple[int,int]) -> int:
    x1,y1 = pos1
    x2, y2 = pos2
    xdist = abs(x1-x2)
    ydist = abs(y1-y2)
    return max(xdist,ydist)


def solve(data: list[tuple[int,int]], part: int = 1) -> int:

    if part == 1:
        total_distance = 0
        active_pos = (0,0)
        for idx in range(len(data)):
            next_pos = data[idx]
            total_distance += manhattan_distance(active_pos,next_pos)
            active_pos = next_pos
        return total_distance
    
    elif part == 2:
        total_distance = 0
        active_pos = (0,0)
        for idx in range(len(data)):
            next_pos = data[idx]
            total_distance += diag_distance(active_pos,next_pos)
            active_pos = next_pos
        return total_distance
    elif part == 3:
        sorted_data = sorted(
            data,
            key=lambda p: manhattan_distance(p, (0, 0))
        )
        total_distance = 0
        active_pos = (0,0)
        for idx in range(len(sorted_data)):
            next_pos = sorted_data[idx]
            total_distance += diag_distance(active_pos,next_pos)
            active_pos = next_pos
        
        return total_distance        


if __name__ == "__main__":
    data = setup("input04.dat")
    p1_result = solve(data,part=1)
    print("Part 1:", p1_result)
    
    p2_result = solve(data,part=2)
    print("Part 2:", p2_result)

    p3_result = solve(data,part=3)
    print("Part 3:", p3_result)