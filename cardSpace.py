import pygame

class CardSpace(pygame.sprite.Sprite):
  def __init__(self, x = 0, y = 0, card = None):
    super().__init__()
    self.image = pygame.image.load("sprites\parchment-card-outline.png").convert_alpha()
    self.rect = self.image.get_rect(center = (x, y))
    self.x = x
    self.y = y
    self.card = card

  def update(self):
    if self.card is not None:
      self.card.update()
  
  def storeCard(self, card):
    self.card = card
    self.card.placed = True
    card.setX(self.rect.centerx)
    card.setY(self.rect.centery)

  def setX(self, x):
    self.x = x
    self.rect.centerx = x

  def setY(self, y):
    self.y = y
    self.rect.centery = y