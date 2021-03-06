import pygame
import random

class Character(object):
    def __init__(self):
        self.x = random.randint(0, 510)
        self.y = random.randint(0, 480)
        self.speed = 0
        self.duration = 0
        self.alive = True

    def move_north(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 480

    def move_east(self):
        self.x += self.speed
        if self.x > 510:
            self.x = 0

    def move_south(self):
        self.y += self.speed
        if self.y > 480:
            self.y = 0

    def move_west(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 510

    def move_northwest(self):
        self.x -= self.speed
        self.y -= self.speed
        if self.x < 0:
            self.x = 510
        if self.y < 0:
            self.y = 480

    def move_northeast(self):
        self.x += self.speed
        self.y -= self.speed
        if self.x > 510:
            self.x = 0
        if self.y < 0:
            self.y = 480

    def move_southeast(self):
        self.x += self.speed
        self.y += self.speed
        if self.x > 510:
            self.x = 0
        if self.y > 480:
            self.y = 0

    def move_southwest(self):
        self.x -= self.speed
        self.y += self.speed
        if self.x < 0:
            self.x = 510
        if self.y > 480:
            self.y = 0

    def direction_determination(self):
        direction_number = random.randint(0, 7)
        if direction_number == 0:
            self.move_north()
            return self.move_north()
        elif direction_number == 1:
            self.move_east()
            return self.move_east()
        elif direction_number == 2:
            self.move_south()
            return self.move_south()
        elif direction_number == 3:
            self.move_west()
            return self.move_west()
        elif direction_number == 4:
            self.move_northwest()
            return self.move_northwest()
        elif direction_number == 5:
            self.move_northeast()
            return self.move_northeast()
        elif direction_number == 6:
            self.move_southeast()
            return self.move_southeast()
        elif direction_number == 7:
            self.move_southwest()
            return self.move_southwest()

    def direction_duration(self):
        random_duration_number = random.randint(0,2)
        if random_duration_number == 0:
            self.duration = 1
        elif random_duration_number == 1:
            self.duration = 50
        elif random_duration_number == 2:
            self.duration = 80


    def alive_test(self, attacker):
        if (attacker.x + 32) < self.x:
            return self.alive
        elif (self.x + 32) < attacker.x:
            return self.alive
        elif (attacker.y + 32) < self.y:
            return self.alive
        elif (self.y + 32) < attacker.y:
            return self.alive
        else:
            self.alive = False
            return self.alive

class Hero(Character):
    def __init__(self):
        self.x = 255
        self.y = 240
        self.alive = True
        self.speed = 1
        self.sword_upgrade = False

    def move_north(self):
        if self.y > 25:
            self.y -= self.speed
    
    def move_east(self):
        if self.x < 455:
            self.x += self.speed

    def move_south(self):
        if self.y < 420:
            self.y += self.speed

    def move_west(self):
        if self.x > 25:
            self.x -= self.speed

    def move_around(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.move_north()
        if pressed[pygame.K_DOWN]:
            self.move_south()
        if pressed[pygame.K_RIGHT]:
            self.move_east()
        if pressed[pygame.K_LEFT]:
            self.move_west()

class Monster(Character):
    def __init__(self):
        super(Monster, self).__init__()
        self.speed = 5
        self.alive = True
        self.duration = 1

class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__()
        self.speed = 5
        self.duration = 1

class Sword(object):
    def __init__(self):
        self.x = random.randint(50, 460)
        self.y = random.randint(50, 430)
        self.available = True
        self.alive = True

    def alive_test(self, attacker):
        if (attacker.x + 32) < self.x:
            return self.available
        elif (self.x + 32) < attacker.x:
            return self.available
        elif (attacker.y + 32) < self.y:
            return self.available
        elif (self.y + 32) < attacker.y:
            return self.available
        else:
            self.available = False
            return self.available

def next_level(level_number):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        next_level_number = level_number + 1
        game(next_level_number)

def restart():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        game(1)

def game(level):
    current_level = level
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
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha()
    sword_image = pygame.image.load('images/sword_small.png').convert_alpha()

    sound = pygame.mixer.Sound('sounds/win.wav')
    sound_lost = pygame.mixer.Sound('sounds/lose.wav')
    music = pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1)
    
    font = pygame.font.Font(None, 25)
    text = font.render('Hit ENTER to go to the next level!', True, (255, 0, 0))
    text_lost = font.render('You lose! Hit ENTER to play again.', True, (255, 0, 0))
    level_display = font.render('Current Level: ' + str(current_level), True, (255, 0, 0))

    knight = Hero()
    orc = Monster()
    sword = Sword()
    
    goblin_number = current_level + 2
    
    character_list = [orc]
    goblin_list = []

    for i in range(0, goblin_number):
        goblin_1 = Goblin()
        character_list.append(goblin_1)
        goblin_list.append(goblin_1)

    change_dir_countdown = 5
    sword_counter = 600
    sword_upgrade_counter = 300
    sound_counter = 1

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 5
            for character in character_list:
                character.direction_determination()
        
        knight.move_around()
    
        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(level_display, (30, 30))

        if sword.available == True:
            sword_counter -= 1
            if 0 <= sword_counter <= 300:
                if sword.alive_test(knight) == True:
                    screen.blit(sword_image, (sword.x, sword.y))
                elif sword.alive_test(knight) == False:
                        knight.sword_upgrade = True
            if sword_counter < 0:
                sword.available = False

        if knight.sword_upgrade == True:
            sword_display = font.render('Sword Upgrade Timer: ' + str((sword_upgrade_counter / 60) +1), True, (255, 0, 0))
            screen.blit(hero_image, (knight.x, knight.y))
            if sword_upgrade_counter > 0:
                screen.blit(sword_display, (285, 30))
                if orc.alive_test(knight) == True:
                    screen.blit(monster_image, (orc.x, orc.y))
                elif orc.alive_test(knight) == False:
                    sound.play()
                    screen.blit(text, (160, 230))
                    next_level(current_level)
                for goblin in goblin_list:
                    if goblin.alive_test(knight) == False:
                       goblin_list.remove(goblin)
                for i in range(len(goblin_list)):
                    screen.blit(goblin_image, (goblin_list[i].x, goblin_list[i].y))
            if sword_upgrade_counter <= 0:
                knight.sword_upgrade = False
                screen.blit(hero_image, (knight.x, knight.y))
            sword_upgrade_counter -= 1

        if knight.sword_upgrade == False:
            for k in range(len(goblin_list)):
                screen.blit(goblin_image, (goblin_list[k].x, goblin_list[k].y))
            if orc.alive_test(knight) == True:
                screen.blit(monster_image, (orc.x, orc.y))
            elif orc.alive_test(knight) == False:
                sound.play()
                screen.blit(text, (120, 230))
                next_level(current_level)

            for goblin in goblin_list:
                if knight.alive_test(goblin) == True:
                    screen.blit(hero_image, (knight.x, knight.y))
                elif knight.alive_test(goblin) == False:
                    sound_lost.play()
                    screen.blit(text_lost, (130, 230))
                    restart()
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def main():
    game(1)


main()