from turtle import Turtle

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__() # initialize turtle
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0