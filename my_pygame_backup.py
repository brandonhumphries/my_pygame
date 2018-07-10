import pygame
import random

class Monster(object):
    def __init__(self):
        self.x = random.randint(0, 510)
        self.y = random.randint(0, 480)

    def move_north(self):
        self.y -= 5
        if self.y < 0:
            self.y = 480
        # return self.y

    def move_east(self):
        self.x += 5
        if self.x > 510:
            self.x = 0
        # return self.x

    def move_south(self):
        self.y += 5
        if self.y > 480:
            self.y = 0
        # return self.y

    def move_west(self):
        self.x -= 5
        if self.x < 0:
            self.x = 510
        # return self.x
        

def main():
    width = 510
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    orc = Monster()

    # monster_x = random.randint(0, 510)
    # monster_y = random.randint(0, 480)
    change_dir_countdown = 120
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            direction_number = random.randint(0, 3)
            if direction_number == 0:
                orc.move_north()
            if direction_number == 1:
                orc.move_east()
            if direction_number == 2:
                orc.move_south()
            if direction_number == 3:
                orc.move_west()
        
        

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (255, 240))
        screen.blit(monster_image, (orc.x, orc.y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
