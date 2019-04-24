"""
an initial blank screen for a pygame video game

@author: Nima Created on Wed Apr 24 16:14:45 2019
"""

import pygame
import sys

class MovingDot():
    def __init__(self,left, top, width, height):
        self.player_rect=pygame.Rect(left, top, width, height)
        self.color=(255, 0, 0)
        self.screen = pygame.display.get_surface()    
    def set_pos_size(self,left, top, width, height):
        """sets the position of the top left corrner of the player rectangle"""
        self.player_rect=pygame.Rect(left, top, width, height)

    def display_rect(self):        
        pygame.draw.rect(self.screen, self.color, self.player_rect)
        
    def move_rect(self, x_step, y_step):
        self.player_rect=self.player_rect.move(x_step,y_step)
        
  
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    #Initialize Everything     
    pygame.init()
    screen = pygame.display.set_mode((800, 480))
    clock=pygame.time.Clock()
    dot_1=MovingDot(0, 0, 64, 64)
    dot_1.set_pos_size(40,40,65,64)
    dot_1.display_rect()
    print(dot_1.player_rect)    
    # main loop
    while True: 
        # a clock keeps the frame rate under 60
        clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        dot_1.move_rect(10,10)
        print(dot_1.player_rect)
        dot_1.display_rect()
        pygame.display.update()
    pygame.quit()
    
# game main loop
if __name__=="__main__":
    main()
        