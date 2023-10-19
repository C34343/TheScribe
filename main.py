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

      Main.handOfCards.update()  

      Main.handOfCards.draw(Main.screen)

      pygame.display.flip()

  @staticmethod
  def posHand():
    cardAmount = len(Main.handList)
    for card in Main.handList:
      card.setX((900 / cardAmount) * (Main.handList.index(card) + 1) + 350 - (450/cardAmount))
      card.setY(800)

if __name__ == "__main__":
  pygame.init()
  Main.main()
  pygame.quit()