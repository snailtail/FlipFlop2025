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
    
    def move_many_seconds(self,seconds: int, grid_size: int = 1000):
        self.xpos = (self.xpos + self.x_speed * seconds) % grid_size
        self.ypos = (self.ypos + self.y_speed * seconds) % grid_size
        
    def __repr__(self):
        return f"Bird {self.id} : x velocity: {self.x_speed}, y velocity {self.y_speed} - currently at {self.xpos},{self.ypos}"

def setup(path="testinput06.dat"):
    with open(path) as f:
        birdlist = []

        for line in f.readlines():
            x, y = map(int, line.strip().split(","))
            birdlist.append(Bird(x, y))

        return birdlist


def solve(
    bird_list: list[Bird], part: int = 1, is_test: bool = True
):
    grid_size = 1000
    frame_size = 500
    seconds_to_process = 100
    window_topleft = ((grid_size - frame_size) // 2) + 1
    window_topright = window_topleft + frame_size - 1

    def get_visible(birds: list[Bird]) -> int:
        return sum([1 for bird in birds if (bird.xpos >= window_topleft  and bird.xpos <= window_topright and bird.ypos >= window_topleft and bird.ypos <= window_topright)])
        
    if is_test:
        grid_size = 8
        frame_size = 4
        seconds_to_process = 8
    if part == 1:
        for bird in bird_list:
            bird.move_many_seconds(seconds_to_process,grid_size)
    
        visible_birds = get_visible(bird_list)
        return visible_birds
    
    elif part == 2:
        total_sum = 0
        for r in range(1000):
            seconds_to_process = 3600
            for bird in bird_list:
                bird.move_many_seconds(seconds_to_process,grid_size)
            
            visible_birds = get_visible(bird_list)
            total_sum += visible_birds
        return total_sum

    elif part == 3:
        total_sum = 0
        for r in range(1000):
            seconds_to_process = 31556926
            for bird in bird_list:
                bird.move_many_seconds(seconds_to_process,grid_size)
            
            visible_birds = get_visible(bird_list)
            total_sum += visible_birds
        return total_sum    


if __name__ == "__main__":
    data_p1 = setup("input06.dat")
    p1_result = solve(data_p1, 1, False)
    print("Part 1:",p1_result)


    data_p2 = setup("input06.dat")
    p2_result = solve(data_p2, 2, False)
    print("Part 2:",p2_result)

    data_p3 = setup("input06.dat")
    p3_result = solve(data_p3, 3, False)
    print("Part 3:",p3_result)
  