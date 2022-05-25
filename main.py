from processing import *
from bullet import Bullet
from ship import Ship
from enemyShip import EnemyShip
import random


#non changing variables
width = 550
height = 450
enemies_per_row = 7
enemy_rows = 2
enemy_sep = 30


#changing variables
class gameState:
  gameOver = False
gs = gameState()
boss = EnemyShip(250, 10, "BOSS")
player = Ship(350, 400)
enemies = []
enemyBullets = []
bullets = []


def createEnemies():
  enemies_per_row = 7
  enemy_rows = 2
  enemy_sep = 60
  
  localY = 135
  for i in range(0, enemy_rows):
    localX = 100
    for i in range(0, enemies_per_row):
      enemy = EnemyShip(localX, localY, "REGULAR")
      localX += enemy_sep
      enemies.append(enemy)
    localY += enemy_sep

  #YOUR CODE HERE
  #create rows of enemies using the variables enemies_per_row, enemy_rows, enemy_sep
  enemies_per_row = 5
  enemy_rows = 2
  enemy_sep = 20



def enemiesShoot():
  #YOUR CODE HERE
  #randomly decide if each spaceship should shoot
  #try 1 in 50 odds a regular ship shoots, 1 in 25 for boss
  if random.randint(0, 50) == 4 and len(enemies) > 0:
    randomEnemy = random.randint(0, len(enemies))
    ebullet = Bullet(enemies[randomEnemy-1].x, enemies[randomEnemy-1].y, "enemy")
    enemyBullets.append(ebullet)
  
  if random.randint(0, 25) == 4 and boss != None:
    bbullet = Bullet(boss.x+40, boss.y+60, "enemy")
    enemyBullets.append(bbullet)
  pass


def moveEverything():
  player.move()
  boss.moveShip()
  
  for i in range(len(bullets)):
    if i < len(bullets):
      currBullet = bullets[i]
      currBullet.move()
    
      if currBullet.y <= 0:
        bullets.remove(currBullet)
  
  for i in range(len(enemies)):
    currentEnemy = enemies[i]
    currentEnemy.moveShip()

  #YOUR CODE HERE
  #move the enemy bullets and remove if they go off the screen
  for i in range(len(enemyBullets)):
    enemyBullets[i].move()


def drawEverything():
  player.draw()
  if boss.isAlive():
    boss.draw()
    
  for i in range(len(bullets)):
    currBullet = bullets[i]
    currBullet.draw()
    
  for i in range(len(enemies)):
    currentEnemy = enemies[i]
    currentEnemy.draw()
    
  for i in range(len(enemyBullets)):
    currEnBullet = enemyBullets[i]
    currEnBullet.draw()
  

def getEnemyAt(x, y):
  for i in range(len(enemies)):
    if pointInRect(x, y, enemies[i].x, enemies[i].y, enemies[i].width, enemies[i].height):
      return enemies[i]
      
  if boss.isAlive() and pointInRect(x, y, boss.x, boss.y, boss.width, boss.height):
      return boss
      
  return None
  
  
def checkBulletCollisions():
  for i in range(len(bullets)):
    if i < len(bullets):
      currBullet = bullets[i]
    
      collObj = getEnemyAt(currBullet.x + 2, currBullet.y + 2)
    
      if collObj is not None:
        collObj.takeDamage()
        if not collObj.isAlive():
          if collObj is not boss:
            enemies.remove(collObj)
        
        bullets.remove(currBullet)
    
  #YOUR CODE HERE
  #check if enemy bullets hit the player (hint: use pointInRect)
  for i in range(0, len(enemyBullets)):
    if pointInRect(enemyBullets[i].x, enemyBullets[i].y, player.x, player.y, player.width, player.height):
      gs.gameOver = True


#if an ememy ship collided with the player ship
def checkTouchingShip():
  for i in range(len(enemies)):
    if pointInRect(player.x + player.width/2, player.y + player.height/2, enemies[i].x, enemies[i].y, enemies[i].width, enemies[i].height):
      gs.gameOver = True


def pointInRect(pt_x, pt_y, rect_x, rect_y, rect_w, rect_h):
  if (pt_x > rect_x) and (pt_x < rect_x + rect_w) and (pt_y > rect_y) and (pt_y < rect_y + rect_h):
    return True
  else:
    return False


def mousePressed():
  #not game over
  if not gs.gameOver:
    #last bullet has moved 30 pixels
    if bullets == [] or bullets[len(bullets)-1].y < player.y - 30:
      newBullet = Bullet(player.x + player.width/2, player.y, "mine")
      bullets.append(newBullet)


def setup():
  size(width, height)
  createEnemies()
  frameRate(30)
  #load all the images here so it just happens once (but after processing initiates)
  player.loadImg()
  boss.loadImg()
  for i in range(len(enemies)):
    currentEnemy = enemies[i]
    currentEnemy.loadImg()


def draw():
  background(0, 0, 0)
  

  if len(enemies) == 0 and boss.isAlive() == False:
    gs.gameOver = True

  if not gs.gameOver:
    enemiesShoot()
    moveEverything()
    checkBulletCollisions()
    checkTouchingShip()
  else:
    fill(255, 0, 0)
    textSize(35)
    text("Game Over", 195, 220) 
    
  drawEverything()

  
run()