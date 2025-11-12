import turtle

def tele_turtle(n):
  win = turtle.Screen()
  tele_t = turtle.Turtle()
  for i in range(n):
    move = input("Enter next move: ")
    do_move(tele_t, move)
  win.exitonclick()

def do_move(turt, move):
    if move == 'f':
        turt.forward(15)
    if move == 'b':
        turt.back(15)
    if move == 'r':
        turt.right(90)
    if move == 'l':
        turt.left(90)

move = input("Enter next move: ")
print(move)





