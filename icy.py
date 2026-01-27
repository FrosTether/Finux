import os
import time
import random

# The Map: # = Wall, . = Ice, S = Start, $ = Sushi/Gucci (Goal)
LEVEL_1 = [
    "####################",
    "#S.................#",
    "#.###.#####.###.##.#",
    "#.#...#...#.#....#.#",
    "#.###.#.#.#.####.#.#",
    "#.....#.#........#.#",
    "#######.##########.#",
    "#..................#",
    "#.########.#######.#",
    "#..........$.......#",
    "####################"
]

class IceWalk:
    def __init__(self):
        self.grid = [list(row) for row in LEVEL_1]
        self.player_pos = [1, 1] # Start at S
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.moves = 0

    def draw(self):
        os.system('clear')
        print(f"\n❄️  GUCCI MANE'S ICE WALK  ❄️")
        print(f"Moves: {self.moves} | Target: Get the Sushi ($)\n")
        
        for y, row in enumerate(self.grid):
            line = ""
            for x, cell in enumerate(row):
                if [y, x] == self.player_pos:
                    line += "☃ " # You are the Snowman
                elif cell == '#':
                    line += "██" # Wall
                elif cell == '.':
                    line += "░░" # Ice
                elif cell == '$':
                    line += "💰" # The Goal
                else:
                    line += "  "
            print(f"  {line}")
        print("\n[W] Up  [A] Left  [S] Down  [D] Right  [Q] Quit")

    def slide(self, dy, dx):
        self.moves += 1
        sliding = True
        while sliding:
            new_y = self.player_pos[0] + dy
            new_x = self.player_pos[1] + dx
            
            # Check collisions
            if self.grid[new_y][new_x] == '#':
                sliding = False # Hit a wall, stop
                # Play a 'thud' sound if possible
            elif self.grid[new_y][new_x] == '$':
                self.player_pos = [new_y, new_x]
                return True # WINNER
            else:
                # Keep sliding
                self.player_pos = [new_y, new_x]
                self.draw()
                time.sleep(0.1) # Animation delay so you see the slide
        return False

    def play(self):
        while True:
            self.draw()
            try:
                # Get input
                move = input("Slide direction > ").lower().strip()
                
                win = False
                if move == 'w': win = self.slide(-1, 0)
                elif move == 's': win = self.slide(1, 0)
                elif move == 'a': win = self.slide(0, -1)
                elif move == 'd': win = self.slide(0, 1)
                elif move == 'q': break
                
                if win:
                    self.draw()
                    print("\n\n✨ ICE COLD! YOU GOT THE BAG! ✨")
                    # Play the 852Hz victory tone logic here if linked
                    break
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    game = IceWalk()
    game.play()
