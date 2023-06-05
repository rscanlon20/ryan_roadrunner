import pygame
import random
from bullet import Bullet

class Player(pygame.sprite.Sprite):

        def __init__(self, colour, x, y):
            pygame.sprite.Sprite.__init__(self)
            # self.image = pygame.Surface((10, 10))
            # self.image.fill(colour)
            self.image = pygame.image.load("image/roadrunner_idle.png")
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()

            self.speed = 5
            self.rect.x = x
            self.rect.y = y
            self.sound0bj = pygame.mixer.Sound('sounds/laser.wav')
            self.lives = 3

        def lose_life(self):
            self.lives -= 1
            print(self.lives)
            if self.lives <= 0:
                return False
            else:
                return True


        def move(self, keys):
            self.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
            self.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.speed

        def randomMove(self):
            self.rect

        def shoot(self):
            self.sound0bj.play()
            b1 = Bullet(5, self.rect.x + 26, self.rect.y)
            #b2 = Bullet(5, self.rect.x + self.rect.width -5, self.rect.y)
            return b1, #b2
