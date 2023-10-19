import pygame

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

  def update(self):
    pos = pygame.mouse.get_pos()
    hit = self.rect.collidepoint(pos) or self.rect.collidepoint(pos[0], pos[1]-100)
    if hit:
      self.hover()
    else:
      self.unhover()

  def hover(self):
    targetY = self.y - 100
    if self.rect.y != targetY:
      self.yMove = pygame.math.Vector2(0, (targetY-self.rect.y)/5)
      self.rect.move_ip(self.yMove)

    if not self.hovering:
      group = self.groups()[0]
      self.index = group.get_layer_of_sprite(self)
      group.move_to_front(self)

    self.hovering = True
    
  def unhover(self):
    if self.rect.y != self.y:
      self.yMove = pygame.math.Vector2(0, (self.y-self.rect.y)/5)
      self.rect.move_ip(self.yMove)

    if self.hovering:
      group = self.groups()[0]
      group.change_layer(self, self.index-1)
    
    self.hovering = False

  def setX(self, x):
    self.x = x
    self.rect.x = x - 100

  def setY(self, y):
    self.y = y
    self.rect.y = y - 100