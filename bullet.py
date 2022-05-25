from processing import *


class Bullet:
	def __init__(self, spaceshipX, spaceshipY, type):
	  self.x = spaceshipX
	  self.y = spaceshipY
	  self.type = type

	  if type == "enemy":
	    self.speed = 6
	  else:
	    self.speed = -8
	
	def move(self):
	  self.y = self.y + self.speed
	  
	def draw(self):
	  if self.type == "enemy":
	    fill(255, 0, 0)
	  else:
	    fill(255, 255, 255)
	  noStroke()
	  ellipse(self.x, self.y, 5, 5)
	  
