import pygame
from constants import FPS
from card import Card

class Main:
  screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  pygame.display.set_caption("The Scribe")
  clock = pygame.time.Clock()
  running = True

  hover = False

  BG = pygame.image.load("sprites/parchment.jpg").convert()

  handList = [Card(200, 200, 0), Card(400, 200, 1)]
  handOfCards = pygame.sprite.LayeredUpdates()
  handOfCards.add(handList[0])
  handOfCards.add(handList[1])


  @staticmethod
  def main():
    Main.posHand()
    while Main.running:
      Main.screen.blit(Main.BG, (0, 0))
      Main.clock.tick(FPS)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          Main.running = False
          exit()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            Main.running = False
            exit()

          if event.key == pygame.K_a:
            Main.handList.append(Card(index = len(Main.handList)))
            Main.handOfCards.add(Main.handList[-1])
            Main.posHand()

        if event.type == pygame.MOUSEBUTTONDOWN:
          card = Main.selectCard()
          if card != None:
            card.follow()

        if event.type == pygame.MOUSEBUTTONUP:
          card = Main.selectCard()
          if card != None:
            card.unfollow()

      try:
        Main.selectCard().hover()
      except (AttributeError):
        pass

      Main.handOfCards.update()

      Main.handOfCards.draw(Main.screen)

      pygame.display.flip()

  @staticmethod
  def posHand():
    cardAmount = len(Main.handList)
    for i, card in enumerate(Main.handList):
      card.setLayer(i)
      card.setX((800 / cardAmount) * (Main.handList.index(card) + 1) + 400 - (400/cardAmount))
      card.setY(700)

  @staticmethod
  def selectCard():
    
    hitCards = []
    hitCardVal = []
    for i in Main.handList:
      pos = pygame.mouse.get_pos()
      hit = i.rect.collidepoint(pos) or i.rect.collidepoint(pos[0], pos[1]-100)
      if hit:
        hitCards.append(i)
        hitCardVal.append(i.groups()[0].get_layer_of_sprite(i))
      else:
        i.unhover()
    
    if len(hitCardVal) > 0:
      highestVal = hitCardVal.index(max(hitCardVal))
    else:
      return None
    
    for i, card in enumerate(hitCards):
      if i != highestVal:
        card.unhover()
      else:
        return card


if __name__ == "__main__":
  pygame.init()
  Main.main()
  pygame.quit()