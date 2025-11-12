import turtle
import time

ball_color = input("Choose a ball color (red, blue, green, black, etc.): ")
ball_size = int(input("Choose a ball size (10 (easy) - 50 (hard)): "))

screen = turtle.Screen()
screen.title("Turtle Soccer Game")
screen.bgcolor("green")
screen.tracer(0)

goal = turtle.Turtle()
goal.hideturtle()
goal.penup()
goal.goto(200, 150)
goal.pendown()
goal.pensize(6)
goal.color("white")
goal.forward(120)
goal.right(90)
goal.forward(300)
goal.right(90)
goal.forward(120)

player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2, 2)
player.color("white")
player.penup()
player.goto(-200, 0)
player.setheading(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color(ball_color)
ball.penup()
ball.shapesize(ball_size / 20)
ball.goto(-150, 0)

goalie = turtle.Turtle()
goalie.shape("square")
goalie.color("yellow")
goalie.shapesize(4, 1)
goalie.penup()
goalie.goto(260, 0)


ball_in_motion = False
curve_direction = 0
curve_strength = 4
ball_speed = 10

def move_up():
    if not ball_in_motion:
        player.sety(player.ycor() + 20)
        ball.sety(player.ycor())

def move_down():
    if not ball_in_motion:
        player.sety(player.ycor() - 20)
        ball.sety(player.ycor())

def start_curve_left():
    global curve_direction
    curve_direction = -2

def start_curve_right():
    global curve_direction
    curve_direction = 2

def stop_curve():
    global curve_direction
    curve_direction = 0

def shoot_ball():
    global ball_in_motion
    if ball_in_motion:
        return
    ball_in_motion = True
    target_y = player.ycor()
    ball.setheading(ball.towards(300, target_y))

def goalie_track(target_y):
    if goalie.ycor() < target_y:
        goalie.sety(goalie.ycor() + 5)
    elif goalie.ycor() > target_y:
        goalie.sety(goalie.ycor() - 5)
    goalie.sety(max(-130, min(130, goalie.ycor())))

def show_message(text, color, duration=1.6):
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.color(color)
    msg.penup()
    msg.goto(0, 210)
    msg.write(text, align="center", font=("Arial", 28, "bold"))
    screen.update()
    time.sleep(duration)
    msg.clear()

def reset_ball():
    global ball_in_motion, curve_direction
    ball_in_motion = False
    curve_direction = 0
    ball.goto(-150, player.ycor())
    ball.setheading(0)

def game_loop():
    global ball_in_motion, curve_direction

    if ball_in_motion:
        if curve_direction == -2:
            ball.setheading(ball.heading() + curve_strength)
        elif curve_direction == 2:
            ball.setheading(ball.heading() - curve_strength)

        ball.forward(ball_speed)

        goalie_track(ball.ycor())

        if 200 < ball.xcor() < 320 and -150 < ball.ycor() < 150:
            if abs(ball.ycor() - goalie.ycor()) < 35:
                show_message("BLOCKED!", "red")
                reset_ball()
            else:
                show_message("GOAL!!!", "gold")
                reset_ball()

        if ball.xcor() > 360 or abs(ball.ycor()) > 300:
            show_message("MISSED!", "white")
            reset_ball()

    screen.update()
    screen.ontimer(game_loop, 20)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(shoot_ball, "space")

screen.onkeypress(start_curve_left, "Left")
screen.onkeypress(start_curve_right, "Right")
screen.onkeyrelease(stop_curve, "Left")
screen.onkeyrelease(stop_curve, "Right")

show_message("Move ↑/↓ to aim. Press SPACE to shoot. Hold ← or → to curve!", "white", duration=2.0)
game_loop()
screen.mainloop()






