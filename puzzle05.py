"""
FlipFlop 2025 Puzzle 5
"""

def setup(path="testinput05.dat"):
    
    with open(path) as f:
        return f.read().strip()

def solve(data: str, part: int = 1):
    
    if part == 1:    
        idx = 0
        total_steps=0
        while idx >= 0 and idx < len(data):
            tunnel = data[idx]
            other_tunnel_idx = data.find(tunnel,idx+1)
            if other_tunnel_idx == -1:
                other_tunnel_idx = data.find(tunnel,0)
            # will this do?
            steps = abs(idx - other_tunnel_idx)
            total_steps += steps
            idx = other_tunnel_idx +1
        return total_steps
    elif part == 2:
        visited = set()
        idx = 0
        total_steps=0
        while idx >= 0 and idx < len(data):
            tunnel = data[idx]
            visited.add(tunnel)
            other_tunnel_idx = data.find(tunnel,idx+1)
            if other_tunnel_idx == -1:
                other_tunnel_idx = data.find(tunnel,0)
            # will this do?
            steps = abs(idx - other_tunnel_idx)
            total_steps += steps
            idx = other_tunnel_idx +1
        
        not_visited = []
        for c in data:
            if c not in visited and c not in not_visited:
                not_visited.append(c)
        return "".join(not_visited)
        
    elif part == 3:
        idx = 0
        total_steps=0
        while idx >= 0 and idx < len(data):
            tunnel = data[idx]
            other_tunnel_idx = data.find(tunnel,idx+1)
            if other_tunnel_idx == -1:
                other_tunnel_idx = data.find(tunnel,0)
            # will this do?
            steps = abs(idx - other_tunnel_idx)
            if tunnel.isupper():
                steps *= -1

            total_steps += steps
            idx = other_tunnel_idx +1
        return total_steps
    else:
        raise NotImplementedError("Very much not implemented!!!!!")


if __name__ == "__main__":
    data = setup("input05.dat")
    print(data)
    
    p1_result = solve(data,part=1)
    print("Part 1:", p1_result)

    p2_result = solve(data,part=2)
    print("Part 2:", p2_result)

    p3_result = solve(data,part=3)
    print("Part 3:", p3_result)