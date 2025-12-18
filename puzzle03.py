"""
FlipFlop 2025 Puzzle 3
"""

def setup(path="testinput03.dat"):
    
    with open(path) as f:
        return [tuple(x for x in line.strip().split(",")) for line in f.readlines()]

def solve(data: list[tuple[int,int,int]], part: int = 1):

    if part == 1:
        colors = {}
        for item in data:
            if item in colors:
                colors[item]+=1
            else:
                colors[item]=1
        sorted_colors = sorted(colors.items(), key=lambda kv: (kv[1], kv[0]))
        r,g,b = sorted_colors[-1][0] 
        return r,g,b

    elif part == 2:
        colors = []
        for r,g,b in data:
            if r == g or r == b or g == b:
                colors.append("special")
            elif r < g < b or g < r < b :
                colors.append("blue")
            elif r < b < g or b < r < g:
                colors.append("green")
            elif g < b < r or b < g < r:
                colors.append("red")
        return sum(1 for x in colors if x == 'green')


    elif part == 3:
        colors = []
        for r,g,b in data:
            if r == g or r == b or g == b:
                colors.append("special")
            elif r < g < b or g < r < b :
                colors.append("blue")
            elif r < b < g or b < r < g:
                colors.append("green")
            elif g < b < r or b < g < r:
                colors.append("red")
        red_sum = sum(5 for x in colors if x == 'red')
        green_sum = sum(2 for x in colors if x == 'green')
        blue_sum = sum(4 for x in colors if x == 'blue')
        special_sum = sum(10 for x in colors if x == 'special')
        return red_sum + green_sum + blue_sum + special_sum

    else:
        raise NotImplementedError("Oh boy this should never happen..! part equals:",part)
if __name__ == "__main__":
    data = setup("input03.dat")
    print("Part 1:",",".join([x for x in solve(data,part=1)]))
    print("Part 2:", solve(data,part=2))
    print("Part 3:", solve(data,part=3))