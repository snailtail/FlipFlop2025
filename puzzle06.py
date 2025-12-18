"""
FlipFlop 2025 Puzzle 6
"""


class Bird:
    id_counter: int = 1

    def __init__(self, x_speed: int, y_speed: int, xpos: int = 0, ypos: int = 0):
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.xpos = xpos
        self.ypos = ypos
        self.id = Bird.id_counter
        Bird.id_counter += 1

    def move(self, grid_size: int):
        self.xpos = (self.xpos + self.x_speed) % grid_size
        self.ypos = (self.ypos + self.y_speed) % grid_size

    def __repr__(self):
        return f"Bird {self.id} : x velocity: {self.x_speed}, y velocity {self.y_speed} - currently at {self.xpos},{self.ypos}"

def setup(path="testinput06.dat"):
    with open(path) as f:
        # return [tuple(map(int,x)) for x in line.strip().split(",")] for line in f.readlines()]
        birdlist = []

        for line in f.readlines():
            x, y = map(int, line.strip().split(","))
            birdlist.append(Bird(x, y))

        return birdlist


def solve(
    bird_list: list[tuple[int, int, int, int]], part: int = 1, is_test: bool = True
):
    grid_size = 1000
    frame_size = 500
    seconds_to_process = 100

    if is_test:
        grid_size = 8
        frame_size = 4
        seconds_to_process = 8

    for s in range(seconds_to_process):
        print(f"Second {s + 1}")

        for bird in bird_list:
            bird.move()
            print(bird)


if __name__ == "__main__":
    data = setup("testinput06.dat")
    print(data)
#    p1_result = solve(data, 1, True)
