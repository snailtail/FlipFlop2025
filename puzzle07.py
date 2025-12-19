"""
FlipFlop 2025 Puzzle 7
"""
from math import comb, factorial

def number_of_shortest_paths(x: int, y: int) -> int:
    return comb(x + y - 2, x - 1)

def number_of_shortest_paths_3d(x: int, y: int, z: int) -> int:
    return factorial(x + y + z - 3) // (
        factorial(x - 1) *
        factorial(y - 1) *
        factorial(z - 1)
    )

def number_of_shortest_paths_n_dimensions(n: int, size: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    if size < 1:
        raise ValueError("size must be >= 1")

    s = size - 1
    N = n * s
    return factorial(N) // (factorial(s) ** n)

def setup(path: str ="testinput_07.dat"):
    with open(path, "r") as f:
        return [(tuple(map(int, line.strip().split()))) for line in f.readlines()]
    

def solve(data: list[tuple[int,...]], part: int = 1):
    if part == 1:
        total_paths = 0
        for x, y in data:
            total_paths += number_of_shortest_paths(x, y)
        return total_paths
    elif part == 2:
        total_paths = 0
        for x, y in data:
            total_paths += number_of_shortest_paths_3d(x, y, x)
        return total_paths
    elif part == 3:
        total_paths = 0
        for n, size in data:
            total_paths += number_of_shortest_paths_n_dimensions(n,size)
        return total_paths

if __name__ == "__main__":
    data = setup("input_07.dat")
    p1_solution = solve(data, part=1)
    print("Part 1:", p1_solution)
    p2_solution = solve(data, part=2)
    print("Part 2:", p2_solution)
    p3_solution = solve(data, part=3)
    print("Part 3:", p3_solution)