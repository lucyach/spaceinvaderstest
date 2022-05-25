from processing import *


class Ship:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.width = 40
    self.height = 40
    self.imageName = "ship5.png"
    
  def loadImg(self):
    self.img = loadImage(self.imageName)
  
  def move(self):
    self.x = mouseX
    #don't allow to go too far
    if self.x > 510:
      self.x = 510
    
  def draw(self):
    image(self.img, self.x, self.y, self.width, self.height)
