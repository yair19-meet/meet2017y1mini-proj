import turtle
import random

turtle.tracer(1, 0)

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos += SQUARE_SIZE

    my_pos = (x_pos, y_pos)
    snake.goto(x_pos, y_pos)

    pos_list.append(my_pos)

    STAMP_ID = snake.stamp()
    stamp_list.append(STAMP_ID)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 100

SPACEBAR = "space"

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    move_snake()
    print("You pressed the up key!")

def down():
    global direction
    direction = DOWN
    move_snake()
    print("You pressed the down key!")

def left():
    global direction
    direction = LEFT
    move_snake()
    print("You pressed the left key!")

def right():
    global direction
    direction = RIGHT
    move_snake()
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)    
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left!')
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
    








