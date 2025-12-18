"""
FlipFlop 2025 Puzzle 2
"""

from functools import lru_cache
import re


def setup(path="testinput02.dat"):
    with open(path) as f:
        return [c for c in f.read().strip()]


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)


def get_value_for_direction(direction: str) -> int:
    if direction == "^":
        return 1
    if direction == "v":
        return -1


def solve(chars: list[str], part: int = 1):
    if part == 1:
        height = 0
        max_height = 0
        for c in chars:
            height += get_value_for_direction(c)
            max_height = max(height, max_height)
        return max_height

    elif part == 2:
        height = 0
        max_height = 0
        down_count = 1
        up_count = 1
        lastchar = chars[0]
        for c in chars:
            if c != lastchar:
                down_count = 1
                up_count = 1
            if c == "^":
                height += up_count
                up_count += 1
            elif c == "v":
                height -= down_count
                down_count += 1
            max_height = max(height, max_height)
            lastchar = c

        return max_height

    elif part == 3:
        # count consecutive up's and downs.
        # when direction changes - do fib(count) and add to height
        height = 0
        max_height = 0
        direction_as_string = "".join(chars)
        search = re.findall(r"(\^+)|(v+)", direction_as_string)
        if search:
            for dir in search:
                max_len = max(len(dir[0]), len(dir[1]))
                value = fib(max_len)

                if "^" in dir[0] or "^" in dir[1]:
                    height += value
                else:
                    height -= value
                max_height = max(height, max_height)

        return max_height


if __name__ == "__main__":
    data = setup("input02.dat")
    print("Part 1:", solve(data, part=1))
    print("Part 2:", solve(data, part=2))
    print("Part 3:", solve(data, part=3))
