
import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Paddle A
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up(): 
	new_y = paddle.ycor() + 20
	paddle.goto(paddle.xcor(), new_y)

def go_down():
	new_y = paddle.ycor() - 20
	paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkeypress(go_up, "Up")

screen.update()
screen.exitonclick() # Close the window on click
