import sys

import pygame
from ship import Ship
from settings import Settings

class AlienInvasion:
     """Game Assets and Behavior for game"""
     
     def __init__(self):
          """Initialize game and create game resources"""
          pygame.init()
          
          self.ship = Ship(self)
          
          self.settings = Settings()
          
          self.screen = pygame.display.set_mode((
               self.settings.screen_width, self.settings.screen_height
          ))
          
          pygame.display.set_caption("Alien Invasion")
          
     def run_game(self):
          """ Start the main loop for the game"""
          while True:
               # Watch for interaction Mouse and Keyboad
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         sys.exit()
                         
               self.screen.fill(self.settings.bg_color)
               self.ship.blitme()
               
               # Make the most recently drawn screen visible
               pygame.display.flip()
               
               
if __name__ == '__main__':
     ai = AlienInvasion()
     ai.run_game()