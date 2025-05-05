import pygame
from constants import *
from player import Player

def main():
    # Keep your existing print statements
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # Initialize pygame
    pygame.init()
    
    time_clock = pygame.time.Clock()
    dt = 0

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # In your main function, instantiate a Player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # Your game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with black
        screen.fill('black')
        player.update(dt)
        
        # re-render the player on the screen each frame
        player.draw(screen)

        # Update the display to show the changes
        pygame.display.flip()

        # At the end of each loop iteration, call tick on the time_clock object
        dt = time_clock.tick(60)/1000

if __name__ == "__main__":
    main()
