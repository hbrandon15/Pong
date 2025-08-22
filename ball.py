from turtle import Turtle


class Ball(Turtle): 
	def __init__(self): # define the ball
		super().__init__() # initialize the turtle
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x_move = 10
		self.y_move = 10

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1 # reverse y direction

	def bounce_x(self):
		self.x_move *= -1 # reverse x direction

	def reset_position(self):
		self.goto(0, 0)
		self.bounce_x() # send the ball in the opposite direction

	def wall_bounce(self): 
		if self.ycor() > 280 or self.ycor() < -280:
			self.bounce_y()