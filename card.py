import pygame
from constants import CARD_RISE

class Card(pygame.sprite.Sprite):
  def __init__(self, x = 0, y = 0, index = 0):
    super().__init__()
    self.image = pygame.image.load("sprites\parchment-card-bg.png").convert_alpha()
    self.rect = self.image.get_rect(center = (x, y))
    self.x = x
    self.y = y
    self.yMove = pygame.math.Vector2(0, 0)
    self.index = index
    self.hovering = False
    self.following = False
    self.placed = False

  def setLayer(self, layer):
    group = self.groups()[0]
    self.index = layer
    group.change_layer(self, layer)

  def update(self):
    if self.following:
      self.rect.center = pygame.mouse.get_pos()
    elif self.placed:
      pass
    else:
      move = pygame.math.Vector2((self.x-self.rect.x)/5, (self.y-self.rect.y)/5)
      self.rect.move_ip(move)

  def hover(self):
    targetY = self.y - CARD_RISE
    if self.rect.y != targetY:
      self.yMove = pygame.math.Vector2(0, (targetY-self.rect.y)/5)
      self.rect.move_ip(self.yMove)

    if not self.hovering:
      group = self.groups()[0]
      group.move_to_front(self)

    self.hovering = True
    
  def unhover(self):
    if self.rect.y != self.y:
      self.yMove = pygame.math.Vector2(0, (self.y-self.rect.y)/5)
      self.rect.move_ip(self.yMove)

    if self.hovering and not self.following:
      group = self.groups()[0]
      group.change_layer(self, self.index)
    
    self.hovering = False

  def follow(self):
    if not self.following:
      group = self.groups()[0]
      group.move_to_front(self)

    self.following = True
  
  def unfollow(self):
    if self.following and not self.hovering:
      group = self.groups()[0]
      group.change_layer(self, self.index)
    self.following = False

  def setX(self, x):
    self.x = x
    self.rect.centerx = x

  def setY(self, y):
    self.y = y
    self.rect.centery = y