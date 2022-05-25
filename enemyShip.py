from processing import *


class EnemyShip:
  def __init__(self, x, y, type):
    self.x = x
    self.y = y
    self.type = type
    if type is "REGULAR":
      self.hitPoints = 3
      self.height = 25
      self.width = 45
      self.imageName = "spaceship-small.png"
      self.speed = -4
    else:
      self.hitPoints = 15
      self.height = 80
      self.width = 100
      self.imageName = "spaceship6.png"
      self.speed = -2

  def loadImg(self):
    self.img = loadImage(self.imageName)

  def takeDamage(self):
    self.hitPoints =  self.hitPoints - 1

  def isAlive(self):
    return self.hitPoints > 0
	
  def draw(self):
    image(self.img, self.x, self.y, self.width,self.height)

  def moveShip(self):
    self.x = self.x + self.speed
    
    if self.x <= 0 or self.x >= 530:
      self.speed = -self.speed
      self.y = self.y + 30
    #YOUR CODE HERE
    #make the space ships bounce off the side and go back the other way
