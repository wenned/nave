import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_funcoes as gf

def run_game():
    pygame.init()
    sy = Settings()
    screen = pygame.display.set_mode((sy.screen_w, sy.screen_h))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(sy, screen)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(sy, screen, ship, aliens)
    
    while True:

        gf.check_events(sy, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(sy, screen, ship, aliens, bullets)
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                gf.sys.exit()
        
        screen.fill(sy.bg)
        ship.blitme()
        pygame.display.flip()
        

run_game()


