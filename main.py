import pygame
from constants import *
from card import Card
from cardSpace import CardSpace

class Main:
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
  pygame.display.set_caption("The Scribe")
  clock = pygame.time.Clock()
  running = True

  hover = False

  BG = pygame.image.load("sprites/parchment.jpg").convert()
  BG = pygame.transform.scale(BG, (SCREEN_WIDTH * 1.05, SCREEN_HEIGHT * 1.05))

  handList = []
  handOfCards = pygame.sprite.LayeredUpdates()

  playerSpaceList = [CardSpace(), CardSpace(), CardSpace(), CardSpace()]
  playerCardSpaces = pygame.sprite.Group()
  for i in playerSpaceList:
    playerCardSpaces.add(i)
  placedCards = pygame.sprite.Group()

  @staticmethod
  def main():
    Main.posHand()
    Main.posPlayerSpaces()
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
          if card is not None:
            card.follow()

        if event.type == pygame.MOUSEBUTTONUP:
          for i in Main.handList:
            if i.following:
              for j in Main.playerSpaceList:
                if j.card is None and j.rect.collidepoint(pygame.mouse.get_pos()):
                  i.unfollow()
                  j.storeCard(i)
                  Main.placedCards.add(i)
                  Main.handList.remove(i)
                  Main.handOfCards.remove(i)
                  break
              i.unfollow()

      try:
        Main.selectCard().hover()
      except (AttributeError):
        pass

      Main.handOfCards.update()

      Main.placedCards.draw(Main.screen)

      Main.playerCardSpaces.draw(Main.screen)

      Main.handOfCards.draw(Main.screen)

      pygame.display.flip()

  @staticmethod
  def posHand():
    cardAmount = len(Main.handList)
    for i, card in enumerate(Main.handList):
      card.setLayer(i)
      card.setX((HAND_SPACE / cardAmount) * (Main.handList.index(card) + 1) + HAND_MARGIN - (HAND_SPACE/2/cardAmount))
      card.setY(HAND_HEIGHT)

  @staticmethod
  def posPlayerSpaces():
    spaceAmount = len(Main.playerSpaceList)
    for i, space in enumerate(Main.playerSpaceList):
      space.setX((PLACE_SPACE / spaceAmount) * (Main.playerSpaceList.index(space) + 1) + PLACE_MARGIN - (PLACE_SPACE/2/spaceAmount))
      space.setY(PLACE_HEIGHT)

  @staticmethod
  def selectCard():
    
    hitCards = []
    hitCardVal = []
    isFollowing = False
    for i in Main.handList:
      pos = pygame.mouse.get_pos()
      hit = i.rect.collidepoint(pos) or i.rect.collidepoint(pos[0], pos[1]-100)
      isFollowing = i.following or isFollowing
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
      if i != highestVal or isFollowing:
        card.unhover()
      else:
        return card


if __name__ == "__main__":
  pygame.init()
  Main.main()
  pygame.quit()