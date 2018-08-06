import turtle
turtle.goto(0,0)

def up():
    global direction
    print("You pressed the up key.")
    
turtle.onkey(up, "Up") 
turtle.listen()

def on_move():
   up = 100
   turtle.goto(100,0)
   turtle.left
   turtle.goto(100, -100)
   turtle.down
   turtle.goto(-100, -100)
