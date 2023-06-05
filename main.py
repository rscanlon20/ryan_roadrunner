
import sys

import pygame, random
from pygame.locals import *
from player import Player
from enemies import Enemy

from player import Player

def reset():
    global score, alive
    score = 0
    alive = True
    p1.rect.x = (width / 2) - p1.image.get_width() / 2
    p1.rect.y = height / - p1.image.get_height() + 400
    p1.lives = 3
    create_enemies()

def create_enemies():
    enemies.empty()
    for i in range(10):
        e1 = Enemy()
        enemies.add(e1)

pygame.init()

fps =60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

background = pygame.image.load("image/roadrunner.background.jpeg")


# Game loop.

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()









font = pygame.font.SysFont(None, 24)

score = 0








p1 = Player((random.randint(0,255),random.randint(0,255),random.randint(0,255)),width / 2, height / 2)
all_sprites = pygame.sprite.Group()

p1 = Player((255,0,0), 255, 255)
all_sprites.add(p1)
alive = True

create_enemies()





while True:

  screen.fill((0,0 , 0))

  keys = pygame.key.get_pressed()
  for sprite in all_sprites:
    sprite.move(keys)





  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          #b1, b2 = p1.shoot() actual code
          b1 = p1.shoot()
          bullets.add(b1)
          #bullets.add(b2)
        if event.key == pygame.K_r and not alive:
            reset()


# Update.
  for enemy in enemies:
      enemy.move()

  for bullet in bullets:
      bullet.move()
      collided_enemy = pygame.sprite.spritecollideany(bullet, enemies)
      if collided_enemy != None:
          score += 1
          enemies.remove(collided_enemy)
          bullets.remove(bullet)

  collidedenemy = pygame.sprite.spritecollideany(p1, enemies)
  if collidedenemy != None:
      enemies.remove(collidedenemy)
      alive = p1.lose_life()










  # Draw.
# Drawing Rectangle
#  pygame.draw.rect(screen, (200,0,0), pygame.Rect(x, y, r_width, r_height))
  if alive:
      screen.blit(background, (0, 0))
      all_sprites.draw(screen)
      enemies.draw(screen)
      bullets.draw(screen)
      score_board = font.render('Score:' + str(score), True, (0,0,0))
      lives_board = font.render('Lives:' + str(p1.lives), True, (0,0,0))
      screen.blit(score_board,(10,10))
      screen.blit(lives_board,(10,50))

  else:
      game_over = font.render("Game over", True, (255,255,255))
      restart = font.render("Press R to Restart", True, (255,255,255))
      screen.blit(restart, (screen.get_width()//2 - 75, screen.get_height()//2))
      screen.blit(game_over, (screen.get_width()//2 - 50, screen.get_height()//2.2))
  pygame.display.flip()
  fpsClock.tick(fps)


