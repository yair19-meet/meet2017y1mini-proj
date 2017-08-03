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

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction = UP
    print("You pressed the up key!")

def down():
    global direction
    direction = DOWN
    print("You pressed the down key!")

def left():
    global direction
    direction = LEFT
    print("You pressed the left key!")

def right():
    global direction
    direction = RIGHT
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)    
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()


def make_food():
    
    global food_pos
    global food_stamps
    global SIZE_X
    global SIZE_Y
    global SQUARE_SIZE

    
    min_x = -int(SIZE_X/2/SQUARE_SIZE) + 1
    max_x = int(SIZE_X/2/SQUARE_SIZE) - 1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE) - 1
    max_y = int(SIZE_Y/2/SQUARE_SIZE) + 1

    food_x = random.randint(min_x, max_x) * SQUARE_SIZE
    food_y = random.randint(min_y, max_y) * SQUARE_SIZE


    food.goto(food_x, food_y)
    NewPos = food.pos()
    famp = food.stamp()
    food_pos.append(NewPos)
    food_stamps.append(famp)






def move_snake():
   
    global pos_list
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit() 


    elif direction == RIGHT:
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

    if snake.pos() in pos_list:
        quit()
        
        

    turtle.ontimer(move_snake, TIME_STEP)

    

    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)


    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        
        print("You have eaten the food!")
        make_food()
        

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    


    


turtle.register_shape("trash.gif")

food = turtle.clone()
food.shape("trash.gif")

food_pos = [(100, 100), (-100, 100), (-100, -100), (100, -100)]
food_stamps = []

food.hideturtle()

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    f_stamp = food.stamp()
    food_stamps.append(f_stamp)
    

move_snake()



    
    








