import turtle
import random

# Game Configuration
WIDTH, HEIGHT = 600, 600
STEP = 20

def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Ms. Frostman: Legacy Edition")
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0)
    return screen

def create_player():
    player = turtle.Turtle()
    player.shape("circle")
    player.color("yellow")
    player.penup()
    player.speed(0)
    return player

# --- Controller Logic ---
def move_up():
    y = ms_frostman.ycor()
    ms_frostman.sety(y + STEP)

def move_down():
    y = ms_frostman.ycor()
    ms_frostman.sety(y - STEP)

def move_left():
    x = ms_frostman.xcor()
    ms_frostman.setx(x - STEP)

def move_right():
    x = ms_frostman.xcor()
    ms_frostman.setx(x + STEP)

# --- Initialize ---
window = setup_screen()
ms_frostman = create_player()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Game Loop Simulation
print("MS. FROSTMAN IS LIVE. Use W/A/S/D to navigate the Spire.")

while True:
    window.update()
