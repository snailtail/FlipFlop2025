"""
FlipFlop 2025 Puzzle 7
"""
from math import comb

def number_of_shortest_paths(x: int, y: int) -> int:
    return comb(x + y - 2, x - 1)

