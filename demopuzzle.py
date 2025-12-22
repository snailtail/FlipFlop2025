
from collections import Counter # this will help us count stuff

nums = []
with open("input_demo.dat", "r") as f:
    nums = [int(line.strip()) for line in f.readlines()]

print(f"Part 1: {sum(nums)}")

#part 2 just a mean
print(f"Part 2: {round(sum(nums) / len(nums))}")

p3_data = Counter(nums)
p3_sorted = sorted(p3_data.items(), key=lambda x: x[1], reverse=True)
most_common = p3_sorted[0]

digit_counts = Counter("".join(map(str, nums)))
p3_least_common_digit = sorted(digit_counts.items(), key=lambda x: x[1])[0]

print(f"Part 3: {most_common[0]}{p3_least_common_digit[0]}")
